# 模式卡片 · 2024 MCM A · 队伍 2424371（Xi'an Jiaotong University）

> **身份验证链**：论文 PDF（队伍号 2424371，正文匿名 Team Control Number，题名 "Magic Sex Ratio: Exploring the Important Role of Lampreys in the Ecosystem"）→ 官方 `2024_A_Results.pdf` 验证（本站）：**Xi'an Jiaotong University / 顾问 Lei Chen / 2024 A Outstanding Winner + SIAM Award**。
> **页码纪律**：本卡页码 = PDF 页码 = 印刷页码（p.1 为 Summary Sheet，页眉 "Page 3 of 25" 与 PDF 第 3 页对应，全文共 25 页；References 止于 p.25）。
> **版权纪律**：PDF 存本地学习目录（不进公开仓库）；本页只放本站原创分析与 ≤25 词短引注。
> 论文经拆解代理逐页深读（25/25 页）+ 站内方法清单（[A_连续](../03_题型打法/A_连续.html)、[02_微分方程与动力学](../02_知识模块/02_微分方程与动力学.html)）交叉对照；同题对照卡：[06_卡片_2024A_Wuhan](06_卡片_2024A_Wuhan.html)（已上线，本卡 distinct 字段据此填写）。[A_连续](../03_题型打法/A_连续.html) 题型画像表经官方题面核实无误。

## 1. 模式卡片

