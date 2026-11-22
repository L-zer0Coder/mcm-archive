# 模式卡片 · 2023 MCM B · 队伍 2300136（Tsinghua University，Outstanding Winner）

> **身份验证链**：论文 PDF 页眉自印 "Team # 2300136"（每页）+ Summary Sheet 印队伍号 2300136（p.1）；信件落款 "MCM #2300136, 2023.2.20"（p.3，符合 2023 年 2 月赛程）→ 官方 Results 册交叉验证（本站）（2023_B_Results.pdf p.3-4）：**Tsinghua University / 顾问 Heng Liang / 2023 B 题 Outstanding Winner**，2026-11-22 核。论文正文匿名（无作者名），身份全部来自 Results 册。
> **页码纪律**：本 PDF 页眉自印 "Page N of 25"，印刷页码与 PDF 页码一致；卡内页码即 PDF 页码 p.1–25。代理逐页深读（25/25 页）。
> **版权纪律**：PDF 存本地学习目录（不进公开仓库）；本卡只放本站原创分析与 ≤25 词短引注。
> **对照基线**：同题 F 档卡 [04_卡片_2023B_Fuzhou](04_卡片_2023B_Fuzhou.html)（2316192，Finalist，下称 "F 卡"），其 F 档特征 6 条与升档差值候选 5 条为本卡 §2/§3 的对照基线。站内方法页交叉对照：[E_可持续](../03_题型打法/E_可持续.md)、[03_统计与机器学习](../02_知识模块/03_统计与机器学习.md)、[05_评价与决策](../02_知识模块/05_评价与决策.md)。本卡与 F 卡构成全站第一个**同题同年 O-vs-F 升档差值对**。

## 1. 模式卡片

