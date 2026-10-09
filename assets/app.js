/* IT 会议英语练习库 · 共享应用
   三种页面共用本文件，靠 body 上的 data-* 区分：
     index.html                data-mode="index"  data-root=""
     player.html               data-mode="player" data-root=""
     audio/<g>/<item>/<x>.html data-mode="item"   data-root="../../../" data-id="0007"
   数据来自 data/catalog.js 与 data/talks.js（用 <script src> 加载，file:// 双击可用） */

(function () {
  'use strict';

  var body = document.body;
  var ROOT = body.getAttribute('data-root') || '';
  var MODE = body.getAttribute('data-mode') || 'player';
  var FIXED = body.getAttribute('data-id') || '';

  var CAT = window.CATALOG || { groups: [], items: [], mediaRoot: 'audio' };
  var TALKS = window.TALKS || {};
  var MEDIA = CAT.mediaRoot || 'audio';

  var GROUPS = (CAT.groups || []).slice().sort(function (a, b) { return (a.order || 99) - (b.order || 99); });
  var GMAP = {}; GROUPS.forEach(function (g) { GMAP[g.id] = g; });
  var ITEMS = (CAT.items || []).slice();
  var IMAP = {}; ITEMS.forEach(function (x) { IMAP[x.id] = x; });

  var PH = window.PHRASES || { phrases: {} };
  var SERIES = (CAT.series || []).slice();
  var SMAP = {}; SERIES.forEach(function (s) { SMAP[s.id] = s; });

  function seriesItems(sid) {
    return ITEMS.filter(function (x) { return sid && x.series === sid; })
      .sort(function (a, b) { return (a.part || 0) - (b.part || 0) || (a.id < b.id ? -1 : 1); });
  }
  function phOf(pid) { return (PH.phrases || {})[pid] || null; }

  /* ---------- 集合（事件线）与段号 ----------
     每个素材都属于一个「集合」：有 series 的用事件线标题，
     没有的退回用所属场景当集合。段号 = 它在集合里的第几段 / 共几段。 */
  var SPOS = {};
  function skey(it) { return it.series || ('#' + it.group); }
  function sOf(it) { return SMAP[it.series || ''] || SMAP[skey(it)] || null; }
  function sTitle(it) { var se = sOf(it); return se ? se.title : ((GMAP[it.group] || {}).name || '未分集合'); }
  (function buildPos() {
    var buckets = {};
    ITEMS.forEach(function (x) { var k = skey(x); (buckets[k] = buckets[k] || []).push(x); });
    Object.keys(buckets).forEach(function (k) {
      buckets[k].slice().sort(function (a, b) {
        return (a.part || 0) - (b.part || 0) || (a.id < b.id ? -1 : 1);
      }).forEach(function (x, i) { SPOS[x.id] = { k: i + 1, n: buckets[k].length }; });
    });
  })();
  function noOf(it) { return SPOS[it.id] || { k: 1, n: 1 }; }
  function noTxt(it) { var p = noOf(it); return p.n > 1 ? p.k + '/' + p.n : ''; }
  function serOf(list, sid) {
    return list.filter(function (x) { return skey(x) === sid; })
      .sort(function (a, b) { return (a.part || 0) - (b.part || 0) || (a.id < b.id ? -1 : 1); });
  }
  function durOf(list) { return list.reduce(function (a, x) { return a + (x.duration || 0); }, 0); }
  function doneOf(list) { return list.filter(function (x) { return PROG[x.id] && PROG[x.id].done; }).length; }

  var PKEY = 'iel.progress', UKEY = 'iel.ui';
  function readJSON(k, d) { try { var s = localStorage.getItem(k); return s ? JSON.parse(s) : d; } catch (e) { return d; } }
  function writeJSON(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  var PROG = readJSON(PKEY, {});
  var UI = readJSON(UKEY, {}) || {};

  var esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };
  function fmt(t) {
    t = Math.max(0, t || 0);
    return Math.floor(t / 60) + ':' + String(Math.floor(t % 60)).padStart(2, '0');
  }
  var subNames = function (it) { var b = it.audio.replace(/\.[^.]+$/, ''); return { both: b + '.vtt', en: b + '.en.vtt', zh: b + '.zh.vtt' }; };
  var hrefOf = function (it) { return ROOT + 'player.html#' + it.id; };
  var mediaOf = function (it) { return ROOT + MEDIA + '/' + it.dir + '/' + it.audio; };
  var dirOf = function (it) { return ROOT + MEDIA + '/' + it.dir + '/'; };
  var pctOf = function (it) {
    var p = PROG[it.id];
    if (!p) return -1;
    if (p.done) return 100;
    if (!p.t || !it.duration) return 0;
    return Math.min(99, Math.round(p.t / it.duration * 100));
  };
  function dotOf(it) {
    var p = PROG[it.id];
    if (p && p.done) return '<span class="dot d"></span>';
    if (p && p.t > 2) return '<span class="dot p" style="--p:' + pctOf(it) + '%"></span>';
    return '<span class="dot"></span>';
  }
  function stat(v, k) { return '<div class="stat"><div class="v">' + v + '</div><div class="k">' + esc(k) + '</div></div>'; }

  /* ---------- 搜索 ---------- */
  var query = '';
  var openGroups = UI.open || null;
  function isOpen(gid) { if (query.trim()) return true; if (!openGroups) return true; return openGroups[gid] !== false; }
  function matches(it, f) {
    if (!f) return true;
    var g = GMAP[it.group];
    var hay = [it.id, it.title, it.scene, it.accent, (it.tags || []).join(' '), (it.roles || []).join(' '),
      g ? g.name + ' ' + g.en : ''].join(' ').toLowerCase();
    return f.split(/\s+/).filter(Boolean).every(function (w) { return hay.indexOf(w) >= 0; });
  }
  function visibleItems() {
    var f = query.trim().toLowerCase();
    return ITEMS.filter(function (it) { return matches(it, f); });
  }

  /* ---------- 侧栏 ---------- */
  var cur = null;

  /* 口音在列表里压缩成短标签，完整描述放到 title 悬浮 */
  function accentShort(a) {
    a = a || '';
    if (!a) return '';
    var inId = a.indexOf('印度') >= 0, inBr = a.indexOf('英式') >= 0 || a.indexOf('英音') >= 0;
    if (inId && inBr) return '印英混杂';
    if (inId) return '印度音';
    if (inBr) return '英音';
    if (a.indexOf('美') >= 0) return '美音';
    return a.slice(0, 6);
  }

  function itRow(it) {
    var bits = ['#' + it.id, fmt(it.duration)];
    var acc = accentShort(it.accent);
    if (acc) bits.push(acc);
    var inner = '<span class="no">' + esc(noTxt(it)) + '</span>' + dotOf(it)
      + '<span class="tx"' + (it.accent ? ' title="' + esc(it.title + ' · ' + it.accent) + '"' : '')
      + '><span class="t1">' + esc(it.title) + '</span>'
      + '<span class="t2">' + esc(bits.join(' · ')) + '</span></span>';
    if (cur && cur.id === it.id) return '<div class="it cur" data-id="' + it.id + '">' + inner + '</div>';
    return '<a class="it" data-id="' + it.id + '" href="' + hrefOf(it) + '">' + inner + '</a>';
  }

  function renderSidebar() {
    var vis = visibleItems();
    var html = '';
    GROUPS.forEach(function (g) {
      var list = vis.filter(function (x) { return x.group === g.id; });
      if (!list.length) return;
      var dn = doneOf(list);
      var sers = [];
      list.forEach(function (x) { var k = skey(x); if (sers.indexOf(k) < 0) sers.push(k); });
      var named = sers.some(function (sid) { return !!SMAP[sid]; });
      var body;
      if (named) {
        /* 每个集合都带一条小标题：集合名 + 已练/总数 + 合计时长 */
        body = sers.map(function (sid) {
          var arr = serOf(list, sid);
          if (!arr.length) return '';
          var se = SMAP[sid];
          var name = se ? se.title : (GMAP[list[0].group] || {}).name || '未分集合';
          var meta = doneOf(arr) + '/' + arr.length;
          if (arr.length > 1) meta += ' · ' + fmt(durOf(arr));
          return '<div class="shead"><span class="sh-t">' + esc(name) + '</span>'
            + '<span class="sn">' + esc(meta) + '</span></div>'
            + arr.map(itRow).join('');
        }).join('');
      } else {
        body = list.map(itRow).join('');
      }
      html += '<div class="grp" data-g="' + g.id + '" data-open="' + (isOpen(g.id) ? 1 : 0) + '">'
        + '<button class="grp-h"><span class="car">▾</span>' + esc(g.name)
        + '<span class="n">' + dn + '/' + list.length + '</span></button>'
        + '<div class="grp-b">' + body + '</div></div>';
    });
    var nav = document.getElementById('nav');
    nav.innerHTML = html || '<div class="empty">没有匹配的素材。换个关键词试试。</div>';
    var doneAll = doneOf(ITEMS);
    document.getElementById('sideStat').innerHTML =
      '<span>已练完 ' + doneAll + ' / ' + ITEMS.length + '</span>'
      + '<span class="pbar"><i style="width:' + (ITEMS.length ? Math.round(doneAll / ITEMS.length * 100) : 0) + '%"></i></span>';
    var bc = document.getElementById('brandCount');
    if (bc) bc.textContent = ITEMS.length + ' 段素材 · '
      + GROUPS.filter(function (g) { return ITEMS.some(function (x) { return x.group === g.id; }); }).length + ' 个场景';
  }

  /* ---------- 布局 ---------- */
  function layout() {
    document.getElementById('app').innerHTML =
      '<div class="wrap"><aside class="side">'
      + '<a class="brand" href="' + ROOT + 'index.html"><span class="brand-t">IT 会议英语</span>'
      + '<span class="brand-s" id="brandCount"></span></a>'
      + '<input id="q" class="q" type="search" placeholder="搜索标题 / 场景 / 标签 / 角色…" autocomplete="off">'
      + '<div class="side-scroll" id="nav"></div>'
      + '<div class="side-foot"><div class="prog" id="sideStat"></div>'
      + '<button class="mini" id="clearProg">清除练习进度</button></div>'
      + '</aside><main class="main" id="main"></main></div>';

    var q = document.getElementById('q');
    q.addEventListener('input', function () {
      query = q.value;
      renderSidebar();
      if (MODE === 'index') document.getElementById('main').innerHTML = indexMain();
    });
    document.getElementById('nav').addEventListener('click', function (e) {
      var h = e.target.closest ? e.target.closest('.grp-h') : null;
      if (!h) return;
      var grp = h.parentNode, gid = grp.getAttribute('data-g');
      var nowOpen = grp.getAttribute('data-open') === '1';
      grp.setAttribute('data-open', nowOpen ? '0' : '1');
      openGroups = openGroups || {};
      openGroups[gid] = !nowOpen;
      UI.open = openGroups;
      writeJSON(UKEY, UI);
    });
    document.getElementById('clearProg').addEventListener('click', function () {
      if (!confirm('清除全部练习进度？此操作不可撤销。')) return;
      PROG = {}; writeJSON(PKEY, PROG);
      renderSidebar();
      if (MODE === 'index') document.getElementById('main').innerHTML = indexMain();
      var c = document.getElementById('cnt'); if (c) c.textContent = '';
    });
  }

  /* ---------- 播放器（player.html 与每段条目页共用） ---------- */
  var au, tr, cnt, spk, sen, szh, loopBtn, noticeEl;
  var L = [], mode = UI.mode || 'both', rate = UI.rate || 1;
  var lineLoop = false, curLine = -1, loopIdx = -1, chain = !!UI.chain, lastSave = 0;

  var PLAYER_MAIN =
    '<div id="head"></div>'
    + '<div id="pre"></div>'
    + '<div class="notice" id="notice"></div>'
    + '<audio id="au" controls preload="metadata"></audio>'
    + '<div class="bar">'
    + '<button id="prev">上一句</button><button id="next">下一句</button><button id="loop">循环本句</button>'
    + '<span class="lbl">语速</span>'
    + '<button class="sp" data-s="0.75">0.75×</button><button class="sp" data-s="1">1.0×</button><button class="sp" data-s="1.25">1.25×</button>'
    + '<span class="lbl">字幕</span>'
    + '<button class="md" data-m="off">关</button><button class="md" data-m="en">英文</button>'
    + '<button class="md" data-m="both">中英</button><button class="md" data-m="zh">中文</button>'
    + '<span class="lbl">字号</span>'
    + '<button class="fs" data-f="md">标准</button><button class="fs" data-f="lg">大</button><button class="fs" data-f="xl">特大</button>'
    + '<span class="cnt" id="cnt"></span>'
    + '</div>'
    + '<div class="opts">'
    + '<label class="ck"><input type="checkbox" id="resume"> 自动续听</label>'
    + '<label class="ck"><input type="checkbox" id="chain"> 连听本组</label>'
    + '<label class="ck"><input type="checkbox" id="markdone"> 标记本段已练完</label>'
    + '</div>'
    + '<div class="stage"><div class="spk" id="spk"></div><div class="en" id="sen"></div><div class="zh" id="szh"></div></div>'
    + '<div id="ph"></div>'
    + '<h2>逐句稿（点击任意句跳转，右侧「循环」可只重复该句）</h2><div id="tr"></div>'
    + '<div id="sernav"></div>'
    + '<p class="tip" id="tip"></p>';

  function setFs(v, silent) {
    document.documentElement.setAttribute('data-fs', v);
    document.querySelectorAll('.fs').forEach(function (b) { b.classList.toggle('on', b.dataset.f === v); });
    UI.fs = v;
    if (!silent) writeJSON(UKEY, UI);
  }

  function buildTranscript() {
    tr.innerHTML = L.map(function (c, i) {
      return '<div class="row" data-i="' + i + '"><div class="idx">' + (i + 1) + '</div>'
        + '<div class="body"><div class="who">' + esc(c.sp + (c.role ? ' · ' + c.role : '')) + '  [' + fmt(c.start) + ']</div>'
        + '<div class="e">' + esc(c.en) + '</div><div class="z">' + esc(c.zh) + '</div></div>'
        + '<button class="rep" title="只循环这一句">循环</button></div>';
    }).join('');
    tr.querySelectorAll('.row').forEach(function (row, i) {
      row.addEventListener('click', function (e) {
        if (e.target.classList.contains('rep')) return;
        seekLine(i);
      });
      row.querySelector('.rep').addEventListener('click', function (e) {
        e.stopPropagation();
        loopIdx = i; lineLoop = true; loopBtn.classList.add('on'); markRep(i); seekLine(i); au.play();
      });
    });
  }
  function markRep(i) { tr.querySelectorAll('.rep').forEach(function (b, k) { b.classList.toggle('on', k === i); }); }
  function seekLine(i) { if (!L.length) return; i = Math.max(0, Math.min(L.length - 1, i)); au.currentTime = L[i].start; curLine = -1; if (lineLoop) loopIdx = i; }

  function renderCue(i) {
    if (i === curLine) return;
    curLine = i;
    tr.querySelectorAll('.row').forEach(function (r, k) { r.classList.toggle('on', k === i); });
    if (i < 0 || !L[i]) { spk.innerHTML = ''; sen.textContent = ''; szh.textContent = ''; return; }
    var c = L[i];
    spk.innerHTML = '<b>' + esc(c.sp + (c.role ? ' · ' + c.role : '')) + '</b>  [' + fmt(c.start) + ']';
    sen.textContent = c.en;
    szh.textContent = c.zh;
    applyMode();
  }
  function applyMode() {
    sen.classList.toggle('hide', !(mode === 'en' || mode === 'both'));
    szh.classList.toggle('hide', !(mode === 'zh' || mode === 'both'));
    spk.classList.toggle('hide', mode === 'off');
  }

  function saveTime(force) {
    if (!cur) return;
    var p = PROG[cur.id] || { t: 0, done: 0 };
    p.t = au.currentTime || 0;
    if (cur.duration && p.t >= cur.duration - 2.5) p.done = 1;
    p.at = Date.now();
    PROG[cur.id] = p;
    var now = Date.now();
    if (force || now - lastSave > 3000) { lastSave = now; writeJSON(PKEY, PROG); updateDot(cur.id); }
  }
  function updateDot(id) {
    var it = IMAP[id]; if (!it) return;
    var node = document.querySelector('.it[data-id="' + id + '"]');
    if (!node) return;
    var old = node.querySelector('.dot');
    if (old) old.outerHTML = dotOf(it);
  }

  function toggleDone(v) {
    if (!cur) return;
    var p = PROG[cur.id] || { t: 0 };
    p.done = v ? 1 : 0; p.at = Date.now();
    PROG[cur.id] = p; writeJSON(PKEY, PROG);
    updateDot(cur.id); renderSidebar();
  }

  function open(id, noScroll) {
    var it = IMAP[id];
    if (!it) {
      var h = document.getElementById('head');
      if (h) h.innerHTML = '<h1>找不到素材</h1><p class="sub">编号 ' + esc(id) + ' 不在索引里。</p>'
        + '<p class="meta"><a href="' + ROOT + 'index.html">返回练习库首页</a></p>';
      return;
    }
    if (cur && cur.id !== it.id) saveTime(true);
    cur = it;
    L = (TALKS[id] && TALKS[id].lines) || [];
    curLine = -1; loopIdx = -1; lineLoop = false; loopBtn.classList.remove('on');
    markRep(-1);

    var g = GMAP[it.group] || { name: '' };
    var se = sOf(it);
    var no = noOf(it);
    var s = subNames(it);
    document.title = (no.n > 1 ? no.k + '/' + no.n + ' ' : '') + it.title + ' · IT 会议英语';
    document.getElementById('head').innerHTML =
      '<div class="crumb"><a href="' + ROOT + 'index.html">练习库</a> / ' + esc(g.name)
      + (se ? ' / <span class="ser">' + esc(se.title) + '</span>' : '')
      + (no.n > 1 ? ' / 第 ' + no.k + ' / ' + no.n + ' 段' : '') + '</div>'
      + '<h1>' + esc(it.title)
      + (no.n > 1 ? ' <span class="stageb no">第 ' + no.k + ' / ' + no.n + ' 段</span>' : '')
      + (it.stage ? ' <span class="stageb">' + esc(it.stage) + '</span>' : '') + '</h1>'
      + '<p class="sub">' + esc(it.scene) + '</p>'
      + '<p class="meta">'
      + '<b>' + fmt(it.duration) + '</b> · 共 <b>' + L.length + ' 句</b>'
      + (it.domain ? ' · 技术域：' + esc(it.domain) : '')
      + (it.roles && it.roles.length ? ' · 角色：' + esc(it.roles.join('、')) : '')
      + (it.accent ? ' · ' + esc(it.accent) : '')
      + (it.tags && it.tags.length ? '<br>' + it.tags.map(function (t) { return '<span class="tag">' + esc(t) + '</span>'; }).join('') : '')
      + '</p>';

    document.getElementById('tip').innerHTML =
      '快捷键：<kbd>空格</kbd> 播放/暂停 · <kbd>←</kbd><kbd>→</kbd> 前后 3 秒 · <kbd>↑</kbd><kbd>↓</kbd> 上一句 / 下一句<br>'
      + '音频：<code>' + esc(it.audio) + '</code> · 字幕：<code>' + esc(s.both) + '</code> 中英 · <code>'
      + esc(s.en) + '</code> 英文 · <code>' + esc(s.zh) + '</code> 中文<br>'
      + '用 PotPlayer 打开同目录的 MP3，会自动加载同名字幕（右键 → 字幕 → 显示/隐藏）。文件位置：<code>'
      + esc(MEDIA + '/' + it.dir + '/') + '</code>';

    /* 上文衔接（同场次续听用） */
    document.getElementById('pre').innerHTML = it.premise
      ? '<div class="premise"><b>上回说到</b>' + esc(it.premise) + '</div>' : '';

    /* 本段重点表达 + 复现信息（“反复出现”的可视化） */
    var phs = (it.phrases || []).map(function (x) {
      var b = phOf(x.id);
      if (!b) return null;
      return { id: b.id, en: b.en, zh: b.zh, layer: b.layer, target: b.target,
               note: b.note, seen: b.seen || [], level: x.level };
    }).filter(Boolean);
    document.getElementById('ph').innerHTML = phs.length
      ? '<h2>本段重点表达（★ 必记 · ○ 了解即可）</h2><div class="ph">'
        + phs.map(function (p) {
          var seen = p.seen || [], n = seen.length;
          var others = seen.filter(function (x) { return x !== it.id; });
          var line = '<div class="phc' + (p.level === 'core' ? ' core' : '') + '">'
            + '<div class="phe">' + (p.level === 'core' ? '★ ' : '○ ') + esc(p.en) + '</div>'
            + '<div class="phz">' + esc(p.zh) + '</div>'
            + '<div class="phm"><span class="ly">' + esc(p.layer) + '</span>'
            + '<span class="cn">已出现 <b>' + n + '</b> 次'
            + (p.target ? ' · 目标 ' + p.target + ' 次' : '') + '</span></div>';
          if (p.note) line += '<div class="phn">' + esc(p.note) + '</div>';
          if (others.length) {
            line += '<div class="phs">也出现在：' + others.map(function (x) {
              var t = IMAP[x];
              return '<a href="' + hrefOf({ id: x }) + '" title="' + esc(t ? t.title : '') + '">' + x + '</a>';
            }).join(' ') + '</div>';
          }
          return line + '</div>';
        }).join('')
        + '</div>'
      : '';

    /* 同场次前后导航 */
    var seq2 = seriesItems(it.series);
    if (seq2.length > 1) {
      var pos = -1;
      seq2.forEach(function (x, k) { if (x.id === it.id) pos = k; });
      var pv = pos > 0 ? seq2[pos - 1] : null;
      var nx = pos >= 0 && pos < seq2.length - 1 ? seq2[pos + 1] : null;
      document.getElementById('sernav').innerHTML = '<div class="sernav">'
        + (pv ? '<a class="sb" href="' + hrefOf(pv) + '">← 第 ' + noOf(pv).k + ' / ' + noOf(pv).n + ' 段 · ' + esc(pv.title) + '</a>'
          : '<span class="sb gap"></span>')
        + '<a class="smid" href="' + ROOT + 'index.html">' + esc(se ? se.title : '') + '</a>'
        + (nx ? '<a class="sb" href="' + hrefOf(nx) + '">第 ' + noOf(nx).k + ' / ' + noOf(nx).n + ' 段 · ' + esc(nx.title) + ' →</a>'
          : '<span class="sb gap"></span>')
        + '</div>';
    } else {
      document.getElementById('sernav').innerHTML = '';
    }

    au.src = mediaOf(it);
    au.playbackRate = rate;

    buildTranscript();
    renderCue(-1);

    var p = PROG[id];
    var resume = document.getElementById('resume').checked;
    if (resume && p && p.t > 5 && (!it.duration || p.t < it.duration - 3)) {
      au.currentTime = Math.max(0, p.t - 2);
      showNotice('已从上次位置 <b>' + fmt(p.t) + '</b> 继续。要重头听就点一下进度条最左边。');
    } else showNotice('');

    document.getElementById('markdone').checked = !!(p && p.done);
    document.getElementById('cnt').textContent = '0 / ' + L.length;

    UI.last = id; writeJSON(UKEY, UI);
    renderSidebar();
    if (!FIXED) { try { history.replaceState(null, '', '#' + id); } catch (e) { } }
    if (!noScroll) window.scrollTo(0, 0);
    var node = document.querySelector('.it[data-id="' + id + '"]');
    if (node && node.scrollIntoView) node.scrollIntoView({ block: 'nearest' });
  }

  function showNotice(html) { noticeEl.innerHTML = html; noticeEl.style.display = html ? 'block' : 'none'; }

  function tick() {
    var t = au.currentTime;
    if (lineLoop && loopIdx >= 0 && L[loopIdx]) {
      var c = L[loopIdx];
      if (t >= c.end - 0.05 || t < c.start - 0.15) au.currentTime = c.start;
    }
    var found = -1;
    for (var i = 0; i < L.length; i++) { if (t >= L[i].start - 0.05) found = i; else break; }
    renderCue(found);
    cnt.textContent = (found < 0 ? 0 : found + 1) + ' / ' + L.length;
    saveTime(false);
  }

  function beginPlayer() {
    document.getElementById('main').innerHTML = PLAYER_MAIN;
    au = document.getElementById('au');
    tr = document.getElementById('tr');
    cnt = document.getElementById('cnt');
    spk = document.getElementById('spk');
    sen = document.getElementById('sen');
    szh = document.getElementById('szh');
    loopBtn = document.getElementById('loop');
    noticeEl = document.getElementById('notice');

    au.playbackRate = rate;
    var sb = document.querySelector('.sp[data-s="' + rate + '"]');
    if (!sb) { rate = 1; au.playbackRate = 1; sb = document.querySelector('.sp[data-s="1"]'); }
    if (sb) sb.classList.add('on');
    var mb = document.querySelector('.md[data-m="' + mode + '"]');
    if (!mb) { mode = 'both'; mb = document.querySelector('.md[data-m="both"]'); }
    if (mb) mb.classList.add('on');
    setFs(UI.fs || 'md', true);
    document.getElementById('resume').checked = UI.resume !== false;
    document.getElementById('chain').checked = !!UI.chain;
    chain = !!UI.chain;

    document.querySelectorAll('.sp').forEach(function (b) {
      b.addEventListener('click', function () {
        rate = parseFloat(b.dataset.s); au.playbackRate = rate;
        document.querySelectorAll('.sp').forEach(function (x) { x.classList.toggle('on', x === b); });
        UI.rate = rate; writeJSON(UKEY, UI);
      });
    });
    document.querySelectorAll('.md').forEach(function (b) {
      b.addEventListener('click', function () {
        mode = b.dataset.m;
        document.querySelectorAll('.md').forEach(function (x) { x.classList.toggle('on', x === b); });
        UI.mode = mode; writeJSON(UKEY, UI);
        curLine = -1; tick();
      });
    });
    document.querySelectorAll('.fs').forEach(function (b) { b.addEventListener('click', function () { setFs(b.dataset.f); }); });

    document.getElementById('prev').addEventListener('click', function () { seekLine(curLine < 0 ? 0 : curLine - 1); });
    document.getElementById('next').addEventListener('click', function () { seekLine(curLine + 1); });
    loopBtn.addEventListener('click', function () {
      lineLoop = !lineLoop; loopBtn.classList.toggle('on', lineLoop);
      if (lineLoop) { loopIdx = Math.max(0, curLine); markRep(loopIdx); } else { loopIdx = -1; markRep(-1); }
    });
    document.getElementById('resume').addEventListener('change', function () { UI.resume = this.checked; writeJSON(UKEY, UI); });
    document.getElementById('chain').addEventListener('change', function () { chain = this.checked; UI.chain = chain; writeJSON(UKEY, UI); });
    document.getElementById('markdone').addEventListener('change', function () { toggleDone(this.checked); });

    au.addEventListener('timeupdate', tick);
    au.addEventListener('seeked', function () { curLine = -1; tick(); });
    au.addEventListener('pause', function () { saveTime(true); });
    au.addEventListener('ended', function () {
      saveTime(true);
      if (PROG[cur.id]) { PROG[cur.id].done = 1; writeJSON(PKEY, PROG); updateDot(cur.id); }
      renderSidebar();
      document.getElementById('markdone').checked = true;
      if (chain) {
        var list = visibleItems();
        var k = list.findIndex(function (x) { return x.id === cur.id; });
        if (k >= 0 && k < list.length - 1) { open(list[k + 1].id); au.play(); }
      }
    });
    window.addEventListener('beforeunload', function () { saveTime(true); });

    document.addEventListener('keydown', function (e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.target.tagName === 'BUTTON' && e.code === 'Space') return;
      if (e.code === 'Space') { e.preventDefault(); au.paused ? au.play() : au.pause(); }
      else if (e.code === 'ArrowLeft') { au.currentTime = Math.max(0, au.currentTime - 3); }
      else if (e.code === 'ArrowRight') { au.currentTime = Math.min(au.duration || 1e9, au.currentTime + 3); }
      else if (e.code === 'ArrowUp') { e.preventDefault(); document.getElementById('prev').click(); }
      else if (e.code === 'ArrowDown') { e.preventDefault(); document.getElementById('next').click(); }
    });

    var start = FIXED || (location.hash || '').replace(/^#/, '') || UI.last || (ITEMS[0] && ITEMS[0].id);
    if (start && !IMAP[start]) start = ITEMS[0] && ITEMS[0].id;
    open(start, true);

    if (!FIXED) {
      window.addEventListener('hashchange', function () {
        var id = (location.hash || '').replace(/^#/, '');
        if (id && (!cur || id !== cur.id)) open(id);
      });
    }
  }

  /* ---------- 首页 ---------- */
  function indexMain() {
    var totalDur = ITEMS.reduce(function (a, x) { return a + (x.duration || 0); }, 0);
    var doneAll = ITEMS.filter(function (x) { return PROG[x.id] && PROG[x.id].done; }).length;
    var usedGroups = GROUPS.filter(function (g) { return ITEMS.some(function (x) { return x.group === g.id; }); });
    var html = '<h1 class="big">IT 会议英语 · 练习库</h1>'
      + '<p class="sub">真实会议场景，逐句中英对照、可变速、可循环单句。音频与字幕同目录同名，'
      + '可直接用 PotPlayer 打开（会自动挂上字幕）。</p>'
      + '<div class="stats">' + stat(ITEMS.length, '段素材') + stat(doneAll, '已练完')
      + stat(fmt(totalDur), '总时长') + stat(usedGroups.length, '个场景')
      + stat(SERIES.filter(function (s) {
        return s.id !== 'baseline' && ITEMS.some(function (x) { return x.series === s.id; });
      }).length, '条事件线') + '</div>';

    var p = UI.last && IMAP[UI.last] ? IMAP[UI.last] : null;
    if (!p) p = ITEMS.find(function (x) { return !(PROG[x.id] && PROG[x.id].done); }) || ITEMS[0];
    if (p) {
      var pp = PROG[p.id];
      html += '<div class="notice" style="display:block">'
        + (pp && pp.t > 5 && !pp.done ? '上次听到 <b>' + esc(p.title) + '</b> ' + fmt(pp.t) + ' —— '
          : '接着练：')
        + '<a href="' + hrefOf(p) + '"><b>' + esc(p.title) + '</b> →</a></div>';
    }

    html += '<h2>按场景</h2><div class="cards">';
    usedGroups.forEach(function (g) {
      var list = ITEMS.filter(function (x) { return x.group === g.id; });
      var dn = doneOf(list);
      var first = list.find(function (x) { return !(PROG[x.id] && PROG[x.id].done); }) || list[0];
      var sers = [];
      list.forEach(function (x) { var k = skey(x); if (sers.indexOf(k) < 0) sers.push(k); });
      var sl = sers.map(function (sid) {
        var arr = serOf(list, sid);
        if (!arr.length) return '';
        var se = SMAP[sid];
        return '<a class="sl" href="' + hrefOf(arr[0]) + '">'
          + '<span class="sl-t">' + esc(se ? se.title : '（未分集合）') + '</span>'
          + '<span class="sl-n">' + doneOf(arr) + '/' + arr.length + '</span></a>';
      }).join('');
      html += '<div class="card' + (dn < list.length ? ' a' : '') + '">'
        + '<div class="ct">' + esc(g.name) + ' <span class="tag">' + esc(g.en) + '</span></div>'
        + '<div class="cd">' + esc(g.desc || '') + '</div>'
        + (sl ? '<div class="sers">' + sl + '</div>' : '')
        + '<div class="prog"><span>' + dn + '/' + list.length + '</span>'
        + '<span class="pbar"><i style="width:' + (list.length ? Math.round(dn / list.length * 100) : 0) + '%"></i></span></div>'
        + '<div class="cn"><a href="' + hrefOf(first) + '">' + (dn < list.length ? '继续练' : '再看一遍')
        + '：' + esc(first.title) + ' →</a></div></div>';
    });
    html += '</div>';

    /* 按事件线（场次串联的可视入口） */
    var seriesUsed = SERIES.filter(function (s) {
      return s.id !== 'baseline' && ITEMS.some(function (x) { return x.series === s.id; });
    });
    if (seriesUsed.length) {
      html += '<h2>按集合：同一场会议切成 ≤2 分钟的连续片段，接着上一段听</h2><div class="cards">';
      seriesUsed.forEach(function (s) {
        var list = seriesItems(s.id);
        var dn = doneOf(list);
        var first = list.find(function (x) { return !(PROG[x.id] && PROG[x.id].done); }) || list[0];
        var g2 = GMAP[s.group];
        var dur = durOf(list);
        var chips = list.map(function (x) {
          var d2 = PROG[x.id] && PROG[x.id].done;
          return '<a class="seg' + (d2 ? ' done' : '') + '" href="' + hrefOf(x) + '" title="'
            + esc(noOf(x).k + '. ' + x.title + ' · ' + fmt(x.duration)) + '">' + noOf(x).k + '</a>';
        }).join('');
        html += '<div class="card' + (dn < list.length ? ' a' : '') + '">'
          + '<div class="ct">' + esc(s.title) + ' <span class="tag">'
          + esc((g2 ? g2.name : s.group) + ' · ' + (s.domain || '')) + '</span></div>'
          + '<div class="cd">' + esc(list.length + ' 段 · 合计 ' + fmt(dur) + ' · ' + (s.impact || '')) + '</div>'
          + '<div class="segs">' + chips + '</div>'
          + '<div class="prog"><span>' + dn + '/' + list.length + '</span>'
          + '<span class="pbar"><i style="width:' + Math.round(dn / list.length * 100) + '%"></i></span></div>'
          + '<div class="cn"><a href="' + hrefOf(first) + '">' + (dn ? '继续' : '开始')
          + '：第 ' + noOf(first).k + ' / ' + list.length + ' 段 · ' + esc(first.title) + ' →</a></div></div>';
      });
      html += '</div>';
    }

    var list2 = visibleItems(), cap = 300;
    html += '<h2>全部素材' + (list2.length > cap ? '（前 ' + cap + ' 条，用左侧搜索缩小范围）' : '') + '</h2><div class="tbl">'
      + '<div class="tr head"><span>编号</span><span>标题</span><span class="ser-c">集合 · 段</span>'
      + '<span>时长</span><span>状态</span></div>';
    list2.slice(0, cap).forEach(function (it) {
      var p2 = PROG[it.id];
      var st = p2 && p2.done ? '<span class="st d">已练完</span>'
        : (p2 && p2.t > 2 ? '<span class="st p">' + pctOf(it) + '%</span>' : '<span class="st">未开始</span>');
      html += '<a class="tr" href="' + hrefOf(it) + '"><span class="seq">' + it.id + '</span>'
        + '<span class="nm">' + esc(it.title) + '</span>'
        + '<span class="ser-c" title="' + esc(sTitle(it)) + ' 第 ' + noOf(it).k + ' 段">'
        + '<span class="sers-n">' + esc(sTitle(it)) + '</span>'
        + '<b class="segn">' + esc(noTxt(it)) + '</b></span>'
        + '<span class="du">' + fmt(it.duration) + '</span>' + st + '</a>';
    });
    html += '</div>';
    if (!list2.length) html = '<h1 class="big">没有匹配的素材</h1><p class="sub">清空左侧搜索框试试。</p>';
    html += '<p class="note">新增素材：把对话写进 <code>sources/dialogues.json</code>，'
      + '运行 <code>python tools/build.py</code> 即可生成索引与页面，不需要改动任何已有文件。</p>';
    return html;
  }

  /* ---------- 启动 ---------- */
  layout();
  if (MODE === 'index') {
    document.getElementById('main').innerHTML = indexMain();
    document.title = 'IT 会议英语 · 练习库';
  } else {
    beginPlayer();
  }
  renderSidebar();
  document.getElementById('q').value = query;
})();
