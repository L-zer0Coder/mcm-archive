# 模式卡片 · 2023 MCM B · 队伍 2316192（Fuzhou University，Finalist）

> **身份验证链**：论文 PDF 为队伍自发布版（Summary Sheet 印队伍号 2316192，p.1；页脚署名 Hanlin Cai, Yufei Wu, Wenxuan Luo, Fuzhou University，p.1/p.25）→ 站长据官方 Results 册交叉验证（2023_B_Results.pdf p.4）：**Fuzhou University / 顾问 Zhezhuang Xu / 2023 B 题 Finalist**，2026-11-22 核。注意：网络曾有说法暗示该队为 O 奖——与官方 Results 册不符，**已证伪，本卡如实标 F 档**。
> **页码纪律**：本 PDF 页眉自印 "Page N of 25"，印刷页码与 PDF 页码一致；卡内页码即 PDF 页码 p.1–25。
> **版权纪律**：PDF 存本地学习目录（不进公开仓库）；本卡只放本站原创分析与 ≤25 词短引注。
> 论文经拆解代理逐页深读（25/25 页），与站内方法页（[E_可持续](../03_题型打法/E_可持续.md)、[03_统计与机器学习](../02_知识模块/03_统计与机器学习.md)、[05_评价与决策](../02_知识模块/05_评价与决策.md)）交叉对照。O 侧参照卡：[01_卡片_2024E_Soochow](01_卡片_2024E_Soochow.md)。

## 1. 模式卡片