```json
{
  "team": "2300136（Tsinghua University，顾问 Heng Liang；2023 B Outstanding Winner，官方 Results 册 p.3-4 交叉验证；PDF 匿名，页眉自证队伍号）",
  "problem": "2023-B（Reimagining Maasai Mara：马赛马拉区内区外的分区政策、政策排序方法与长期趋势确定性）",
  "tiers": {
    "summary": {
      "背景问题": "从 poachers 到 conservationists：把社区利益纳入保护目标，求每个土地类型的最优政策与长期结果（p.1）",
      "任务重述": "对应题面四交付：分区政策建议 / 排序比较方法论 / 长期趋势+确定性+可迁移性 / 两页非技术报告——正文以六步计划逐条对应（p.6 六条 bullet；restatement p.5）",
      "方法主线": "四 section 网络评价模型（Score1-4 各自归一化 0-1）+ AHP 分土地类型定权 + 9 项政策每区 8 种组合×3 区=24 情景 MATLAB 仿真 2022-2041 + 回归趋势外推加正态随机残差（p.1, p.8, p.16, p.24）",
      "关键结果数字": "三区各一名最优：WPZ=①②③、HSZ=④（多数年份）、LGZ=⑦⑧⑨；摘要页数字与 F 队同为工作量型（四 section/三类土地/三政策/24 情景/20 年），结果量值集中在前置非技术信件 p.2-3（50%→2%→5%→30%→0.5%→5%→0.5%→10%→8%→0.5%→0.7%→USD$310 共 12 处）",
      "结论建议": "敏感度显示模型稳定鲁棒（p.1）；CC 校正系数验证可迁移性（p.1 'versatile use'→p.22 定量化）；反直觉发现主动进摘要与信件（①单独施行负面 p.18→p.1；⑥corridor 有害 p.19→p.2）",
      "关键词": "Wildlife conservation; Community-based management; Net-work based modelling（p.1；'net-work' 拼写贯穿全文）"
    },
    "structure": [
      "Summary Sheet（p.1）",
      "Report to the Kenyan Tourism and Wildlife Committee：非技术报告前置为两页信件，12 处结果数字（p.2-3；题面交付物）",
      "Content（p.4）",
      "I. Introduction：Background / Literary review（指出先前研究 survey-based 的缺口）/ Restatement（聚焦财务利益、定义游客）+ 六步计划（p.5-6）",
      "II. Foundations：2.1 Assumptions（6 条主假设逐条 justification，p.6-7）/ 2.2 Nomenclature（Table 1，26 符号，p.7）",
      "III. Model Design：3.1 网络模型（3.1.1-3.1.4 每 section 固定三段式：Modelling ideas→Supplementary assumptions→Calculations，p.8-15；3.1.5 AHP+final objective，p.15-16）/ 3.2 Policy scenarios（Table 2 九政策量化效果，p.16-17）",
      "IV. Results and Discussion：4.1 WPZ / 4.2 HSZ / 4.3 LGZ——每区一张 8 情景曲线图（含 Non 基线）+ 一张 2022/2032/2042 三时点排序表（p.18-20）",
      "V. Sensitivity Analysis：指数系数 α 扫描，六面板 3D 图（p.21）",
      "VI. Testing the Model：correcting coefficient 可迁移性检验 + CC 二次敏感度（p.22）",
      "VII. Strengths and Weaknesses：5 条 Strengths / 3 条 Weaknesses（p.23）",
      "VIII. Conclusions（p.24）",
      "IX. References：22 条，3 条带 URL（p.25）"
    ],
    "models": [
      {"name": "Score1 野生动物保护 section", "type": "时间序列拟合+多样性指数+归一化", "assumptions": "哺乳类可指示全部野生动物（航测数据可得性，p.8）；种群与生物多样性等权（1/2,1/4,1/4 声明式，p.10）", "validation": "指数拟合 y=10^7 e^{-0.051(x+71)}，R²=0.5163 报值但偏低未讨论（Fig2, p.9）；数据源 Ottichilo[13]/Lamprey[11]/KWS 普查[14]（p.9, p.25）", "pages": "p.8-10"},
      {"name": "Score2 自然资源 section", "type": "ODE（Verhulst 草地）+ 水压力分级", "assumptions": "野生草食动物摄食量=牲畜 2 倍（Stelfox[16] 生物量：牛 180/羊 23/角马 123/斑马 200 kg，p.10）；草地 Logistic 生长且摄食率与草量线性相关（p.10）", "validation": "参数全部带出处：dκ/dt=4gbκ(1−bκ)−srκ，g=41.9 kgDM/ha/day、b=1/4000 ha/kgDM、r=0.47% ha/animal/day 引 [17]（p.10）；水压力四级阈值引 Vörösmarty[19]，月度热图 Fig4 为实数据（p.12）；Score_water 权重 0.6/0.3/0.1/0 无来源说明（读不出）", "pages": "p.10-12"},
      {"name": "Score3 本地财务 section", "type": "收入分解+社会折现+sigmoid", "assumptions": "汇率 1 USD=100 KSh 恒定（用 2012-2022 实证除 COVID 年，p.12-13）；2% 社会折现率引 200 专家共识 [20]（p.13）", "validation": "R_total 四收入两成本逐项落地：罚款 100.53 USD/人/年、捕食损失 247.74 USD 引 [10]，10% 年出售率（p.14）；Q=15000 USD 'derived from normalization'（p.14）；Fig5 双面板拟合 R²=0.6196/0.8031 报值（p.13）", "pages": "p.12-14"},
      {"name": "Score4 旅游冲突 section", "type": "物种相遇概率（PIE）+冲击因子向量", "assumptions": "有害交互与游客/动物种群正相关（p.14）", "validation": "PIE 模型改自 Berger & Cunningham [22]：p≈2TN/(T+N)²（p.14）；冲击因子 λ/σ 归一化后为常数参数（p.15）——β/γ 分量数值未列出（读不出）", "pages": "p.14-15"},
      {"name": "AHP 分区赋权+final objective", "type": "综合评价赋权", "assumptions": "三土地类型各建一个 4×4 比较矩阵，矩阵全数印出（p.15-16）", "validation": "CR=0.0612/0.0223/0.0301 三值全报，RI=0.90(n=4)（p.16）——对照 05 模块 §1.4，'做了且报数'；权重结果图 Fig7 带百分比（Wildlife 51/25/6/18, Human 14/10/35/41, Livestock 16/29/12/44）（p.16）", "pages": "p.15-16"},
      {"name": "政策情景机制", "type": "参数改写式情景仿真", "assumptions": "政策效果=对模型参数的百分比改写（Table 2 九政策逐条量化：50%/2%/5%/30%/0.3%/20%/40%/10%/8%/0.7% 等，p.17）", "validation": "24 次仿真（8 情景×3 区）+ 每区 Non 基线对照（Fig8-10, p.18-20）+ 三时点排序表 Tables 3/4/5（p.18-20）；p.18 自认 ① 单独施行结论 'extremely dependent upon our predetermined parameter'", "pages": "p.16-20"},
      {"name": "长期趋势机制", "type": "回归外推+随机残差", "assumptions": "野生动物指数衰减、牲畜/本地人/游客线性趋势延续（03 模块 §1.5 '外推要声明假设趋势延续'——本文以假设 4 与随机残差声明，p.6-7, p.11, p.13）", "validation": "牲畜拟合 y=2000x+303004.9264+ξ，ξ~N(0, 0.39879²)（Fig3, p.11）——残差记法与图轴 thousand 单位的关系读不出；随机残差作为卖点进摘要与 Strength 5（p.1, p.23）", "pages": "p.9-13"},
      {"name": "敏感度机制", "type": "系数扫描", "assumptions": "把拟合指数 B 改写为 (lnα−B) 即得扰动族 y=Ae^{(lnα−B)t}（p.21）", "validation": "α 细粒度扫描（Fig11 轴标约 0.3%–3.0%，读自图轴）六面板分区报告：对牲畜变化更敏感、HSZ 最敏感（p.21）——结论定性，无数值区间", "pages": "p.21"},
      {"name": "可迁移机制（CC 校正系数）", "type": "参数缩放迁移检验", "assumptions": "新保护区参数=原 Mara 参数×(1+CC)（p.22）", "validation": "以政策 ③ 演示变换式；CC∈[−3.6%,−90%] 二次敏感度，报 final score 稳定区间 0.5-0.575（Fig12, p.22）——题面 'applied to other wildlife management areas' 的定量交付", "pages": "p.22"},
      {"name": "网络耦合结构（结构性注记）", "type": "共享变量耦合", "assumptions": "四 section 通过共享变量联动（Fig1：wildlife↔resources、economic incentive、tourism income/illegal affairs、grazing stress，p.8）", "validation": "实为'政策参数改写→共享输入变量→四分数'的单向传播+草地 ODE 对 N/M 的局部响应（p.9-11）；非全反馈动力学系统——论文自称 scoring network，如实登记结构", "pages": "p.8-11"}
    ],
    "figures": [
      {"id": "Fig 1", "page": "p.8", "claim": "四 section 网络评价模型流程图：每个 section 的分数构成与相互作用的箭头（survival/threaten/incentive/illegal affairs/grazing stress）", "type": "概念流程图", "self_evidence": "中-高（信息密度高于常规流程图，图内自带四个 Score 的公式骨架）"},
      {"id": "Fig 2", "page": "p.9", "claim": "野生种群指数拟合：散点+拟合曲线，方程与 R²=0.5163 印在图内", "type": "数据回归图", "self_evidence": "高"},
      {"id": "Fig 3", "page": "p.11", "claim": "牲畜种群线性拟合+随机残差带：方程、残差分布印在图内", "type": "数据回归图", "self_evidence": "高"},
      {"id": "Fig 4", "page": "p.12", "claim": "马赛马拉 sub-basin 各月水压力等级热图（4 种口径 a-d）——Model 的实数据中间产物", "type": "数据热图", "self_evidence": "中-高（图例清晰但轴标签小）"},
      {"id": "Fig 5", "page": "p.13", "claim": "本地人口与游客人口双面板线性拟合，R² 报值", "type": "数据回归图", "self_evidence": "高"},
      {"id": "Fig 6", "page": "p.15", "claim": "三土地类型实地图：WPZ 在 MMNR 内部，HSZ/LGZ 在周边 conservancy（Mara Triangle、Olare Orok 等实名标注）——直接回应题面 'within and outside the current boundaries'", "type": "数据地图", "self_evidence": "高"},
      {"id": "Fig 7", "page": "p.16", "claim": "三区×四 section 权重堆叠条形图（带百分比标签）：AHP 的结果可视化", "type": "结果图", "self_evidence": "高"},
      {"id": "Fig 8", "page": "p.18", "claim": "WPZ 八情景 final score 曲线（含 Non 基线）：最优=①②③，① 单独施行最差的反直觉可见", "type": "结果图", "self_evidence": "中-高（8 条线需配 Table 3）"},
      {"id": "Fig 9", "page": "p.19", "claim": "HSZ 八情景曲线：有/无 corridor 两组分层清晰", "type": "结果图", "self_evidence": "中-高"},
      {"id": "Fig 10", "page": "p.20", "claim": "LGZ 八情景曲线：全情景优于 Non 基线", "type": "结果图", "self_evidence": "中-高"},
      {"id": "Fig 11", "page": "p.21", "claim": "六面板 3D 柱状敏感度（a-c 牲畜系数×三区，d-f 野生动物系数×三区）", "type": "结果图", "self_evidence": "低-中（3D 柱状+轴标签过小，数值难读）"},
      {"id": "Fig 12", "page": "p.22", "claim": "CC 校正系数敏感度 3D 柱状图：final score 在 0.5-0.575 稳定", "type": "结果图", "self_evidence": "低-中（同上）"}
    ],
    "checks": [
      "AHP 一致性检验：三个比较矩阵全印出，CR=0.0612/0.0223/0.0301 全报值，RI=0.90(n=4)（p.16）——对照 05 模块 §1.4：F 卡同位置只有 'the final CR < 0.1'（F p.14）",
      "拟合优度报数：R²=0.5163（Fig2, p.9）、R²=0.6196/0.8031（Fig5, p.13）——R²=0.5163 偏低未讨论（诚实登记）",
      "敏感度：指数系数 α 扫描（Fig11 六面板，p.21），分区结论（对牲畜更敏感；HSZ 最敏感）——定性结论无数值区间",
      "可迁移性检验：CC 校正系数 + CC∈[−3.6%,−90%] 二次敏感度，报 final score 0.5-0.575 稳定（p.22）——题面 'applied to other wildlife management areas' 的直接交付",
      "基线对照：Non（无政策）情景进每张结果图（Fig8-10, p.18-20），并推出'所有情景优于基线→政策选择有效'（p.20）",
      "时点排序稳定性：每区 2022/2032/2042 三时点排序表（Tables 3/4/5, p.18-20）；HSZ 冠军随时点变化如实呈现（④⑤→④，p.19+摘要 'best policy for most years' p.1）",
      "随机残差：牲畜/人口外推加正态随机残差（p.11, p.13），摘要与 Strength 5 呼应（p.1, p.23）",
      "反直觉结果机制核查：① hunting quotas 单独施行长期负面+机制解释+参数依赖自认（p.18）；⑥ wildlife corridor 有害+三重机制（资源竞争/偷猎/PIE 上升，p.19）",
      "缺项（诚实登记）：AHP 权重 ±20% 排名翻转敏感度未做（05 模块 §1.5 纪律——两篇皆缺，O 用回归系数与 CC 敏感度替代）；Table 2 政策效果百分比为设定值而非文献估计（p.17，p.18 自认参数依赖）；残差 ξ~N(0, 0.39879²) 与图轴 thousand 单位关系读不出（p.11）；Fig11/12 3D 图轴标签过小（p.21-22，与 F 卡 Fig9 同病）；Score_water 权重 0.6/0.3/0.1/0 无来源（p.12）；牲畜损失 310 USD（信件 p.3 'locals report'）与 247.74 USD（[10]，p.14）两处数值未互证；β/γ 冲击因子分量数值未列出（p.14-15）；'net-work' 拼写贯穿全文含关键词（p.1）"
    ],
    "wordsmith": [
      {"quote": "By considering human interests as well as preservation goals, we determine the optimal policy for each land type and its corresponding long-term outcomes.", "page": "p.1", "note": "摘要主旨句：一句话把双目标、分区输出、长期结果全部绑定"},
      {"quote": "To minimize error through errant parameters, we apply random residuals in our model to capture unobserved heterogeneity.", "page": "p.1", "note": "摘要验证句：随机残差=对未观测异质性的诚实声明，'capture unobserved heterogeneity' 值得抄"},
      {"quote": "The results from our sensitivity analysis show that the model is stable and robust.", "page": "p.1", "note": "检验结论句式：敏感度→稳定性直连（且正文真的给了 CC 数值区间支撑，p.22）"},
      {"quote": "restricting tourism quickly produces salutary results until 2030 but slowly declines in the further future due to loss of residential income", "page": "p.18", "note": "政策时间尺度句：'起效快但后劲衰减' vs '起效慢但长期有利'（下一句 grazing fines）——把曲线形状翻译成决策语言"},
      {"quote": "this result is extremely dependent upon our predetermined parameter, reducing the certainty of this possible outcome", "page": "p.18", "note": "诚实质疑句式：对自家反直觉结论主动标注参数依赖——评委最吃这一套的自检"},
      {"quote": "the construction of a wildlife corridor can increase wildlife numbers by 0.5% annually, it will reduce livestock populations as a result of competition for grasslands", "page": "p.2", "note": "信件里的'数字+机制'句式：每个建议都是 数字+但+机制 三段"},
      {"quote": "the benefits of compensating livestock losses go beyond measurable numbers and that it is vital in building the trust between locals and the conservancies", "page": "p.3", "note": "不可量化价值论证句式：分数没赢但政策仍推荐——把模型外逻辑写进信件（正文 p.20 同步）"}
    ]
  },
  "distinct": "非技术报告前置为量化信件（p.2-3）：12 处结果数字与 Table 2 政策参数表（p.17）逐条闭环，评委前 3 页即完成'建议—数字—机制'三重交付；辅以每 section 固定三段式（Modelling ideas→Supplementary assumptions→Calculations, p.8-15）与 VI 章 CC 迁移检验（p.22）。与同题 F 卡（2316192）对照成立：F 的非技术海报在文末（F p.23-24）、无三段式模板、无可迁移性章节；与同题其他 O 卡对照待补。"
}
```

