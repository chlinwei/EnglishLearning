import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {
    "us": {"date": "2025-01-20", "contextEn": "Trump began his second presidential term and outlined goals on trade, border policy, and prices in his inaugural address.", "contextZh": "特朗普开始总统第二任期，并在就职演说中提出贸易、边境政策和物价方面的目标。", "url": "https://www.whitehouse.gov/remarks/2025/01/the-inaugural-address/"},
    "jp": {"date": "2025-02-07", "contextEn": "Trump and Japan's then prime minister, Shigeru Ishiba, met in Washington. Their joint statement covered security, investment, technology, and energy.", "contextZh": "特朗普与当时的日本首相石破茂在华盛顿会谈。联合声明涉及安全、投资、技术和能源。", "url": "https://www.whitehouse.gov/briefings-statements/2025/02/united-states-japan-joint-leaders-statement/"},
    "kr": {"date": "2025-11-13", "contextEn": "A joint fact sheet described Trump's October 29 meeting with South Korean President Lee Jae Myung and commitments on trade, investment, and alliance cooperation.", "contextZh": "联合情况说明介绍了特朗普10月29日与韩国总统李在明的会谈，以及贸易、投资和同盟合作方面的承诺。", "url": "https://www.whitehouse.gov/fact-sheets/2025/11/joint-fact-sheet-on-president-donald-j-trumps-meeting-with-president-lee-jae-myung/"},
    "eu": {"date": "2025-07-27", "contextEn": "The European Commission's trade overview records an EU-U.S. trade arrangement reached in July 2025, followed by a joint statement in August.", "contextZh": "欧盟委员会贸易专题页记载，欧美于2025年7月达成贸易安排，随后于8月发布联合声明。", "url": "https://commission.europa.eu/topics/trade/eu-us-trade-deal_en"},
}