```json
{
  "team": "2316192（Fuzhou University，顾问 Zhezhuang Xu；2023 B Finalist，官方 Results 册交叉验证；本 PDF 为自发布版，含作者署名）",
  "problem": "2023-B（Reimagining Maasai Mara：马赛马拉保护区的分区政策、政策排序与长期预测）",
  "tiers": {
    "summary": {
      "背景问题": "人类社会与土地资源的变化正破坏马赛马拉的人地关系平衡，需在经济与生态间求最优政策组合（p.1）",
      "任务重述": "四目标：分区政策建议 / 政策评价排序方法 / 长期趋势预测与确定性 / 两页非技术报告（p.1；对应 §1.2 p.4 Objective 1-4）",
      "方法主线": "Model I 人地耦合度分析（熵权+栅格化 8.75km 网格四分类）；Model II AHP 四层评价+0-1 多目标规划选政策组合；Model III Logistic 方程+收入随机模拟，Python 十二组百年情景（p.1）",
      "关键结果数字": "网格宽 8.75km、四类网格、六项政策、四层结构、十二组百年情景——全部为工作量计数；唯一结果型数值 max W=2.597672 未进摘要（p.1 vs p.15）",
      "结论建议": "敏感度与鲁棒性分析微调参数、改进长期预测性能；优势与可能改进分析；非技术报告交付肯尼亚旅游与野生动物委员会（p.1）",
      "关键词": "Human-Land Relationship, Multi-objective Optimization, Trend Prediction Model, Maasai Mara Nation Reserve (MMNR)（p.1）"
    },
    "structure": [
      "Summary Sheet（p.1）",
      "Contents（p.2）",
      "1 Introduction：Background / Restatement / Related Policies and Strategies（1992-2021 四代政策综述）/ Overview of Our Works（p.3-5）",
      "2 Assumptions and Justifications：4 条假设逐条给 justification（p.6）",
      "3 Notations and Description（Table 1，p.6）",
      "4 Model Preparation：Data Collection（Table 2 六个数据源带 URL）/ Data Pre-Processing（eq1 标准化 + Fig4 80/20 分割流程图）（p.7）",
      "5 Model I 人地耦合分析：耦合度模型（eq2-3）/ 栅格化（Table3 + eq4 Haversine，W_g=8.75km）/ 六项政策与策略（p.8-11）",
      "6 Model II 策略选择：四层 AHP 评价（eq5-6 + Table4/5）/ 0-1 多目标优化（eq7-10）+ 单网格测试（Table6）（p.12-16）",
      "7 Model III 长期预测：Logistic+捕获（eq11）/ 环境容量动态（eq12）/ 收入随机模拟（eq13）/ Python 程序+十二情景结果（Fig9）（p.16-19）",
      "8 Sensitivity and Robustness Analysis（Fig10）（p.20）",
      "9 Model Evaluation：4 条 Strengths / 2 条 Weaknesses+Improvements（p.21）",
      "10 Conclusion and Further Discussion（p.22）",
      "Non-technical Report：两页海报版式（题面交付物，p.23-24）",
      "References（11 条，p.25）"
    ],
    "models": [
      {"name": "向量归一化标准化", "type": "预处理", "assumptions": "数据量纲不统一需消除（p.7）", "validation": "未报告", "pages": "eq1, p.7"},
      {"name": "熵权法", "type": "客观赋权", "assumptions": "指标区分度可由信息熵度量（p.8）", "validation": "四步公式齐全但熵权数值未单独列出（p.8）；后文 Table4/5 的指标权重改由 Google Scholar 词频估计（p.13）", "pages": "p.8"},
      {"name": "人地耦合度模型", "type": "综合评价/耦合协调（改自文献）", "assumptions": "两子系统效用可线性加权 f(H)=Σa_i x_i、f(L)=Σb_j y_j；耦合度 α=arctan(f(H)/f(L))（eq2-3，based on Ref[3]）", "validation": "未报告：α 无实数据分布/直方图，四类阈值 35/45/65 来源未注明", "pages": "p.8-10"},
      {"name": "栅格化方法+Haversine", "type": "空间离散化", "assumptions": "Big MMNR 区（0.56264N~2.1124S, 33.919E~36.344E）可均分为 n=10 格；'for the convenience of calculation'（p.10）", "validation": "网格宽 W_g≈8.75km、面积 S_g=76.5625km² 自洽；n 的选择无敏感度说明", "pages": "eq4, p.9-10"},
      {"name": "AHP 四层策略评价", "type": "综合评价赋权+排序", "assumptions": "四指标 BD/EQ/EB/DI 可 1-9 标度两两比较（eq5）；Google Scholar 词频（47.7M/13.1M/24.45M/11.9M）可代理专家判断（p.13，非常规做法）", "validation": "一致性检验 eq6：'the final CR < 0.1'（MATLAB）——声明式，无数值、比较矩阵未展示；Table4 中 Tourist 1.1606739 与 Livestock 1.16067393 近乎并列仍分 rk1/rk2", "pages": "p.12-14, Table4/5 p.13"},
      {"name": "0-1 多目标规划", "type": "整数规划/多目标", "assumptions": "政策效用可用三角函数子权重（α, sinα, 1−cosα, cosα, 1−sinα, 1−α）线性加权（eq8，借 Ref[11] 不等式链）；预算约束=至多 4 项且每子系统至少 1 项（p.15 Constraint I-III）", "validation": "单网格测试：Mulima Mbili α_test≈20°，μ_L=0.583/μ_H=0.417，最优组合 (x1,x4,x5,x6)，max W=2.597672（p.15-16, Table6 六种组合排序）", "pages": "eq7-10, p.14-16"},
      {"name": "Logistic+捕获方程", "type": "微分方程/种群动力学", "assumptions": "动物按 Logistic 增长（Assumption1, p.6）；捕获率与种群数成正比：dx/dt = rx(1−x/x_m) − Ex（eq11）", "validation": "未报告：r、x_m、E 数值与来源全缺", "pages": "eq11, p.17"},
      {"name": "环境容量动态方程", "type": "离散动力学", "assumptions": "三项产业对承载力的影响线性可加：x_m(t+1)=x_m(t)[1−(z1+z2+z3)]（eq12）", "validation": "未报告：z1-z3 数值与来源全缺", "pages": "eq12, p.17"},
      {"name": "居民收入随机模拟", "type": "蒙特卡洛/随机模拟", "assumptions": "前三类经济活动（hunting/land leasing/logging）受罚打折、后三类（tourism/crop/livestock）增益，折扣因子 R_j~U[0,1.5]（eq13）", "validation": "未报告：基线收入 Q_j 数值与来源全缺；随机模拟跑多少次取平均未说明", "pages": "eq13, p.18"},
      {"name": "Python 预测程序+十二情景", "type": "系统仿真/参数扫描", "assumptions": "政策组合与耦合度 α 映射为仿真系数（pseudocode, p.18）", "validation": "12 组参数（α=17/40/55/77° × 3 种政策组合）×100 年预测（Fig9, p.19）；伪代码循环 t=1 to 50 与'100 年'表述疑似不一致（待复核）；输出仅定性解读（p.22）", "pages": "p.18-19"}
    ],
    "figures": [
      {"id": "Fig 1", "page": "p.3", "claim": "MMNR 生态与经济分布双图：确立研究对象的地理底账", "type": "引用地图拼图", "self_evidence": "中（无数据加工）"},
      {"id": "Fig 2", "page": "p.4", "claim": "1992-2021 四代管理政策演进时间轴，为'我们的方法站在最前沿'做铺垫", "type": "文献综述流程图", "self_evidence": "低-中"},
      {"id": "Fig 3", "page": "p.5", "claim": "全文建模流程总览（两阶段：分类评价→选择）", "type": "总流程图", "self_evidence": "中"},
      {"id": "Fig 4", "page": "p.7", "claim": "数据预处理流水线，标注 80% 建模/20% 测试分割", "type": "流程图", "self_evidence": "低-中（分割声明后文未兑现数字）"},
      {"id": "Fig 5", "page": "p.8", "claim": "人地双子系统与耦合区概念示意", "type": "概念插图", "self_evidence": "低"},
      {"id": "Fig 6", "page": "p.9", "claim": "栅格化后按 α 分四类网格的示意（0-35/35-45/45-65/65-90°）", "type": "概念示意（非实数据）", "self_evidence": "中（分阈清晰但非计算结果）"},
      {"id": "Fig 7", "page": "p.12", "claim": "四层 AHP 评价结构树：目标-子系统-政策-指标", "type": "层次结构图", "self_evidence": "低-中"},
      {"id": "Fig 8", "page": "p.16", "claim": "测试网格档案卡：Mulima Mbili，α_test≈20°，坐标/宽度/面积/地貌", "type": "信息卡+定位图", "self_evidence": "中"}
    ],
    "checks": [
      "AHP 一致性检验：CI/CR 公式（eq6）+ 'final CR < 0.1'（MATLAB），无数值、比较矩阵未展示（p.14）——声明式",
      "敏感度：S_A/S_B/S_C 三种政策组合对 α∈(0,90) 全程扫描（Fig10, p.20）；Score 的计算式未给出（读不出）",
      "鲁棒性：小 α 时加噪声观察系统波动，发现噪声影响随 α 增大递减（p.20）——加噪检验是本卡少见的动作",
      "参数扫描：12 组参数配置×100 年预测矩阵（Fig9, p.19）——情景矩阵替代单点预测",
      "训练/测试分割：Fig4 流程图标 80%/20%（p.7），但全文无样本外测试数字——分割声明了未兑现",
      "缺项（诚实登记）：Logistic 参数 r/x_m/E、收入基线 Q_j、产业强度 z1-z3 无数值无来源（p.17-18）；四类阈值 35/45/65 来源未注明（p.10）；耦合度 α 无实数据分布图，四分类仅概念示意（Fig6, p.9）；熵权结果未以数字呈现（p.8）；伪代码 t=1..50 与 100 年表述疑似不一致（p.18 vs p.19）；无蒙特卡洛次数口径（p.18-19）；AHP 权重无组合赋权对照（对照 05 模块 §1.2 纪律）"
    ],
    "wordsmith": [
      {"quote": "recent changes in human society and land resource are jeopardizing the human-land relationship balance", "page": "p.1", "note": "摘要背景句：把冲突压成一个可贯穿全文的核心变量（人地平衡）"},
      {"quote": "we utilize the Rasterized Method to divide the Big Maasai Mara area into various discrete grid with a width of 8.75km", "page": "p.1", "note": "摘要方法句带具体参数（8.75km）——证明真跑过，此习惯值得抄"},
      {"quote": "we obtain and present twelve 100-year prediction scenarios correspond to twelve sets of parameter configurations to verify the effectiveness and rationality of our model", "page": "p.1", "note": "摘要验证句式：情景数量×时间跨度+验证意图一句话说完"},
      {"quote": "Inspired by the related reference, these two inequation will be utilized to determine the sub-weight of the objective function", "page": "p.14", "note": "亮点技巧：用 α>sinα>1−cosα 不等式链生成目标子权重——'借数学不等式定权'可迁移"},
      {"quote": "the optimal combination in this grid is (x1, x4, x5, x6) and the corresponding total utility value reaches max W = 2.597672", "page": "p.15", "note": "结果句式：具体组合+精确数值——可惜这句没进摘要"}
    ]
  },
  "distinct": "暂缺——需同题对照（本库尚无 2023 B 其他 O/F 卡片，按纪律不得单卡填写）。候选三项待比对：① Google Scholar 关键词词频替代两两比较定 AHP 权重（p.13）；② 三角函数不等式链生成目标函数子权重（p.14）；③ 12 参数配置×100 年预测情景矩阵（p.19）。"
}
```