## 2. 同题 O-vs-F 升档差值（O=2300136 p.X / F=2316192 p.Y）

对照基线：F 卡 §2 的六维度（其对照对象为 2024 E Soochow O 卡）；本节按**同题同年**证据逐维度重比。两篇同为 25 页、同题面。

1. **假设→参数→数值闭环**。O 的假设体系分两层：6 条主假设逐条绑引文数字（85% household income [10]，O p.6；25%/75% 土地占比 [11]，O p.6），另有每 section 的补充假设同样带数（生物量 180/23/123/200 kg 引 [16]，O p.10；草地参数 g=41.9、b=1/4000、r=0.47% 引 [17]，O p.10；汇率 1:100 用 2012-2022 实证，O p.12-13；2% 折现率引 200 专家共识 [20]，O p.13；罚款 100.53/损失 247.74 USD 引 [10]，O p.14）。政策端全部落成 Table 2 一张量化表（O p.17）。F 的 4 条主假设同样逐条 justification（F p.6），但核心动力学参数 r/x_m/E、Q_j、z1-z3 全程无数值无来源（F p.17-18）。**差距不在假设条数，在"假设→参数→数值"的最后一公里：O 的每个方程都有可查的参数账，F 的 Model III 方程只有符号。**

2. **模型链接口：参数改写即接口**。O 的三问共用一套评分函数（final score 公式，O p.16）：上游 Table 2 的政策百分比（O p.17）直接改写 Score1-4 的输入变量，下游 24 次仿真与三区排序全部复用同一函数（O p.18-20）——接口即公式与参数表。F 是三棒接力（耦合度分类 F p.8-10 → AHP+0-1 规划 F p.12-15 → Logistic+随机仿真 F p.17-18），接口靠定性规则（Underdeveloped Grid 的权重不等式，F p.14）加单网格孤例 μ_L=0.583/μ_H=0.417（F p.15）。**O 的评委只需理解一张 Table 2；F 的评委要在两处自行补全映射规则。**

