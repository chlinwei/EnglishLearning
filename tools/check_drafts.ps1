param(
    [string[]]$Scenario,
    [switch]$RequireAll
)

$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$bank = Get-Content (Join-Path $repo 'sources/phrases.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$phrases = @{}
foreach ($phrase in $bank.phrases) {
    if ($phrases.ContainsKey($phrase.id)) { throw "Duplicate phrase: $($phrase.id)" }
    $phrases[$phrase.id] = $phrase
}
$drafts = @{}
foreach ($file in Get-ChildItem (Join-Path $repo 'sources/drafts') -Filter 'S*.json' | Sort-Object Name) {
    $draft = Get-Content $file.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
    $drafts[$file.BaseName] = $draft
    foreach ($phrase in $draft.phraseDefinitions) {
        if ($phrases.ContainsKey($phrase.id)) { throw "Duplicate phrase: $($phrase.id)" }
        $phrases[$phrase.id] = $phrase
    }
}
if ($RequireAll) {
    foreach ($number in 3..50) {
        $name = 'S{0:00}' -f $number
        if (-not $drafts.ContainsKey($name)) { throw "Missing draft: $name" }
    }
}
$names = @($drafts.Keys | Sort-Object)
if ($Scenario) { $names = @($Scenario) }
$banned = 'i would like to|in order to|furthermore|moreover|i am writing to|please find|kindly note that|as per|it is imperative|we should note that'
$indianPattern = '\bright\?\s*$|\bonly[.!]?\s*$|\bitself\b|\bi have a doubt\b|\bhave a doubt\b|\bdo one thing\b|\bprepone\b|\b(?:am|is|are) having\b'
$rows = @()
$failures = @()
foreach ($name in $names) {
    if (-not $drafts.ContainsKey($name)) { throw "Missing draft: $name" }
    $draft = $drafts[$name]
    $number = [int]$name.Substring(1)
    if ($draft.dialogues.Count -ne 10) { $failures += "$name must have 10 dialogues" }
    $total = 0
    $india = 0
    $turns = 0
    $minimumShort = 1.0
    $known = @{}
    foreach ($phrase in $bank.phrases) { $known[$phrase.id] = $true }
    foreach ($previous in $drafts.Keys) {
        if ([int]$previous.Substring(1) -lt $number) {
            foreach ($phrase in $drafts[$previous].phraseDefinitions) { $known[$phrase.id] = $true }
        }
    }
    foreach ($item in $draft.dialogues) {
        $tag = "$name/$($item.id)"
        $expected = '{0:0000}' -f (($number - 1) * 10 + 6 + $item.part - 1)
        if ($item.id -ne $expected -or $item.part -lt 1 -or $item.part -gt 10) { $failures += "$tag invalid numbering" }
        if ($item.lines.Count -lt 8) { $failures += "$tag needs at least 8 substantive turns" }
        $blob = $item.lines.en -join ' '
        if ($blob -match $banned) { $failures += "$tag banned wording" }
        if (-not $item.title -or -not $item.premise -or -not $item.listeningTask) { $failures += "$tag missing learning metadata" }
        $core = 0
        if ($item.phrases.Count -ne 6) { $failures += "$tag needs 6 expressions" }
        if ($item.phrases -notcontains $item.newPhrase -or $known.ContainsKey($item.newPhrase)) { $failures += "$tag invalid new expression" }
        foreach ($spec in $item.phrases) {
            $parts = $spec -split ':'
            $phrase = $phrases[$parts[0]]
            if (-not $phrase) { $failures += "$tag unknown expression $($parts[0])"; continue }
            if ($blob.IndexOf($phrase.en, [StringComparison]::OrdinalIgnoreCase) -lt 0) { $failures += "$tag expression absent $($parts[0])" }
            if ($parts[0] -ne $item.newPhrase -and -not $known.ContainsKey($parts[0])) { $failures += "$tag expression not yet introduced $($parts[0])" }
            $level = $phrase.level
            if ($parts.Count -gt 1) { $level = $parts[1] }
            if ($level -eq 'core') { $core++ }
        }
        if ($core -lt 1 -or $core -gt 3) { $failures += "$tag core expression quota" }
        $known[$item.newPhrase] = $true
        $sentences = @([regex]::Split($blob.Trim(), '(?<=[.!?])\s+'))
        $full = @($sentences | Where-Object { [regex]::Matches($_, "[A-Za-z0-9']+").Count -ge 3 })
        $sum = 0
        foreach ($sentence in $full) { $sum += [regex]::Matches($sentence, "[A-Za-z0-9']+").Count }
        $average = $sum / [math]::Max(1, $full.Count)
        $short = @($sentences | Where-Object { [regex]::Matches($_, "[A-Za-z0-9']+").Count -lt 8 }).Count / [math]::Max(1, $sentences.Count)
        $minimumShort = [math]::Min($minimumShort, $short)
        if ($average -lt 5 -or $average -gt 9.5 -or $short -lt 0.5) { $failures += "$tag sentence metrics average=$([math]::Round($average,2)) short=$([math]::Round($short,2))" }
        $hasIndian = $false
        foreach ($line in $item.lines) {
            $speaker = $draft.speakers.($line.sp)
            if (-not $speaker -or -not $line.en -or -not $line.zh) { $failures += "$tag invalid bilingual speaker line"; continue }
            if ($line.PSObject.Properties.Name -contains 'start' -or $line.PSObject.Properties.Name -contains 'end') { $failures += "$tag invented timeline" }
            $words = [regex]::Matches($line.en, "[A-Za-z0-9']+").Count
            $total += $words
            $turns++
            if ($speaker.accent -eq 'en-IN') {
                $india += $words
                foreach ($sentence in [regex]::Split($line.en, '(?<=[.!?])\s+')) {
                    if ($sentence -match $indianPattern) { $hasIndian = $true }
                }
            } elseif ($speaker.accent -ne 'German-accented English') { $failures += "$tag unsupported accent" }
        }
        if (-not $hasIndian) { $failures += "$tag missing Indian-role feature" }
    }
    if (@($draft.dialogues.part | Sort-Object -Unique).Count -ne 10) { $failures += "$name duplicate parts" }
    $share = $india / [math]::Max(1, $total)
    if ($share -lt 0.55 -or $share -gt 0.65) { $failures += "$name Indian word share=$([math]::Round($share,3))" }
    $rows += [pscustomobject]@{Scenario=$name; Segments=$draft.dialogues.Count; Turns=$turns; Words=$total; IndianPercent=[math]::Round(100*$share,1); MinShortPercent=[math]::Round(100*$minimumShort,1)}
}
$rows | Format-Table -AutoSize
if ($failures.Count) {
    $failures | ForEach-Object { Write-Output "FAIL: $_" }
    throw "$($failures.Count) draft checks failed"
}
Write-Output "PASS: $($names.Count) drafts. Text checks only; audio and editorial acceptance remain separate."