## 2. F 档特征分析（本卡独有任务：与 O 档卡逐维度对照）

对照对象：[01_卡片_2024E_Soochow](01_卡片_2024E_Soochow.md)（2024 E O 奖 + INFORMS 奖，下称"O 卡"；页码为该论文 PDF 页码）。本卡页码为 2316192 PDF 页码。

1. **假设数量与参数追溯**：F 队 4 条假设且逐条 justification（p.6），条数多于 O 队的 3 条（O 卡 p.5-6）；但 F 的假设是"方向性免责"——与模型参数不闭环：Logistic 的 r/x_m/E、收入基线 Q_j、产业强度 z1-z3 全程无数值无来源（p.17-18）。O 队假设直接绑定可执行参数并落到数字（熵权权重表 Table4 四个权重值，O 卡 p.16；PCA 四个方差贡献 42.1%/16.6%/13.7%/10.6%，O 卡 p.11）。**假设多≠追溯强：F 档差距在"假设→参数→数值"的最后一公里**。

2. **模型链条层数与接口**：F 队三问三模型接力（耦合度分类 p.8-10 → AHP+0-1 规划 p.12-15 → Logistic+随机收入仿真 p.17-18），链条完整但接口松：上游"四类网格"如何变成下游权重，只有定性规则（Underdeveloped Grid: weight of (x1,x2,x3) < (x4,x5,x6)，p.14）加一组孤例 μ_L=0.583/μ_H=0.417（p.15）。O 队一个 MGWR 三次显式改写贯穿三问（O 卡 p.8-9→12→19），接口即公式本身，评委无需重新理解。**F 是"三棒接力"，O 是"一条主线"**。