3. **检验报数率**。O 的检验条条带数：CR 三值 0.0612/0.0223/0.0301（O p.16）、三处 R²（O p.9/13）、CC 扫描报 final score 区间 0.5-0.575（O p.22）。F 的检验有框架但近乎不报数：CR 只写 "the final CR < 0.1"（F p.14）、敏感度 Score 公式未定义（F p.20）、80/20 分割只画在流程图（F p.7 Fig4）从未出样本外数字。对照 05 模块 §1.4 与 E_可持续死法#3：**CR"做了"和"报数"是两件事——这是两篇在检验维度最尖锐的差值**。O 的敏感度结论也是定性的（O p.21），但其 CC 检验补了一个数值区间，F 连一个检验数值都没有。

4. **图表论点密度**。O 共 12 图：概念图仅 Fig1（O p.8），其余 11 张中 5 张实数据图（Fig2 p.9、Fig3 p.11、Fig4 p.12、Fig5 p.13、Fig6 p.15）+ 6 张结果图（Fig7 p.16、Fig8-10 p.18-20、Fig11 p.21、Fig12 p.22）。F 共 8 图：6 张流程/概念图（F p.4/5/7/8/9/12），唯一实数据锚点是引用地图（F p.3）与地名坐标表（F p.10），核心中间产物"四类栅格分区"只有概念示意（F p.9 Fig6）。O 的三类核心中间产物全部有实数据图：水压力月度热图（O Fig4 p.12）、三区实地图（O Fig6 p.15）、权重条形图（O Fig7 p.16）。**O 的图多在证明"结论成立"，F 的图多在说明"做了什么"——同题证据强化 F 卡判断。**