TOPICS = [
    ("us", "A second term, not a completed agenda", "第二任期：目标不是结果", "policy agenda", "政策议程", "An agenda sets out priorities. It doesn't prove that those priorities have been delivered.", "议程列出优先事项，但不能证明这些事项已经完成。", "A confident speech can make a proposal sound like a settled outcome.", "自信的演说可能让提议听起来像既定结果。", "Compare the speech with dated policy documents and implementation records.", "把演说与有日期的政策文件和执行记录进行比较。"),
    ("us", "Tariffs and who pays", "关税：究竟谁付钱", "import duty", "进口关税", "Importers pay duties at the border. The wider cost can be shared through prices and profit margins.", "进口商在边境缴纳关税，更广泛的成本可能通过价格和利润率分担。", "The country named in a tariff headline isn't necessarily the party writing the cheque.", "关税标题中提到的国家，不一定就是实际开支票的一方。", "Check the customs rules, the product category, and who imports the goods.", "核查海关规则、产品类别和实际进口方。"),
    ("us", "Prices versus inflation", "物价与通胀不是一回事", "inflation rate", "通胀率", "Slower inflation means prices are rising more slowly, not necessarily falling.", "通胀放缓意味着价格上涨变慢，不一定意味着价格下降。", "A lower rate can still leave households facing higher prices than before.", "即使涨幅下降，家庭面对的价格仍可能比以前高。", "Look at the price index, its period, and the comparison being made.", "查看价格指数、统计时期和比较基准。"),
    ("us", "Executive action and legislation", "行政措施与立法", "executive order", "行政命令", "An executive order directs executive action within legal limits. It isn't the same as a law passed by Congress.", "行政命令在法律范围内指示行政行动，不等同于国会通过的法律。", "Signing an order doesn't settle every question about its authority or implementation.", "签署命令并不解决所有权限和落实问题。", "Read the order, its legal basis, and any relevant court decisions.", "阅读命令、法律依据和相关法院裁决。"),
    ("us", "A court pause isn't a final ruling", "法院暂停措施不等于终局裁决", "temporary injunction", "临时禁令", "A temporary injunction can pause an action while a case continues.", "临时禁令可以在案件继续审理时暂停某项行动。", "A headline about a blocked policy may leave out that the dispute is still ongoing.", "政策被阻止的标题可能省略争议仍在进行这一点。", "Check the court, the scope of the order, and whether it is temporary or final.", "核查法院、命令适用范围以及是临时还是终局决定。"),
    ("us", "Border policy and different legal categories", "边境政策：不同法律身份", "asylum claim", "庇护申请", "An asylum claim is a request for protection assessed under applicable law.", "庇护申请是根据适用法律接受评估的保护请求。", "Reports can blur the distinction between a person's claim, legal status, and case outcome.", "报道可能混淆个人的申请、法律身份和案件结果。", "Check which category the report describes and the procedure that applies.", "核查报道描述的类别和适用程序。"),
    ("us", "Budget plans and actual spending", "预算计划与实际支出", "budget proposal", "预算提案", "A proposal sets out intended spending. Approval and actual expenditure are separate steps.", "提案列出拟议支出，批准和实际支付是另外的步骤。", "An announced saving may be a projection rather than money already saved.", "宣布的节省金额可能是预测，而非已实现的节省。", "Compare proposed amounts, approved budgets, and audited expenditure.", "比较拟议金额、批准预算和经审计支出。"),
    ("us", "Jobs promised and jobs created", "承诺岗位与新增就业", "job creation", "创造就业", "A promise to create jobs is different from measured employment growth.", "创造就业的承诺与统计到的就业增长不同。", "Gross hiring can hide job losses elsewhere or count positions that aren't filled yet.", "招聘总量可能掩盖其他地方的岗位损失，或包含尚未填补的职位。", "Check net employment, the time period, and whether figures are forecasts.", "核查净就业、时间区间和数字是否属于预测。"),
    ("us", "Trade deficits and what they show", "贸易逆差说明什么", "trade deficit", "贸易逆差", "A goods trade deficit means a country imports more goods than it exports over a stated period.", "货物贸易逆差指一国在规定时期内的货物进口超过出口。", "A goods figure alone doesn't describe services trade or the whole economy.", "单看货物数字不能描述服务贸易或整个经济。", "Check whether the figure covers goods, services, or both.", "核查数字涵盖货物、服务还是两者。"),
    ("us", "Promises to bring production home", "生产回流的承诺", "reshoring", "生产回流", "Reshoring means bringing production back to a firm's home country.", "生产回流指把生产迁回企业的本国。", "Moving a factory can take years and depends on skills, costs, and suppliers.", "迁移工厂可能耗时数年，并取决于技能、成本和供应商。", "Look for construction milestones and production, not just an announcement.", "查看建设节点和实际生产，而不只是公告。"),
    ("us", "Energy policy and household bills", "能源政策与家庭账单", "energy prices", "能源价格", "Supply is one factor in energy prices; demand, infrastructure, and market conditions matter too.", "供应是影响能源价格的因素之一，需求、基础设施和市场情况也重要。", "A drilling announcement doesn't guarantee an immediate fall in household bills.", "钻探公告不能保证家庭账单立即下降。", "Compare production data, wholesale prices, and retail bills over time.", "比较不同时期的产量数据、批发价格和零售账单。"),
    ("us", "Polling numbers and uncertainty", "民调数字与不确定性", "margin of error", "误差范围", "A poll estimates views from a sample rather than asking every voter.", "民调通过样本估计看法，而非询问每位选民。", "A small change may fall within sampling uncertainty, and methods can differ.", "小幅变化可能处于抽样不确定性范围内，方法也可能不同。", "Check fieldwork dates, sample design, question wording, and uncertainty.", "核查调查日期、样本设计、问题措辞和不确定性。"),
    ("us", "Campaign language in a news report", "报道中的竞选措辞", "campaign pledge", "竞选承诺", "A campaign pledge tells us what a candidate says they intend to do.", "竞选承诺说明候选人表示打算做什么。", "Repeating a slogan without attribution can make a political claim sound like a verified fact.", "不注明来源地重复口号，可能让政治主张听起来像核实过的事实。", "Identify the speaker and separate the pledge from evidence of delivery.", "辨认发言者，并把承诺与兑现证据分开。"),
    ("us", "Negotiating leverage or lasting policy", "谈判筹码还是长期政策", "bargaining leverage", "谈判筹码", "Leverage is an advantage used to influence negotiations.", "筹码是用来影响谈判的优势。", "We can't assume a threat is only a negotiating tactic or that it will definitely happen.", "不能假定威胁只是谈判手段，也不能断言它一定会发生。", "Follow formal decisions and dated statements instead of guessing private intentions.", "关注正式决定和有日期的声明，不猜测私下动机。"),
    ("us", "A headline and the full quotation", "标题与完整引述", "context", "语境", "Context includes the surrounding remarks and the question being answered.", "语境包括前后讲话内容和当时回答的问题。", "A short clip can leave out a condition that changes the meaning.", "短视频可能省略改变原意的条件。", "Check the fuller recording and the date before interpreting a clip.", "解释片段前先查看更完整的记录和日期。"),
    ("jp", "What the summit statement actually says", "峰会声明究竟说了什么", "joint statement", "联合声明", "A joint statement records positions or intentions that the parties choose to publish together.", "联合声明记录双方选择共同公布的立场或意向。", "Agreement on wording doesn't mean every project is funded or complete.", "对措辞达成一致不等于每项项目都已有资金或已经完成。", "Compare commitments with later contracts, budgets, and implementation reports.", "把承诺与后续合同、预算和落实报告进行比较。"),
    ("jp", "Gas imports and energy security", "天然气进口与能源安全", "LNG", "液化天然气", "LNG is natural gas cooled into liquid so it can be transported by ship.", "液化天然气是冷却成液体、便于船运的天然气。", "More suppliers can offer options, but price, capacity, and contract terms still matter.", "更多供应商可提供选择，但价格、运力和合同条件仍然重要。", "Check contract volumes, delivery dates, and the basis for price comparisons.", "核查合同数量、交付日期和价格比较依据。"),
    ("jp", "Investment intentions and business decisions", "投资意向与企业决策", "investment intention", "投资意向", "An intention signals a possible future investment rather than a completed transaction.", "意向表明未来投资的可能性，而非已完成交易。", "Government encouragement doesn't make every company commit money.", "政府鼓励不意味着每家企业都会投入资金。", "Look for company disclosures and project-specific agreements.", "查看企业披露和具体项目协议。"),
    ("jp", "Supply chains and concentration risk", "供应链与集中风险", "supply chain resilience", "供应链韧性", "Resilience is the ability to keep operating or recover when supplies are disrupted.", "韧性是供应中断时继续运作或恢复的能力。", "Adding a supplier may help, but several suppliers can still share the same bottleneck.", "增加供应商可能有帮助，但多个供应商仍可能依赖同一个瓶颈。", "Map critical inputs and where production and transport depend on one another.", "梳理关键投入以及生产和运输的相互依赖。"),
    ("jp", "Security pledges and operational details", "安全承诺与执行细节", "security commitment", "安全承诺", "A security commitment sets out a promise whose meaning depends on its terms and legal framework.", "安全承诺是一项保证，其含义取决于具体条款和法律框架。", "A strong phrase in a statement doesn't answer every question about a future response.", "声明中的强烈措辞并不能回答未来应对的所有问题。", "Read the relevant agreement and distinguish public commitments from hypothetical actions.", "阅读相关协议，区分公开承诺与假设行动。"),
    ("jp", "Defence plans and fiscal years", "防务计划与财政年度", "fiscal year", "财政年度", "A fiscal year is the accounting period used for a budget and may differ from the calendar year.", "财政年度是预算采用的会计期间，可能与日历年不同。", "Comparing figures from different periods can create a misleading impression.", "比较不同统计期间的数字可能产生误导。", "Check the fiscal period, currency, and whether amounts are proposed or approved.", "核查财政期间、币种和金额是拟议还是已批准。"),
    ("jp", "Export controls and normal trade", "出口管制与普通贸易", "export controls", "出口管制", "Export controls restrict specified products or technologies under defined rules.", "出口管制依据明确规则限制特定产品或技术。", "A restriction on one category isn't automatically a ban on all trade.", "限制一种类别不自动等于禁止所有贸易。", "Check the covered items, destinations, and licensing requirements.", "核查涉及物项、目的地和许可要求。"),
    ("jp", "Diplomatic language and disagreement", "外交措辞与分歧", "shared interests", "共同利益", "Shared interests describe areas where parties see benefits in working together.", "共同利益指各方认为合作有益的领域。", "Positive diplomatic wording doesn't prove the absence of disagreement.", "积极的外交措辞不能证明双方没有分歧。", "Compare the statement's specific commitments with issues it leaves unaddressed.", "比较声明中的具体承诺和未涉及的问题。"),
    ("jp", "Domestic effects of foreign policy", "外交政策的国内影响", "domestic impact", "国内影响", "Domestic impact means effects on people, businesses, or institutions inside a country.", "国内影响指对一国境内个人、企业或机构产生的影响。", "A diplomatic success claim doesn't show how costs and benefits are distributed.", "外交成功的说法不能说明成本和收益如何分配。", "Seek sector-level evidence and avoid treating one interview as a national view.", "查找行业层面的证据，不把一次采访当成全国看法。"),
    ("jp", "Exchange rates and imported costs", "汇率与进口成本", "exchange rate", "汇率", "An exchange rate is the price of one currency in terms of another.", "汇率是一种货币以另一种货币计价的价格。", "A currency move can affect import costs without passing straight through to every shop price.", "汇率变动可影响进口成本，但不一定直接传导到每种零售价。", "Check the currency pair, period, and how businesses price their imports.", "核查货币对、时期以及企业如何给进口品定价。"),
    ("kr", "A meeting date and a publication date", "会谈日期与发布日期", "publication date", "发布日期", "The date a document is published may be later than the event it describes.", "文件发布日期可能晚于它描述的事件。", "Calling an older meeting today's meeting changes the timeline.", "把较早的会谈称为今天的会谈，会改变时间线。", "Read the event date in the body as well as the date above the headline.", "既阅读正文中的事件日期，也查看标题上方的日期。"),
    ("kr", "Investment commitments and funding", "投资承诺与资金到位", "investment commitment", "投资承诺", "A commitment may set out intended funding subject to agreed conditions.", "承诺可能列出受约定条件限制的拟议资金投入。", "A large announced total isn't proof that all the money has been transferred.", "宣布一个庞大的总额不能证明资金已经全部转移。", "Check funding schedules, conditions, and recorded disbursements.", "核查资金时间表、条件和实际支付记录。"),
    ("kr", "Shipbuilding cooperation and capacity", "造船合作与产能", "production capacity", "生产能力", "Capacity is how much an industry can produce with its available facilities and workforce.", "产能指行业利用现有设施和劳动力可以生产多少。", "An order doesn't instantly create trained workers or more shipyard space.", "订单不会立即创造熟练工人或更多船厂空间。", "Look for facility upgrades, workforce plans, and delivery schedules.", "查看设施升级、人员计划和交付时间表。"),
    ("kr", "Car tariffs and effective dates", "汽车关税与生效日期", "effective date", "生效日期", "An effective date tells us when a specified rule starts to apply.", "生效日期说明某项规则何时开始适用。", "Announced terms may require further steps before importers can use them.", "宣布的条款可能还需要后续步骤，进口商才能使用。", "Check the customs notice and the exact goods covered on the relevant date.", "核查海关通知和相关日期具体涵盖的货物。"),
    ("kr", "Currency stability and financing", "汇率稳定与融资", "foreign exchange market", "外汇市场", "Foreign exchange markets allow currencies to be bought and sold.", "外汇市场用于买卖货币。", "Large financing plans can raise questions about timing and currency demand without proving instability.", "大规模融资计划可能引发对时点和货币需求的疑问，但不能据此证明市场不稳定。", "Check financing arrangements and market data rather than assuming an announced sum moves at once.", "核查融资安排和市场数据，不假设公告金额会一次性流动。"),
    ("kr", "Alliance cooperation and budget choices", "同盟合作与预算选择", "defence spending", "国防支出", "Defence spending covers resources allocated to defence under a budget framework.", "国防支出是预算框架中用于防务的资源。", "A planned share of GDP doesn't by itself tell us the final amount or how it is spent.", "计划中的GDP占比不能单独说明最终金额或具体用途。", "Compare plans with approved budgets and the GDP measure used.", "比较计划与获批预算，并核对采用的GDP口径。"),
    ("kr", "Technology industries and supply risks", "技术产业与供应风险", "semiconductor supply", "半导体供应", "Chip supply depends on several stages, including design, manufacturing, and packaging.", "芯片供应依赖设计、制造和封装等多个环节。", "Investment in one stage doesn't eliminate shortages in every other stage.", "投资一个环节不意味着其他环节的短缺都会消失。", "Identify the chip type and the production stage discussed in the report.", "辨认报道中的芯片类型和生产环节。"),
    ("kr", "Trade barriers beyond tariffs", "关税之外的贸易壁垒", "non-tariff barrier", "非关税壁垒", "Non-tariff barriers are obstacles to trade other than customs duties.", "非关税壁垒是关税之外的贸易障碍。", "Some requirements serve safety goals, so their effects and justification need separate assessment.", "部分要求服务于安全目标，因此影响和合理性应分别评估。", "Read the specific requirement and evidence about its effect on market access.", "阅读具体要求及其影响市场准入的证据。"),
    ("kr", "Cooperation and legal conditions", "合作与法律条件", "subject to legal requirements", "须符合相关法律要求", "This phrase means an action depends on satisfying applicable legal conditions.", "这句话意味着行动取决于满足适用法律条件。", "Leaving out the condition can turn limited support into an unconditional promise.", "省略条件可能把有限支持变成无条件承诺。", "Keep the qualifying words and check which approval process applies.", "保留限定词，并核查适用的批准程序。"),
    ("kr", "Business deals and public benefits", "商业安排与公众收益", "economic benefit", "经济收益", "Economic benefits can differ for firms, workers, consumers, and public finances.", "企业、工人、消费者和公共财政获得的经济收益可能不同。", "A business contract doesn't establish an equal gain for every group.", "商业合同不能证明每个群体获益相同。", "Ask who benefits, who bears costs, and what outcomes have been measured.", "追问谁获益、谁承担成本，以及已衡量哪些结果。"),
    ("eu", "The EU isn't all of Europe", "欧盟不等于整个欧洲", "European Union", "欧洲联盟", "The EU is a union of member states, not a name for every country in Europe.", "欧盟是成员国组成的联盟，不是欧洲所有国家的统称。", "Calling an EU measure a rule for all of Europe can misstate its scope.", "把欧盟措施说成全欧洲的规则，可能误述适用范围。", "Check membership and whether the policy applies to the EU or particular countries.", "核查成员资格，以及政策适用于欧盟还是特定国家。"),
    ("eu", "A trade arrangement and its next steps", "贸易安排与后续步骤", "trade framework", "贸易框架", "A framework sets out an approach that can require further agreements or implementing measures.", "框架规定一种安排，可能还需后续协议或实施措施。", "A political announcement and a rule in force aren't always the same stage.", "政治公告与已生效规则不一定处于同一阶段。", "Build a timeline of announcement, publication, approval, and implementation.", "整理宣布、发布、批准和实施的时间线。"),
    ("eu", "Predictable doesn't mean cheap", "可预期不等于便宜", "predictability", "可预期性", "Predictability helps businesses plan around known conditions.", "可预期性帮助企业根据已知条件规划。", "A predictable charge can still be costly for a low-margin business.", "可预期收费对于低利润企业仍可能很昂贵。", "Compare planning benefits with the actual cost for the relevant sector.", "比较规划上的好处与相关行业的实际成本。"),
    ("eu", "Tariff ceilings and exceptions", "关税上限与例外", "tariff ceiling", "关税上限", "A ceiling is a maximum within a stated scope, not necessarily a rate for every product.", "上限是在规定范围内的最高值，不一定是每种产品的税率。", "Exceptions and product categories can change what an importer actually pays.", "例外和产品分类可能改变进口商实际缴纳的金额。", "Check the dated tariff schedule rather than using a headline rate for everything.", "核查有日期的税则表，不把标题税率套用到所有商品。"),
    ("eu", "Different industries, different outcomes", "不同行业，不同结果", "sectoral impact", "行业影响", "Sectoral impact describes how a measure affects a particular industry.", "行业影响描述措施如何影响某个特定行业。", "An average can hide different outcomes for agriculture, manufacturing, and services.", "平均数可能掩盖农业、制造业和服务业不同的结果。", "Break down the evidence by industry and identify the affected products.", "按行业细分证据，并辨认受影响产品。"),
    ("eu", "Rules, standards, and market access", "规则、标准与市场准入", "market access", "市场准入", "Market access concerns the conditions under which goods or services can enter a market.", "市场准入涉及商品或服务进入市场所需的条件。", "Reducing tariffs alone doesn't remove every regulatory requirement.", "仅降低关税不能消除所有监管要求。", "Check tariffs alongside testing, certification, and product rules.", "同时核查关税、检测、认证和产品规则。"),
    ("eu", "Energy purchases and diversification", "能源采购与供应多元化", "diversification", "多元化", "Diversification spreads reliance across suppliers or sources.", "多元化把依赖分散到不同供应商或来源。", "Replacing one dependency with another may leave some concentration risk.", "用一种依赖取代另一种依赖，可能仍存在集中风险。", "Compare supplier shares, contract lengths, and infrastructure constraints.", "比较供应商份额、合同期限和基础设施限制。"),
    ("eu", "Member states and a common position", "成员国与共同立场", "common position", "共同立场", "A common position is a stance agreed through the relevant collective process.", "共同立场是通过相关集体程序达成的立场。", "A statement from one national leader doesn't automatically speak for every member state.", "一位国家领导人的声明不自动代表所有成员国。", "Identify whether the speaker represents a government, an EU institution, or a party.", "辨认发言者代表政府、欧盟机构还是政党。"),
    ("eu", "The UK and EU rules", "英国与欧盟规则", "jurisdiction", "管辖范围", "Jurisdiction helps identify which authority's rules apply to a place or activity.", "管辖范围帮助判断某地或某项活动适用哪个机构的规则。", "A report using European as shorthand may blur different legal arrangements.", "报道用欧洲作简称时，可能混淆不同法律安排。", "Check the country and the specific agreement instead of assuming uniform rules.", "核查国家和具体协议，不假定规则完全一致。"),
    ("eu", "Compromise and the alternative", "妥协与替代方案", "counterfactual", "反事实情景", "A counterfactual asks what might have happened under a different choice.", "反事实情景询问作出另一种选择时可能发生什么。", "An imagined alternative isn't directly observed evidence that a deal was the best possible one.", "想象中的替代情景不是能直接观察到的证据，不能证明安排已经最优。", "State assumptions and compare plausible alternatives without presenting them as events.", "明确假设并比较合理替代方案，不把它们说成已发生事件。"),
    ("eu", "Retaliation and escalation", "反制与升级", "retaliatory measure", "反制措施", "A retaliatory measure is an action taken in response to another party's measure.", "反制措施是回应另一方措施而采取的行动。", "A warning about retaliation isn't proof that the measure is already in effect.", "反制警告不能证明措施已经生效。", "Separate threats, adopted measures, and effective dates in the timeline.", "在时间线上区分威胁、已通过措施和生效日期。"),
    ("eu", "Goods, services, and competing totals", "货物、服务与不同统计总额", "trade in services", "服务贸易", "Services trade includes cross-border activities such as finance, travel, and business services.", "服务贸易包括金融、旅游和商业服务等跨境活动。", "Comparing a goods-only total with a goods-and-services total can mislead.", "把仅货物总额与货物及服务总额相比可能误导。", "Match the categories, period, and data source before comparing balances.", "比较差额前统一类别、时期和数据来源。"),
    ("eu", "Political agreement and legal approval", "政治共识与法律批准", "approval process", "批准程序", "An approval process determines which institutions must authorise a measure under applicable rules.", "批准程序根据适用规则确定哪些机构必须授权某项措施。", "Different types of agreements follow different procedures; there isn't one universal route.", "不同类型协议采用不同程序，并不存在统一路径。", "Check the legal instrument and its required steps rather than guessing from the title.", "核查法律文件类型和必要步骤，不根据标题猜测。"),
    ("eu", "Updates and the risk of reading backwards", "更新页面与时间错置", "as of", "截至", "As of anchors a claim to the information available at a stated time.", "截至把说法限定到规定时间可获得的信息。", "A current web page may include later developments that weren't known when an older video was made.", "当前网页可能包含旧视频制作时尚不知晓的后续发展。", "Match the report date with dated documents and label later updates separately.", "把报道日期与有日期文件对应，并单独标明后续更新。"),
    ("eu", "Reporting, analysis, and opinion", "事实报道、分析与评论", "attribution", "归因与来源标注", "Attribution tells the audience who makes a claim rather than silently adopting it.", "来源标注明确谁提出说法，而非不加说明地接受它。", "A confident commentator can sound factual while offering a judgement.", "自信的评论者可能在表达判断时听起来像在陈述事实。", "Identify evidence, named sources, and evaluative language in each passage.", "辨认每段中的证据、具名来源和评价性语言。"),
]