```json
{
  "team": "2424371（Xi'an Jiaotong University，顾问 Lei Chen；2024 A Outstanding Winner + SIAM Award，官方 Results 册交叉验证；PDF 正文匿名，仅 Team Control Number）",
  "problem": "2024-A（Resource Availability and Sex Ratios：七鳃鳗 adaptive sex ratio 对种群与生态系统的影响；连续型——本篇把海洋池空间化，升维成反应-扩散-趋化 PDE）",
  "tiers": {
    "summary": {
      "背景问题": "最古老脊椎动物之一，既是美食又是寄生性入侵种；性别比随外部环境变化的能力对生态系统稳定至关重要（p.1, p.3）",
      "任务重述": "摘要按四问分段，每问一段方法+结论，其中三问带图指针：Q1 (result:Figure 8-11)、Q3 (result:Figure 17)、Q4 (result:Figure 19)（p.1）；§1.2 四问完整重述（p.3）",
      "方法主线": "两模型命名报出：Model I Population Growth Model Induced by Sex Ratio（最小二乘拟合幼体生长率-食物密度关系 + sex logistic 函数 + 改进 Logistic 与 Lotka-Volterra → 微分方程组，Finite Volume Method 解 PDE）；Model II 3-R Index Model of Ecosystem Stability（Resistance/Resilience/Recovery + Shannon Index）（p.1；加粗方法名词串贯穿摘要）",
      "关键结果数字": "摘要零数字——无任何百分数/数值结果，结论全部定性 + 图指针（p.1，与 Wuhan 卡 3 个百分数形成对照）；正文散落数字：拟合 R²=0.9804（p.8）、15×15 网格/Δt=1d（p.12）、种群 4000-5000 天稳定（p.14）、崩溃阈值 r_H∈(0.023,0.024)（p.22）",
      "结论建议": "四问各一条结论（§9, p.24）：①可变性别比通过反馈调节种群与生态系统（控自身增殖、稳宿主、抑浮游植物过剩）；②利=抗外部扰动强，弊=性别比调节有明显 time lag；③性别比对 Recovery 影响小、对 Resilience 影响大，雄性比例高→弹性大、抗性略降；④可变性别比对竞争性寄生虫与宿主的食物来源有利",
      "关键词": "Lampreys, Sex Ratio, PDE, Finite Volume Method, 3-R Index（p.1）"
    },
    "structure": [
      "Summary Sheet（p.1）",
      "Contents（p.2）",
      "1 Introduction：1.1 Background（Fig 1 实物照片）/ 1.2 Restatement（四问）/ 1.3 Our Work（Fig 2 总流程图）——无独立 Literature Review 小节（p.3-4）",
      "2 Assumptions and Justifications：5 条假设各带 justification，每条指文献编号（p.4-5）",
      "3 Notations：Table 1（8 个符号——仅覆盖河流池变量，海洋池符号缺）（p.5）",
      "4 Model I：4.1 Model Overview（三阶段生活史→建模路线, p.5-6）/ 4.2 Model Building（4.2.1 Migratory Sub-model p.7-8 / 4.2.2 Predisposing Factors and Effects of Sex Ratio p.8 / 4.2.3 River 模型 p.9 / 4.2.4 Ocean 模型 p.9-11）/ 4.3 Model Solution（FVM, p.12）/ 4.4 Results of Problem I（p.12-14）/ 4.5 Results of Problem II（4.5.1 Advantages p.14-15 / 4.5.2 Disadvantages: time lag p.16）",
      "5 Model II 3-R Index Model：5.1 Overview（p.16）/ 5.2 Model Building（5.2.1 指标选择 p.16-17 / 5.2.2 指标量化 p.17-18 / 5.2.3 内部系统变量 p.18-19 / 5.2.4 扰动因子 p.19）/ 5.3 Results of Problem III（p.19-20）",
      "6 Model Expansion：加寄生 A（与七鳃鳗竞争同一宿主）+ 鱼 B（宿主鱼的食物）→ 5 物种食物网；方程明示省略（p.20-22）",
      "7 Sensitivity Analysis：r_H 双侧扫描两张表（p.22-23）",
      "8 Strengths and Weaknesses（p.23）",
      "9 Conclusion（p.24）",
      "References（20 条，p.24-25）"
    ],
    "models": [
      {"name": "迁移子模型（Migratory Sub-model）", "type": "脉冲开关迁移通量（年度事件门控）", "assumptions": "两次迁徙：t1（3-4 月，5-7 龄成体上溯产卵 [8]）、t2（5-6 月，3-5 龄幼体变态下海 [9]）；上溯量对全海洋积分 N1=δ(t−t1)·m1·∬M2 dxdy（eq1）、下海量 N2=δ(t−t2)·m2·M1（eq2），雌雄各一；δ(t) 为 1-at-t0 脉冲开关（eq5, p.8）", "validation": "未报告迁移率 m1/m2 取值与触发实现细节（诚实登记）；生理一致性：产卵即死（假设4, p.5）→ 上溯成体不进河流生物量池、只作为出生源进入 eq8-9（p.8-9）", "pages": "eq1-5, p.7-8"},
      {"name": "sex logistic 函数", "type": "机理-经验桥（幼体生长率→雌性分化概率）", "assumptions": "性别分化由幼体生长率直接决定：慢生长（贫营养）偏雄、快生长（富营养）偏雌，field study 文献 [10] 支撑（p.8）；η(v)=1/(1+e^{−(αv+β)})，α、β 为生长率修正（eq6, p.8）", "validation": "文献定性一致（p.8）；α、β 取值未报（诚实登记）", "pages": "eq6, p.8"},
      {"name": "生长率-食物密度关系", "type": "行为关系拟合（最小二乘）", "assumptions": "幼体生长率主要取决于可食浮游植物密度 ρ [11]；函数形式 v=A·e^{μρ}+M（eq7, p.8）", "validation": "最小二乘拟合：A=−0.76, μ=−0.02, M=0.67，报 R²=0.9804（p.8）——全文唯一一处拟合优度报告。拆解者注：按参数符号 dv/dρ=+0.0152·e^{−0.02ρ}>0（v 随食物增），与正文 'gradually slows down with the increase of food concentration' 方向相悖（p.8）；数学结果与生物学逻辑（快生长偏雌, [10]）自洽，正文表述疑为笔误", "pages": "eq7, p.8"},
      {"name": "出生率桥（性别比→出生）", "type": "机理桥函数（交配制度→新生分性别）", "assumptions": "一雄多雌制、体外受精、雄性生物量通常占优 [12]→出生率只需按雌性数计；R_male=c·N1_female·(1−η)、R_female=c·N1_female·η（eq8-9, p.8）——新生性别由 η 即时刻生长率决定，性别比调节从此进入种群动力学", "validation": "无定量对账（诚实登记）", "pages": "eq8-9, p.8"},
      {"name": "河流 ODE 组", "type": "集总参数种群动力学（浮游植物+七鳃鳗雌雄）", "assumptions": "河内环境变化不显著 [7]→整段水体视为一个池（p.7，降维依据）；浮游植物 logistic + 七鳃鳗牧食 δ_P·(M1+F1)（eq10）；成体产后短命→不计其对河流池贡献；天敌强食物替代→只留捕食项 δ1 不建天敌动态（eq11-12）", "validation": "无解析稳定性分析（诚实登记）", "pages": "eq10-12, p.9"},
      {"name": "海洋 PDE 组（本篇核心）", "type": "反应-扩散-趋化方程组（宿主鱼 SI 型分舱 + 七鳃鳗扩散-趋化）", "assumptions": "宿主鱼按寄生状态分舱：未寄生 Hu、已寄生 Hi，寄生'传染'项 β·Hu(M2+F2)、寄生附加死亡 α、自然死亡 d（eq13-14）——借用传染病舱室结构 [13]；七鳃鳗：死亡 δ2 − 上溯脉冲 + 自由扩散 E∇²M2 + 趋化项 G(∂H/∂x+∂H/∂y)（'lampreys always move towards the place where there are more hosts', p.11）；下海个体以点源 (x0,y0) 进入（eq15-18）", "validation": "FVM 数值解（p.12）；无解析分析（诚实登记）", "pages": "eq13-18, p.9-11"},
      {"name": "3-R 指标体系", "type": "生态稳定性评估指标组（文献锚定）", "assumptions": "五个候选指标（Resistance/Resilience/Recovery/Persistence/Tolerance [18]）中取前三个：抗性=初始稳定、弹性=恢复速率、恢复=长期适应（p.17）；指标设计三原则先行：(a) 无量纲归一化且单调、(b) 有界、(c) 普适 [19]（p.17）；Resistance=1−2|S_R−S_0|/(S_R+|S_R−S_0|)（eq19-20）、Resilience=2|S_R−S_0|/(|S_R−S_0|+|S_R−S_Y|)−1（eq21）、Recovery=1−2|S_R−S_R′|/(S_R+|S_R−S_R′|)（eq22），三者均 ∈[−1,1]（p.18）", "validation": "Fig 15 在扰动曲线上图解每个量的含义（p.18）；Fig 17 剂量-响应曲线（p.20）", "pages": "eq19-22, p.17-18"},
      {"name": "Shannon 指数作为内部系统变量 S", "type": "评估桥（物种生物量→单一稳定性读数）", "assumptions": "Shannon 指数兼顾丰富度与均匀度、对小变化敏感（p.18-19）；S=−Σp_i·log(p_i)（eq23）；由 Model I 结论得 S=f(ρ) 接入 3-R 公式（p.19）", "validation": "Fig 16：Day=5115 外源类固醇扰动下 S 时序（p.19）", "pages": "eq23, p.19"},
      {"name": "扩展食物网（Q4，5 物种）", "type": "食物网扩展（加竞争者 A 与下行动链 B）", "assumptions": "寄生 A 与七鳃鳗竞争同一宿主、鱼 B 是宿主鱼的主要食物（p.20）；人为在 8000≤t≤9000 降低幼体雌性比例作扰动（p.21）", "validation": "定性结论：可变性别比对 A、B 有利（p.21-22）；方程明示省略 'For the sake of space, the specific formulas will not be listed here'（p.21）——可复现性缺口（诚实登记）", "pages": "p.20-22, Fig 18-19"}
    ],
    "figures": [
      {"id": "Fig 1", "page": "p.3", "claim": "开场实物照片：sea lamprey（来源标注 baijiahao.baidu.com）", "type": "照片", "self_evidence": "低——装饰性"},
      {"id": "Fig 2", "page": "p.4", "claim": "Our Work 总流程图：Model I（迁移子模型+性别比子模型+FVM）→Q1/Q2；Model II（3-R+Shannon）→Q3；Model Expansion→Q4；Sensitivity/Strengths 并列", "type": "流程图", "self_evidence": "高——一图完成两模型-四问映射"},
      {"id": "Fig 3", "page": "p.6", "claim": "生活史图：Year 0-7 逐龄 Larvae/Juveniles/Adults 三段 + 两次迁徙箭头 + Reproduction/Die 标注", "type": "时间轴示意图", "self_evidence": "高——年龄结构一眼可见，是迁移开关 eq1-2 的图形化"},
      {"id": "Fig 4", "page": "p.7", "claim": "球面四边形→平面矩形的抽象过程（地球仪+网格）", "type": "空间抽象示意", "self_evidence": "高——为'经纬度均分网格'辩护"},
      {"id": "Fig 5", "page": "p.10", "claim": "生物关系图：幼体捕食浮游植物、成体寄生于宿主鱼", "type": "生态关系示意", "self_evidence": "中-高"},
      {"id": "Fig 6", "page": "p.11", "claim": "全方程组项级流程图：River 池（P/M1/F1）与 Ocean 池（M2/F2/Hu/Hi）之间每个通量项按 eq10-18 逐一标注", "type": "项级通量图", "self_evidence": "很高——方程组的图形对账表，评委可逐项核对"},
      {"id": "Fig 7", "page": "p.12", "claim": "宿主鱼空间分布热图三时刻：t=360/3600/18000 天（Initial/Adjustment/Stabilization Period）——展示 FVM 解的空间收敛过程", "type": "空间热图序列", "self_evidence": "高；图题笔误 'FAM'（应为 FVM）"},
      {"id": "Fig 8", "page": "p.13", "claim": "p=0.56 可变性别比（左：种群降后升、4000-5000 天稳定）vs 不可变（右：七鳃鳗灭绝、宿主鱼走高）", "type": "四线时序双面板", "self_evidence": "中——须四图并排读"},
      {"id": "Fig 9", "page": "p.13", "claim": "p=0.67 同式对照", "type": "四线时序双面板", "self_evidence": "中"},
      {"id": "Fig 10", "page": "p.13", "claim": "p=0.78 同式对照", "type": "四线时序双面板", "self_evidence": "中"},
      {"id": "Fig 11", "page": "p.13", "claim": "p=0.82 同式对照——四组初值下'可变存活/不可变灭绝'结论重复出现", "type": "四线时序双面板", "self_evidence": "中——多初值扫描的说服力靠重复"},
      {"id": "Fig 12", "page": "p.14", "claim": "Food Crisis：t=7000 时 P→0.75P，横轴标注 Adjustment/Stabilization/Recovery Period + 扰动竖线 + Reduction 区间标注", "type": "分期标注时序", "self_evidence": "高——实验时间线自带图上"},
      {"id": "Fig 13", "page": "p.15", "claim": "Killing Crisis：t=6000 起 δ1,δ2→2δ1,2δ2，种群降至新平衡不灭绝", "type": "分期标注时序", "self_evidence": "高"},
      {"id": "Fig 14", "page": "p.15", "claim": "Reproduction Crisis：t=5000 起 c→0.5c，同样维持低量延续", "type": "分期标注时序", "self_evidence": "高"},
      {"id": "Fig 15", "page": "p.18", "claim": "3-R 指标含义图：外源类固醇扰动曲线上标注 S_R/S_0/S_Y/t_p/t_0/Rst/Rsl 各量位置", "type": "公式-曲线对照示意", "self_evidence": "很高——指标定义的图形化教科书"},
      {"id": "Fig 16", "page": "p.19", "claim": "Day=5115 扰动下各物种生物量 + Shannon Index 时序", "type": "双面板时序", "self_evidence": "中-高"},
      {"id": "Fig 17", "page": "p.20", "claim": "3-R Index 对扰动幅度 Δp 的剂量-响应：Rc 恒≈1 不敏感、Rsl 在 Δp≈0.1 处从 0.1 跳升至 ~0.75、Rst 微降", "type": "三线剂量-响应散点", "self_evidence": "很高——全文最关键一图，单图回答 Q3"},
      {"id": "Fig 18", "page": "p.21", "claim": "5 物种食物网：River（幼体-浮游植物-生产者+外源营养）/ Ocean（寄生 A、七鳃鳗、宿主鱼、海鱼）", "type": "食物网图", "self_evidence": "高"},
      {"id": "Fig 19", "page": "p.21", "claim": "5 物种生物量时序 + 8000-9000 性别比突变扰动——Q4 证据图", "type": "分期标注时序", "self_evidence": "中——曲线密集需图例细读"},
      {"id": "Fig 20", "page": "p.23", "claim": "r_H=0.02 时生态系统崩溃过程", "type": "时序", "self_evidence": "中"},
      {"id": "Fig 21", "page": "p.23", "claim": "r_H=0.1 时各物种时序（宿主鱼逼近 K_H）——正文误引作 'Figure (7)'（p.22）", "type": "时序", "self_evidence": "中"}
    ],
    "checks": [
      "开关式对照 × 多初值扫描（Q1 主检验）：同一模型开/关性别比调节，4 个初始雄性比 p=0.56/0.67/0.78/0.82（p.12）共 8 组；初值刻意取非平稳态（'the given initial values do not necessarily make the community in a stable state', p.12）；结论重复：可变组降后升并稳定、不可变组灭绝（Fig 8-11, p.13；解读 p.14）",
      "三危机参数扰动（Q2）：饥荒 P→0.75P@t=7000（Fig 12, p.14）、猎杀 δ1,δ2→2δ1,2δ2@t=6000（Fig 13, p.15）、繁殖 c→0.5c@t=5000（Fig 14, p.15）；读出=种群是否灭绝/恢复快慢；并从模型结构导出弊：time lag（§4.5.2, p.16）",
      "扰动-响应剂量曲线（Q3 主检验）：外源类固醇@Day=5115（与假设3 'steroids 只改性别比不改生死率' 咬合, p.4, p.19）；Shannon 指数作系统变量（Fig 16, p.19）；扰动幅度 Δp∈{0.02,...,0.2} 扫描得 3-R 剂量-响应（Fig 17, p.20）——非对称结论：Rc 不敏感、Rsl 敏感（雄性比例高→弹性大）、Rst 微降",
      "敏感度双侧扫描（§7, p.22-23）：r_H 上升 8 档（0.03+0.01k）报 Shannon 表（Table 2: 1.0344→0.8998 单调降）；下降 6 档（0.02+0.001k）报崩溃时间表（Table 3: 488/1736/3158/6225/>24000/>24000 天）——发现阈值 r_H∈(0.023,0.024) 崩溃时间跳变；模型内 r_H=0.026（p.22）；另以 Fig 20/21 展示两端情形",
      "缺项（诚实登记）：无收敛性/网格加密论证（15×15、Δx=Δy=0.5°、Δt=1d 直接给定, p.12）；无参数值汇总表（m1/m2/δ1/δ2/δ_P/r_P/K_P/K_H/d/α/β/D/E/G/c 等十余个参数值全篇未报，§4.3 只说 'review a large number of literature and online resources [13]–[16]', p.12）；无实测数据对账（全文无模型轨迹 vs 真实种群对照）；无平衡点/线性化稳定性分析（'稳定性'走实验扰动+文献指标路线）；Q4 方程明示省略（p.21）；α、β（sex logistic 修正项）取值未报（p.8）"
    ],
    "wordsmith": [
      {"quote": "we develop two main models, the Population Growth Model Induced by Sex Ratio and the 3-R Index Model of Ecosystem Stability", "page": "p.1", "note": "摘要模型清单句：命名式报模型，与 Wuhan 同款动作——两篇 O 摘要都用'两模型'命名框架"},
      {"quote": "but has a serious 'time lag effect'", "page": "p.1", "note": "摘要结论句：把模型推出的机理发现加上引号命名——一个可引用的标签比一段描述更易被评委记住"},
      {"quote": "Therefore define the sex logistic function", "page": "p.8", "note": "自造函数命名动作句：给桥函数起名（sex logistic）使其成为论文资产，后文可反复引用"},
      {"quote": "lampreys are likely to become extinct due to the time lag effect and the failure to adjust the population size in a timely manner", "page": "p.16", "note": "弊的机理句式：不利结论不是罗列风险，而是指出模型结构中的延迟反馈链条（幼体先成熟才能繁殖）"},
      {"quote": "Resistance reflects the initial stability of an ecosystem, resilience reflects the rapid recovery ability, and recovery reflects the long-term stability", "page": "p.17", "note": "指标三角化句：三个指标各管一段稳定性，一句话论证'为什么三个都要'"},
      {"quote": "It is worth noting that all three of the above equations take values between -1 and 1.", "page": "p.18", "note": "指标有界性声明句：主动宣告指标有界，兑现 5.2.2 的设计原则(b)"},
      {"quote": "The partial differential equation model is a natural description of the multivariate system", "page": "p.23", "note": "模型选型辩护句：strengths 里为 PDE 路线辩护——'空间多元系统的自然描述'，正是 SIAM 奖数学味的自我陈述"}
    ]
  },
  "distinct": "把问题空间化的 PDE 路线（已与同题 Wuhan 卡对照后填写）：海洋池写成反应-扩散-趋化方程组——宿主鱼按寄生状态分 Hu/Hi 舱室（传染病 SI 结构）、七鳃鳗带自由扩散 E∇² 与向宿主聚集的趋化项 G∇H（eq13-18, p.9-11），地理抽象用 Haversine 公式落地（p.7），15×15 经纬网格 FVM 求解（p.12）；稳定性评估用生态学文献现成 3-R 指标体系（[18][19]）对扰动幅度 Δp 做剂量-响应曲线（Fig 17, p.20）。同题 Wuhan 卡（2400996）为纯时间迭代+年龄舱位+自造 S 指标单点对照，两卡无重叠——此 distinct 在两卡对照下成立。"
}
```