5. **摘要数字密度与结果量值的位置**。两篇摘要页同为工作量计数型：O 摘要（O p.1）=四 section/三类土地/三政策/24 情景/20 年，F 摘要（F p.1）=8.75km/四类/六政策/四层/十二情景。差值在**结果量值的位置**：O 把非技术报告前置为 p.2-3 信件，内含 12 处结果数字（50%→2%→5%→30%→0.5%→5%→0.5%→10%→8%→0.5%→0.7%→USD$310），其中 11 处可逐条回查 Table 2（O p.17）；F 的唯一结果型数值 max W=2.597672 在正文 p.15（F 卡已登记"未进摘要"），非技术海报在文末 F p.23-24，且 Model III 输出仅定性解读（F p.22）。**评委按序阅读的前 3 页内，O 可触达 12 处结果量值，F 为 0 处（首个结果值在第 15 页）。**修订 F 卡候选 1：升档动作不是"往一页摘要塞数字"，而是"把结果量值前移到评委最先读到的页面，并与参数表闭环"。

6. **distinct 风格：反直觉登记 + 三段式节奏**。O 主动登记两个反直觉结果并给机制与自质疑：① hunting quotas 单独施行长期负面，机制=政策参数压迫草地，并自认 "extremely dependent upon our predetermined parameter"（O p.18）；⑥ wildlife corridor 有害，机制=资源竞争+偷猎+PIE 上升（O p.19）；另有"补偿政策分数无差异但值得推荐"的不可量化论证（O p.20→信件 O p.3）。F 全文结论与直觉同向，无反直觉登记。写作节奏上，O 每个 section 固定三段式 Modelling ideas→Supplementary assumptions→Calculations（O p.8-15），假设跟随模型分散登记；F 假设集中于 §2（F p.6），章节为公式流水式。**"模型在思考"vs"模型在执行"是 distinct 维度的核心差值。**