HIGHLIGHT_NOTES = {
    "breaking news": "指正在发生或刚被报道的重要消息。不是所有新上传的视频都属于突发新闻；这里not presenting this as明确否定这一定位。",
    "context": "指理解事件所需的背景或上下文。give someone context是提供背景；out of context表示脱离语境。",
    "stated position": "指某方公开表达的立场。stated强调说了什么，不代表观点已得到证实或承诺已落实。",
    "separate evidence": "指另外、独立的证据。这里强调公告本身不足以证明成效，需要额外材料；separate不自动等于经过独立核实。",
    "in context": "表示结合前后内容或事件背景理解。put something in context是把某事放回语境中解释，不只是逐词翻译。",
    "qualification": "这里不是学历或资格，而是限制某项说法成立范围的条件，如只有满足某条件才适用。",
    "possibility": "表示可能发生或成立的情况。turn a possibility into a certainty指把尚不确定的说法讲成定论。",
    "certainty": "指确定性、确信程度。新闻中要区分已证实事实与预测，不能把may或could的语气抹掉。",
    "drawing a conclusion": "draw a conclusion是根据信息得出结论，draw不是画图。before drawing a conclusion表示先核查再判断。",
    "on its own": "表示单独、仅凭它本身。这里it wouldn't establish...on its own说明单个采访不足以证明总体效果。",
    "without overstating it": "overstate是夸大程度或重要性。without后用动词-ing，表示解释时不要把有限证据说得过满。",
    "implying": "imply指没有直接说出但让人理解为某种意思。与explicitly state明确陈述不同，要留意报道暗含的推断。",
    "I see your point": "回应异议的自然说法，表示理解对方理由，不一定同意全部结论。后接but可以礼貌说明保留意见。",
    "Fair enough": "承认对方理由合理，类似有道理、可以理解。通常是简短回应，不表示全面认同对方立场。",
    "attribution": "新闻中的来源归属：明确谁说了这句话，如according to officials。标明来源不等于证实其说法。",
    "independently verified": "表示由独立于原说法来源的核查确认。not independently verified常用于提醒某项说法仍无法独立证实。",
    "got this right": "get something right表示理解或处理正确。let me check I've got this right用于复述前确认自己没有听错。",
    "watch out for": "表示留意、提防某种风险或错误，后接名词。这里问需要避免什么误解，不是字面意义的向外看。",
    "sum up": "表示简洁概括要点，可说sum up the report。与逐句重复不同，应保留事件、来源和关键限定。",
    "going beyond the evidence": "指作出证据无法支持的进一步推断。without going beyond...要求复述时不把预测或评论说成事实。",
    "inaugural address": "指领导人在就职典礼上的正式演说。inaugural是就职的；address在这里是正式讲话，不是地址。常用in his inaugural address引出讲话内容，不代表其中承诺已实现。",
}