## 2. 同题 O-O 对比（vs Wuhan 2400996，INFORMS 奖）

1. **空间维度之争：PDE-趋化 vs 纯时间迭代——SIAM 奖的数学味落点**。XJTU 把海洋池升维成反应-扩散-趋化 PDE（15×15 经纬网格、D 扩散、G∇H 宿主趋化项, eq13-18 p.9-11；FVM, p.12；Haversine 地理抽象, p.7），且降维有依据：河流环境均匀 [7]→集总 ODE（p.7）——"哪一池需要空间分辨率"是逐池决策。Wuhan 全程时间维度（年度差分迭代+年龄舱位）。SIAM（应用数学学会）奖落在 PDE 侧，说明评委对"把生物场景翻译成有结构的数学物理问题"（扩散/趋化/传染病舱室）给予最高认可；代价是 XJTU 参数报账几乎为零。
2. **稳定性问答路线：文献锚定指标体系+剂量-响应曲线 vs 自造单指标+统一优化率**。Wuhan 自造 S（扰动后均方差, eq19）给单点数 R=73.3%；XJTU 用生态学现成 3-R 指标（Orwin & Wardle 2004 [19]、Van Meerbeek 2021 [18], p.17-18），先声明指标设计三原则（无量纲/有界/普适, p.17），再对扰动幅度 Δp 扫描出剂量-响应曲线（Fig 17, p.20），得到"哪个维度敏感/不敏感"的非对称结论（Rc 不敏感、Rsl 敏感、Rst 微降）。**评估给曲线和排序 > 给一个数**——这是本篇"数学味"的第二落点。
3. **摘要策略完全相反：零数字+图指针 vs 百分数密度——数字密度不是 O 的必要条件**。XJTU 摘要无任何数值结果，取而代之每问定性结论+`(result:Figure X)` 指针（p.1），但有一个带引号的可命名发现 "time lag effect"（p.1）；Wuhan 摘要 3 个百分数且全部可复算。两卡对照表明：评委奖励的是**结论的具体性与可追溯性**（可命名机理发现/可复算指标二选一皆可），"摘要塞数"不是硬门槛。
4. **Q1 对照设计：多初值扫描 vs 单对开关对照**。Wuhan 开/关机制单对对照 1000 年+恢复时间 T1-T4 定量；XJTU 开/关 × 4 个初始雄性比（0.56/0.67/0.78/0.82）八组扫描（p.12-13），且刻意用非平稳初值（p.12）——用"结论在多个初值下重复出现"替代单点对照，鲁棒性论证更宽。但 Wuhan 的统一量化指标 R（eq21）把四问结果串成可复算数字链，XJTU 没有 equivalent——两篇各取一条护栏：一条"指标贯穿"，一条"初值扫描"。
5. **报账纪律反转：Wuhan 参数表齐备 vs XJTU 参数无账仍拿 SIAM**。Wuhan 有 Table 3 十参数+初值+扰动时间线（p.15），缺收敛检验；XJTU 连参数表都没有（十几个参数值未报, p.12）、无收敛论证、Q4 方程省略（p.21）——可攻击面比 Wuhan 更多却获 SIAM。数据点说明：**机理-数学结构的深度可以补偿报账缺口**，但这是高风险路线（换一批评委可能翻车），备赛不应模仿缺口，应学"深度+补齐报账"的组合。