7. **时点排序与基线对照**。O 每区给 2022/2032/2042 三时点八情景排序表（Tables 3/4/5，O p.18/19/20），HSZ 冠军随时间变化被如实展示（④⑤→④，O p.19）——这正是 05 模块 §1.5 要求的"条件化结论"（"best policy for most years"，O p.1）；每个情景图含 Non 基线并推出"政策选择有效"（O p.18-20）。F 的排序是单网格孤例（Table 6，F p.15-16），百年预测无基线对照、无时点对照，输出仅定性解读（F p.19/22）。

8. **题面逐句对齐**。题面两处高亮要求：① "within and outside the current boundaries"（题面 p.1）→ O 的三区划分明确 "HSZ and LGZ mainly exists outside the reserve in surrounding conservancies"（O p.15 + Fig6 实地图）；② "how your approach could be applied to other wildlife management areas"（题面 p.1）→ O 专设 VI 章，用 correcting coefficient 做成定量检验并自带 CC∈[−3.6%,−90%] 敏感度（O p.22）。"estimates of the certainties"（题面 p.1）→ O 的随机残差+α 扫描+CC 区间三层交付（O p.1/21/22）。F 对要求②无对应章节或动作（F 卡 structure 全序列无 universality 项）。**题面每句话都有交付物，是 O 结构层面的隐性得分点。**