def line(speaker, english, chinese):
    return {"sp": speaker, "en": english, "zh": chinese}


def build_scene(number, topic):
    region, title_en, title_zh, term_en, term_zh, explanation_en, explanation_zh, caveat_en, caveat_zh, check_en, check_zh = topic
    source = SOURCES[region]
    scene_id = f"PA{number:02}"
    discussions = [
        ("先确定报道角度", "What are we focusing on in this report?", "这段报道主要关注什么？", f"The focus is {title_en.lower()}. We're using the 2025 background, not presenting this as breaking news.", f"重点是{title_zh}。我们使用2025年的背景，不把它当成突发新闻。", "So the event and the angle aren't quite the same thing?", "所以事件和报道角度不是完全相同的东西？", "Right. The event gives us context; the angle tells us what question we're examining.", "对。事件提供背景，角度说明我们正在研究什么问题。"),
        ("事实与官方说法", "What can we safely say about the background?", "关于背景，我们可以确切说什么？", source["contextEn"], source["contextZh"], "Does the official document prove that every stated goal was achieved?", "官方文件能证明每个提出的目标都实现了吗？", "No. It records the announcement or stated position. We'd need separate evidence for the results.", "不能。它记录公告或公开立场。结果需要另外的证据。"),
        ("听清关键术语", f"When a reporter says {term_en}, what should I understand?", f"记者说{term_en}时，我应该理解为什么？", explanation_en, explanation_zh, "Could you put that in context rather than just give me a dictionary translation?", "你能结合语境解释，而不只是给出词典翻译吗？", f"In this discussion of {title_en.lower()}, that distinction is what keeps the meaning precise.", f"在{title_zh}的讨论中，正是这个区别保证理解准确。"),
        ("不要漏掉限定条件", "What's the main qualification listeners should catch?", "听众应该听清的主要限定条件是什么？", caveat_en, caveat_zh, "So a confident headline doesn't remove that qualification?", "所以一个肯定的标题不能消除这个限定条件？", "Exactly. Listen for words such as may, could, and subject to. Don't turn a possibility into a certainty.", "没错。留意may、could和subject to等词，不要把可能性变成确定性。"),
        ("记者追问证据", "What would you check before drawing a conclusion?", "下结论之前你会核查什么？", check_en, check_zh, "Would one interview be enough?", "一次采访够吗？", "It could illustrate a person's experience, but it wouldn't establish the overall effect on its own.", "它可以说明一个人的经历，但不能单独证明整体影响。"),
        ("解释不是预测", f"How should a reporter explain {term_en} without overstating it?", f"记者如何解释{term_en}而不过度断言？", explanation_en, explanation_zh, "And what should the report avoid implying?", "报道应避免暗示什么？", caveat_en, caveat_zh),
        ("采访中的自然异议", "I see why the headline sounds clear. Aren't we making this too complicated?", "我理解为什么标题听起来清楚。我们是不是把事情弄得太复杂了？", f"I see your point, but here's the issue: {caveat_en[0].lower() + caveat_en[1:]}", f"我理解你的意思，但问题在于：{caveat_zh}", "Fair enough. What would help settle the question?", "有道理。什么能帮助厘清问题？", check_en, check_zh),
        ("区分来源与判断", "How do we tell the source's claim from the reporter's assessment?", "如何分清来源的说法和记者的评估？", f"Listen for attribution, then check the basis for the assessment. For this topic: {check_en}", f"先听来源标注，再核查评估依据。针对这个话题：{check_zh}", "So according to doesn't mean independently verified?", "所以according to并不意味着已独立核实？", "Correct. It identifies a source. The evidence still needs to support the claim.", "对。它标明来源。说法仍需证据支持。"),
        ("听力核查与纠错", f"Let me check I've got this right. How should I understand {term_en}?", f"让我确认是否听对了。我该如何理解{term_en}？", explanation_en, explanation_zh, "And what's the mistake to watch out for?", "需要避免什么误解？", caveat_en, caveat_zh),
        ("复述与下一步", "How would you sum up the report without going beyond the evidence?", "如何在不超出证据的前提下概括报道？", f"The topic is {title_en.lower()}. The key explanation is this: {explanation_en}", f"主题是{title_zh}。关键解释是：{explanation_zh}", "What remains to be checked?", "还有什么需要核实？", check_en, check_zh),
    ]
    dialogues = []
    highlights = [
        [("breaking news", "突发新闻"), ("context", "背景、语境")],
        [("stated position", "公开表明的立场"), ("separate evidence", "另外的证据")],
        [(term_en, term_zh), ("in context", "结合语境")],
        [("qualification", "限定条件"), ("possibility", "可能性"), ("certainty", "确定性")],
        [("drawing a conclusion", "下结论"), ("on its own", "单独、仅凭自身")],
        [("without overstating it", "不过度断言"), ("implying", "暗示")],
        [("I see your point", "我理解你的意思"), ("Fair enough", "有道理")],
        [("attribution", "来源标注"), ("independently verified", "已独立核实")],
        [("got this right", "理解正确"), ("watch out for", "留意、提防")],
        [("sum up", "概括"), ("going beyond the evidence", "超出证据")],
    ]
    if region == "us":
        highlights[1].append(("inaugural address", "就职演说；address在这里指演说，不是地址"))
    for part, (heading, question_en, question_zh, answer_en, answer_zh, follow_en, follow_zh, final_en, final_zh) in enumerate(discussions, 1):
        dialogues.append({"id": f"{scene_id}-{part:02}", "part": part, "title": heading,
                          "highlights": [{"en": english, "zh": chinese,
                                          "note": HIGHLIGHT_NOTES.get(english, explanation_zh + " 注意：" + caveat_zh)}
                                         for english, chinese in highlights[part - 1]],
                          "lines": [line("Host", question_en, question_zh), line("Reporter", answer_en, answer_zh),
                                    line("Host", follow_en, follow_zh), line("Reporter", final_en, final_zh)]})
    return {"id": scene_id, "trackId": "public-affairs", "region": region, "title": title_zh,
            "titleEn": title_en, "status": "text-draft", "backgroundDate": source["date"],
            "source": source, "scope": "Original thematic training, not a transcript or 50 distinct news events",
            "terms": [{"en": term_en, "zh": term_zh, "note": explanation_zh + " 注意：" + caveat_zh}], "dialogues": dialogues}