## 3. 可复用的打法提炼（连续题特有动作，8 条）

1. **降维要有依据，逐池决定维度**：河流因"环境变化不显著 [7]"整体化为 ODE（p.7），海洋因"生物量是经纬度的函数"升为 PDE（p.10）——空间化不是全有全无，先问"环境/过程是否均匀"，均匀池降维、异质池升维。对照 A_连续骨架：这一步是"机理方程"之前的选型动作，两篇 2024 A O 卡在此分岔。
2. **借成熟数学结构写生态关系**：寄生直接套传染病 SI 舱室（Hu/Hi + β·Hu(M2+F2) 传染项 + 附加死亡 α, eq13-14, p.10）——方程立刻"有出处、有形状"；"七鳃鳗向宿主聚集"译成趋化项 G∇H（eq15/17, p.11）。机理翻译的动作不只是"文献说了什么"，还有"哪个数学结构天生长这个样"。
3. **行为关系三件套：文献数据→函数形式→最小二乘+R²**：幼体生长率-食物密度关系 v=Ae^{μρ}+M（eq7, p.8），最小二乘报 A=−0.76/μ=−0.02/M=0.67 + R²=0.9804（p.8）——行为参数不是拍脑袋，是"数据拟合+优度报告"；这是全文唯一一处拟合优度，值得复制到每个 fitted 环节。警示：引用文献数据要核对方向（本篇正文 'slows down' 与参数符号推算相悖, p.8）。
4. **指标设计三原则先行，公式配曲线图解**：无量纲归一化+单调、有界、普适（p.17, [19]）先声明再推导 3-R（eq19-22, p.17-18），并画 Fig 15 在扰动曲线上标注每个量的位置（p.18）——"先原则、后公式、再图解"三步曲，图解让评委 10 秒读懂指标；有界性主动宣告（'take values between -1 and 1', p.18）。
5. **评估做剂量-响应，不止给一个数**：扰动幅度 Δp 作自变量、3-R 指标作因变量（Fig 17, p.20）——得到"敏感/不敏感维度排序"，比单点对照信息量大一个量级；扰动源选外源类固醇与假设3（steroids 只改性别比）咬合（p.4, p.19），假设-实验闭环。
6. **敏感度用"崩溃时间"作读出，找相变式阈值**：r_H 下降扫描报生态系统崩溃时间 488→>24000 天（Table 3, p.22），发现 r_H∈(0.023,0.024) 之间崩溃时间跳变——敏感度分析的最高产出不是"趋势不变"，是**阈值定位**（模型内 r_H=0.026 恰在阈值之上，p.22，暗示系统贴近临界，论文未点破）。
7. **"弊"要从模型结构里长出来**：题面问 advantages and disadvantages，XJTU 的弊（time lag）由模型年龄结构推出——性别比只能作用于当前幼体，幼体需先成熟才能繁殖→调节必然滞后（§4.5.2, p.16）；并顺势给出适用边界（剧烈长期变化下可能灭绝, p.16）。机理推论的弊比罗列的风险可信一个量级，且能反哺摘要（'time lag effect', p.1）。
8. **分期标注时序图**：横轴标注 Adjustment/Stabilization/Crisis/Recovery Period + 扰动时刻竖线（Fig 12/13/14/19, p.14-15, 21）——一张图同时交代实验时间线、扰动位置与各阶段状态；另配 Fig 6 项级通量图（p.11）把方程组逐项画成流程，评委可对账。