**反向亮点（O 不做或做得比 F 少的三处，防一面倒）**：① 情景覆盖广度：F 的十二参数配置×百年预测（F p.19）时间跨度比 O 的 20 年预测窗（O p.18-20，图示 2002-2041）更激进；② 加噪鲁棒性检验：F 对小 α 加噪观察波动（F p.20），O 的随机残差是建模成分（O p.11）而非独立加噪实验——F 卡此亮点在同题对照下依然成立；③ 数据源登记形式：F 的 Table 2 六源带 URL（F p.7）比 O 的行文内联引用（O p.2 信件点名五源 + p.25 共 22 条文献）更易集中核查。F 队的短板不在动作缺失，而在数字与证据链断点——同题证据与 F 卡原判断一致。

## 3. 升档差值表收束：F 队补上就到 O（延续 F 卡 §3 候选并按同题证据修订）

1. **结果量值前移并与参数表闭环**（修订候选 1）。O 的证据：非技术信件前置 p.2-3，12 处结果数字中 11 处回查 Table 2（O p.17）；O 的一页摘要本身也是工作量计数（O p.1）——说明升档不在摘要页塞数，而在"评委最先读到的位置有可回查的结果账"。F 队动作：把文末海报（F p.23-24）的数字版前移；把 max W=2.597672 与最优组合 (x1,x4,x5,x6)（F p.15）写进摘要或前置信件。
2. **方程级参数对账**（合并候选 2+5）。O 的证据：不设集中参数表，参数在使用处跟随方程出现并挂文献（g/b/r 引 [17]，O p.10；100.53/247.74 USD 引 [10]，O p.14；2% 引 [20]，O p.13），政策效果集中成一张 Table 2（O p.17）。F 队动作：为 r/x_m/E、Q_j、z1-z3（F p.17-18）补文献值或设定依据；给"政策组合→模型参数"画一张 O 式映射表——F 的数据源表（F p.7）不输 O，断点只在方程级。
3. **检验从框架到报数**（修订候选 3）。O 的证据：CR 报三值（O p.16）、CC 扫描报分数区间 0.5-0.575（O p.22）。F 队动作：CR 报具体数值（F p.14）；给 Fig10 的 Score 定义式并报数值结论（F p.20）；兑现 Fig4 的 20% 测试集或删掉该声明（F p.7）——O 的对应习惯是"每个检验动作至少落一个数字"。
4. **核心中间产物配实数据图**（修订候选 4）。O 的证据：水压力热图（O p.12）、三区实地图（O p.15）、权重条形图（O p.16）——三类中间产物全部可视化且可核查。F 队动作：给四类栅格分区画实数据 α 分布地图或直方图，替换概念示意 Fig6（F p.9）。
5. **题面逐句清点交付物**（新增，同题证据）。O 的证据：题面 "applied to other wildlife management areas"（题面 p.1）→ VI 章 CC 检验（O p.22）；"rank and compare"→三时点排序表（O p.18-20）。F 队动作：为可迁移性补一个最小动作（换一组参数重跑十二情景并报对比即可），并把排序结论写成条件化形式（某时段某组合优）——同时继承 F 队已有优势（百年跨度 F p.19、加噪检验 F p.20、六源带 URL 表 F p.7），这三处 O 反而没做或没做全。

## 4. 自查（代理产出，待站长复核）

- 页码逐条核过：本 PDF 页眉 Page N of 25 与 PDF 页码一致（25/25 页逐页读），卡内 p.1–25 全部对应渲染页核实；F 侧页码均引自 04_卡片_2023B_Fuzhou.md（其页码纪律已核）；题面引句核自官方题面 PDF
- 无臆测：Table 2 政策百分比为设定值、R²=0.5163 偏低未讨论、ξ~N(0, 0.39879²) 单位读不出、USD$310 与 247.74 未互证、Fig11 轴标为读图值、Score4 的 β/γ 分量未列出——均按"读不出/如实登记"处理；网络耦合结构注记标明为结构性观察
- 身份 O 档经官方 Results 册交叉验证（Tsinghua University / Heng Liang / Outstanding Winner，2023_B_Results.pdf p.3-4）；distinct 与同题 F 卡对照成立、与同题其他 O 卡对照待补；全部英文引注 ≤25 词；对比用事实陈述，反向亮点单列防一面倒