def main():
    media_path = ROOT / "sources" / "news-lessons.json"
    if media_path.exists():
        document = json.loads(media_path.read_text(encoding="utf-8"))
        ids = set()
        for scene in document["scenes"]:
            assert scene["source"]["url"].startswith("https://transcripts.cnn.com/")
            assert scene["source"]["transcriptReviewed"] and not scene["source"]["audioReviewed"]
            for dialogue in scene["dialogues"]:
                assert dialogue["id"] not in ids
                ids.add(dialogue["id"])
                assert all(turn["en"] and turn["zh"] for turn in dialogue["lines"])
                assert all(any(phrase["en"].lower() in turn["en"].lower() for turn in dialogue["lines"])
                           for phrase in dialogue.get("highlights", []))
        (ROOT / "data" / "news.js").write_text("window.NEWS = " + json.dumps(document, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
        print(f"PASS: {len(document['scenes'])} media-sourced scene(s), {len(ids)} study sections; transcript analysis only")
        return
    raise RuntimeError("Verified media lessons are required. Template drafts must not be published as news lessons.")


def build_archived_templates():
    assert len(TOPICS) == 50
    scenes = [build_scene(number, topic) for number, topic in enumerate(TOPICS, 1)]
    document = {"trackId": "public-affairs", "title": "听懂英语新闻", "created": "2026-10-12",
                "status": "text-draft", "videoVerified": False, "scenes": scenes}
    folder = ROOT / "sources" / "drafts"
    (folder / "public-affairs-scenes.json").write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text = ["# 听懂英语新闻：50个场景，500段短对话", "",
            "原创主题训练文本，每段4轮中英问答，共2000轮。无音频、无时间轴、未接入首页。", "",
            "所有背景均取自2025年来源；不是50条独立事件报道，也不是媒体原话。各场景围绕背景练习不同概念，假设性问题不代表事件已发生。",
            "结构采用可复用新闻提问框架，术语、解释、误解与核查方向按主题区分；属于第一轮草稿，尚需人工去重复、口语与新闻密度评审。",
            "真实YouTube视频尚未绑定；不得把文本数量视为真实新闻听力验收。", "",
            "分配：美国15场、日本10场、韩国10场、欧洲15场。", "", "## 场景索引", ""]
    for scene in scenes:
        text.append(f"- {scene['id']} · {scene['title']} ({scene['region']})")
    for scene in scenes:
        text.extend(["", f"## {scene['id']} · {scene['title']}", "", f"背景来源日期：{scene['backgroundDate']}。",
                     f"事实背景：{scene['source']['contextZh']}", f"来源：{scene['source']['url']}",
                     f"重点术语：**{scene['terms'][0]['en']}**（{scene['terms'][0]['zh']}）。", ""])
        for dialogue in scene["dialogues"]:
            text.extend([f"### {dialogue['id']} · {dialogue['title']}", ""])
            for turn in dialogue["lines"]:
                text.extend([f"**{turn['sp']}:** {turn['en']}", f"{turn['zh']}", ""])
    (folder / "public-affairs-scenes.md").write_text("\n".join(text) + "\n", encoding="utf-8")
    assert len({item["id"] for scene in scenes for item in scene["dialogues"]}) == 500
    assert all(len(scene["dialogues"]) == 10 for scene in scenes)
    assert all(len(item["lines"]) == 4 and all(turn["en"] and turn["zh"] for turn in item["lines"])
               for scene in scenes for item in scene["dialogues"])
    assert all(all(any(phrase["en"].lower() in turn["en"].lower() for turn in item["lines"])
                       for phrase in item["highlights"]) for scene in scenes for item in scene["dialogues"])
    print("PASS: 50 scenes, 500 dialogues, 2000 bilingual turns; no audio produced")


if __name__ == "__main__":
    main()