### 瑕疵清单（O 论文也有，反着学）

- **参数无账**：m1/m2/δ1/δ2/δ_P/r_P/K_P/K_H/d/α/β/D/E/G/c 十余个参数值全篇未报，§4.3 只有一句文献来源（p.12）；Notation 表仅 8 符号、未覆盖海洋池（p.5）
- **无收敛性/网格充分性论证**：15×15、Δx=Δy=0.5°、Δt=1d 直接给定（p.12），无加密对照（02 模块 §4.1 死法）
- **无实测对账**：全文无模型轨迹 vs 真实种群数据对照图
- **符号复用/不一致**：δ 四种含义（脉冲开关 eq5 / δ_P 捕食 / δ1、δ2 死亡, p.8-11）；Notation 表 B_male 与正文 R_male 脱节（p.5 vs p.8）；p.14 'From the comparison of (8)/(11)' 图号公式号混用
- **文字-公式方向张力**：p.8 正文称生长率随食物浓度增大而减慢，按 eq7 参数推算 dv/dρ>0（随食物增）——数学与生物学方向自洽，正文疑笔误
- **笔误群**：Fig 7 图题 'FAM'（应为 FVM, p.12）；§4.2/§5.2 标题 'Buliding'（p.6, 16）；p.22 'Figure (7)' 应为 Fig 21
- **Q4 方程省略**：'For the sake of space'（p.21）——扩展模型不可复现；对比 Wuhan 扩展全量报方程（Wuhan 卡 p.17-18）
- **时间尺度细节缺**：PDE 以天为步长、生命周期以年计，δ(t−t1) 年度触发实现未说明（p.7-8）；生物量曲线锯齿（年迁徙脉冲）正文未解释（p.13）