3. **检验类型计数与报数率**：F 队 4 类检验动作（CR 一致性 p.14、敏感度扫描 Fig10 p.20、加噪鲁棒 p.20、12 情景参数扫描 p.19）对 O 队 5 类（O 卡 checks：回测 p.10、训练验证 p.16、消融重跑 p.21-22、跨区域外推 p.13 等）。数量不差，**差距在报数率**：F 的 CR 只写 "<0.1" 无数值（p.14）、敏感度 Score 公式未定义（p.20）、80/20 分割只画在流程图无样本外数字（p.7 Fig4）；O 至少报出方差贡献与权重两处数字（O 卡 p.11、16）。检验"做了"和"报数"是两件事。

4. **图表论点密度**：F 队前 8 图中 6 张为流程/概念/示意类（Fig2 p.4、Fig3 p.5、Fig4 p.7、Fig5 p.8、Fig6 p.9、Fig7 p.12），0 张基于计算结果；结果图只有 Fig9（12 面板预测，轴标签版面过小难自明）与 Fig10（p.19-20）。O 队对应 8 图中 6 张为结果图（热力图 p.11、双轴预测 p.12、三情景对照 p.18、雷达图 p.21、消融对照 p.22），概念图仅 2 张（O 卡 p.3、14）。**F 的图多在讲"做了什么"，O 的图多在证明"结论成立"**；尤其 F 的核心中间产物——四类栅格分区——没有一张实数据地图（Fig6 是概念图）。