### 升档差值骨架对照（A_连续打法的实测）

机理方程 ✓（每项有文献锚）→ 无量纲化 ✗（方程未无量纲化，仅 3-R 指标归一化）→ 数值解 ✓（FVM）→ 收敛检验 ✗ → 稳定性：实验型 ✓（扰动+3-R）/ 解析型 ✗（无线性化）→ 敏感度 ✓✓（双侧扫描+阈值）→ 优化 ✗（题面未要求）。与 Wuhan 卡同构：**O 档检验靠"选对路线"而非"全做"**——两篇 O 都缺收敛检验，都用机理深度+对照实验补位；XJTU 额外示范了"敏感度做出阈值"这条高阶动作。

## 4. 自查（代理产出，待站长复核）

- 页码逐条核过（PDF 25 页 = 印刷页码，25/25 页逐页图像深读；eq1-23 / Fig 1-21 / Table 1-3 逐一登记）
- 无臆测：缺项与瑕疵诚实登记；v-ρ 方向张力为拆解者按参数符号推算、标注为疑点非定论；摘要零数字、Q4 方程省略均为逐字核对的事实登记；Fig 8-11 具体数值从渲染图读出、只作定性描述
- distinct 已与同题 Wuhan 卡（06_卡片_2024A_Wuhan）对照后填写；引注均 ≤25 词；SIAM Award 身份以派单提供的官方 Results 册验证为准（PDF 本身匿名）