5. **摘要数字密度**：F 摘要含 6+ 个数字（8.75km、四类、六政策、四层、十二情景、两页报告，p.1）但全部是工作量计数，无一带单位的结果量值；O 摘要有三个带美元单位、可回查表格的结果量值（$20.1394M / $31.0054M / 约 $2.5M，O 卡 p.1）。**"我做了多少"vs"我算出了什么"是最直观的档位信号**。

6. **反向亮点（F 不输 O 的三处，防一面倒）**：① 12 参数配置×100 年情景矩阵（p.19）比 O 卡三情景对照（O 卡 p.18）覆盖更宽；② 小 α 加噪的鲁棒性检验（p.20）在 O 卡 checks 中无同类动作；③ 两页海报版式非技术报告完成度不低于 O 卡 letter（O 卡 p.24，本卡 p.23-24）。F 队的短板不在"动作缺失"而在"数字与证据链断点"。

## 3. 升档差值候选（若这支 F 队要升 O，最可能缺什么）

1. **摘要塞结果量值**。依据 O 卡特征：摘要必塞"具体地名+精确数字"且可回查表格（O 卡 wordsmith 第 2 条，O 卡 p.1）。F 摘要只有工作量计数（本卡 p.1），而 max W=2.597672、最优组合 (x1,x4,x5,x6)（本卡 p.15）就在手边却未进摘要——零成本升档动作。
2. **补一张参数表**。依据 O 卡特征：每个模型的关键参数有数值有出处（PCA 方差 4 数，O 卡 p.11；权重表，O 卡 p.16）。F 的 r/x_m/E、Q_j、z1-z3 全无数值无来源（本卡 p.17-18），评委无法复现预测章节——这是最深的一处证据断点。
3. **把已声明的检验跑出数字**。依据 O 卡特征：检验结论落成一句话+数字（消融"趋势不变"，O 卡 wordsmith 第 5 条，O 卡 p.21-22）。F 的 CR 只写 "<0.1"（本卡 p.14）、Score 未定义（p.20）、Fig4 的 20% 测试集从未出样本外误差（p.7）——**检验框架是现成的，只差报数**。
4. **给核心中间结果一张实数据图**。依据 O 卡特征：热力图直接支撑风险分区结论（O 卡 Fig2，O 卡 p.11）。F 的四类栅格分区只有概念示意 Fig6（本卡 p.9），没有实数据分区地图或 α 分布直方图——Model I 的中心产出在全文中"只闻其名"。
5. **数据→模型对账表**。依据 O 卡特征：外部数据源三件套且脚注给 URL、每一步预处理公式化（O 卡打法 2/3，O 卡 p.7-8）。F 有 Table 2 六个数据源带 URL（本卡 p.7）不输，但对账断链：六个来源各喂进哪个方程读不出，正文出现的唯一实数据锚点是 Table 3 四个地名坐标（p.10）。

## 4. 自查（代理产出，待站长复核）

- 页码逐条核过：本 PDF 页眉 Page N of 25 与 PDF 页码一致，卡内 p.1–25 全部对应渲染页核实
- 无臆测：参数无数值 / CR 无数值 / Score 未定义均按"读不出"登记；伪代码 t=1..50 与 100 年之矛盾标"疑似待复核"；Table 4 近并列名次为如实观察
- 身份 F 档经 Results 册交叉验证（Fuzhou University / Zhezhuang Xu / Finalist）；网络"O 奖"说法已证伪不采；distinct 按纪律填"暂缺——需同题对照"
