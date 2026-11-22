# 模式卡片 · 2024 ICM E · 队伍 2413552（Soochow University）

> **身份验证链**：论文 PDF（队伍自发布于 GitHub，25 页，正文匿名 Team Control Number XXXXX）→ 同仓库附官方证书（队伍号 2413552）→ 官方 Results 册名录（`2024_E_Results.pdf` p.2）核对：**Soochow University / 顾问 Kui Wang / E 题 Outstanding Winner / INFORMS Award**。三者闭环，2026-11-22 验证。
> **页码纪律**：本卡页码均为 PDF 页码 p.1–25；印刷页码 = PDF − 2。
> **版权纪律**：PDF 存本地学习目录（不进公开仓库）；本页只放本站原创分析与 ≤25 词短引注。
> 论文经拆解代理逐页深读 + 站内方法清单（[03_统计与机器学习](../02_知识模块/03_统计与机器学习.html)、[E_可持续](../03_题型打法/E_可持续.html)）交叉对照。

## 1. 模式卡片

```json
{
  "team": "2413552（Soochow University，顾问 Kui Wang；E 题 Outstanding Winner + INFORMS Award，官方名录交叉验证；PDF 正文匿名）",
  "problem": "2024-E（Sustainability of Property Insurance）",
  "tiers": {
    "summary": {
      "背景问题": "全球气候变化下极端天气频发，财产保险业面临可持续性挑战（p.1）",
      "任务重述": "三问：Q1 承保/定价策略，Q2 社区建设与发展策略，Q3 历史地标保护（自由女神像）（p.1；与 §1.2 p.4 对应）",
      "方法主线": "MGWR 整合气候数据+地理位置+保险赔付；熵权法定人文调整系数 HIC；盈利调整因子 P；灰色预测 GM(1,1) 外推 2024-2034（p.1）",
      "关键结果数字": "加州（高风险区）2023 年保险金额 $20.1394M，预计 2034 年增至 $31.0054M；自由女神像保护年投入约 $2.5M（p.1）",
      "结论建议": "为保险公司提供承保决策支持，为社区与遗产保护提供可行策略（p.1）",
      "关键词": "Climate change, property insurance, risk assessment, community development, historical heritage protection, multi-scale geographically weighted regression（p.1）"
    },
    "structure": [
      "Summary Sheet（p.1）",
      "Contents（p.2）",
      "1 Introduction：Background / Problem Restatement / Related Work / Our Work（p.3-5）",
      "2 Preparation：Assumptions（仅 3 条）/ Notations（p.5-6）",
      "3 Introduction（与 §1 重名的过渡小节——O 论文也有结构瑕疵，p.6）",
      "4 Insurance Strategy Model：Data / Preprocessing / MGWR / Risk Pricing / Multi-Objective / GM(1,1) / Solution（p.6-13）",
      "5 Community Building Protection：Protection Model / Owner Strategies / Solution（p.13-18）",
      "6 Historical Landmarks：Adapting to MGWR / Statue of Liberty / A Letter to the Community（p.19-21）",
      "7 Sensitivity Analysis（标题拼写为 Senitivity，p.21-22）",
      "8 Strengths and Weaknesses + Future Applications（p.22-23）",
      "9 Conclusion（p.23）",
      "Letter（题面交付物：致社区完整信件，p.24）",
      "References + AI Utilization Report（p.25）"
    ],
    "models": [
      {"name": "PCA 降维", "type": "预处理/降维", "assumptions": "线性变换保留主要信息（eq2, p.7）", "validation": "报 4 个主成分方差 42.1%/16.6%/13.7%/10.6% 并逐个解释物理含义（p.11）", "pages": "eq2 p.7；结果 p.11"},
      {"name": "双变量样条插值", "type": "空间插值（格点气候→事件经纬度）", "assumptions": "格点值可局部逼近（eq3, p.8）", "validation": "未报告（诚实留空）", "pages": "p.8"},
      {"name": "极端天气阈值判别", "type": "规则分类（插值环境值>阈值记为极端事件）", "assumptions": "阈值 T_extreme 可定义极端条件（eq4, p.8）", "validation": "未报告；用于补全官方记录缺失（p.8）", "pages": "p.8"},
      {"name": "MGWR 主模型", "type": "空间回归（各协变量各自带宽的地理加权回归）", "assumptions": "极端天气对赔付的影响存在显著空间异质性（假设2, p.5）", "validation": "未报告 R²/AICc/带宽等诊断（全 25 页无诊断表，诚实留空）；摘要级结论：高风险区赔付与极端事件概率显著正相关（p.1）", "pages": "eq5-6, p.8-9"},
      {"name": "风险定价模型", "type": "多目标定价公式（保费=基准×风险分×人文系数×盈利因子，eq7-9）", "assumptions": "H_i=g(SEF_i), P=HPR+TPM, FP_i=BP(1+θRS_i)H_iP（p.9）", "validation": "作为 Q1 策略输出（Table 2 分州预测, p.12）", "pages": "p.9"},
      {"name": "多目标优化", "type": "双目标均衡（人文 HI vs 盈利 PR，eq10）", "assumptions": "提及线性规划或遗传算法求解（p.10）", "validation": "求解器细节未展示（诚实留空）", "pages": "p.10"},
      {"name": "灰色预测 GM(1,1)（改进版）", "type": "时序外推（AGO+最小二乘）", "assumptions": "序列近似指数增长、趋势延续（p.10）", "validation": "声明历史回测但未报误差指标（p.10）；输出 Fig3/Table2/Table3（p.12-13）", "pages": "eq11-12 p.10"},
      {"name": "社区保护模型", "type": "MGWR 扩展+损失最小化（加保护因子 P_i；min L=Σ(D_i+λC_i)，eq13-16）", "assumptions": "风险承载力与保护投入可量化且成本线性（p.12-13）", "validation": "scipy 求解北美数据；解读为保护水平约 70%、成本约 30%（p.16；Fig5 p.17）", "pages": "p.12-13, 16-17"},
      {"name": "改进熵权法→HIC", "type": "综合评价赋权（→线性 g 函数）", "assumptions": "社会经济因子与保险需求相关（假设3, p.5）", "validation": "以最小化实际-预测保费差训练 a,b（p.16）未给数字；权重表 Table4：healthcare 0.375/GDP 0.250/人口密度 0.250/教育 0.125（p.16）", "pages": "eq17-21 p.13-16"},
      {"name": "建筑保护 MGWR（Q3）", "type": "空间回归改写（因变量=所需保护等级）", "assumptions": "建筑规模/年龄/材料/复杂度/区位决定保护需求（p.19）", "validation": "自由女神像系数区间解读（p.20-21；Fig8 雷达图 p.21）", "pages": "eq22 p.19"}
    ],
    "figures": [
      {"id": "Fig 1", "page": "p.3", "claim": "开场钩子：保险策略是应对极端天气的核心", "type": "概念插图（AI 生成）", "self_evidence": "低——装饰性"},
      {"id": "Fig 2", "page": "p.11", "claim": "极端天气概率空间分异：西部偏旱、东南偏涝，支撑风险分区定价", "type": "地理热力图", "self_evidence": "高——单图自足"},
      {"id": "Fig 3", "page": "p.12", "claim": "2000-2023 实测与 2024-2034 GM(1,1) 预测接续：事件数与保险业绩效同步上升", "type": "双轴时序预测图", "self_evidence": "中"},
      {"id": "Fig 4", "page": "p.14", "claim": "保险不足时业主自力更生（引出 Q2）", "type": "概念插图（AI 生成）", "self_evidence": "低"},
      {"id": "Fig 5", "page": "p.17", "claim": "各州保护/风险/成本三变量空间分布与正相关（Q2 解）", "type": "地图叠加散点", "self_evidence": "低-中——三色条并存较难读"},
      {"id": "Fig 6", "page": "p.18", "claim": "NA 与 Asia 双面板、三情景损失对照：干预降低损失增速", "type": "分组时序折线", "self_evidence": "高——但正文引用数字与图线序疑似矛盾（见瑕疵清单）"},
      {"id": "Fig 8", "page": "p.21", "claim": "自由女神像 MGWR 系数雷达图：保护需求主要由规模与区位驱动", "type": "雷达图（5 因子）", "self_evidence": "中-高"},
      {"id": "Fig 9", "page": "p.22", "claim": "换熵权系数重跑后损失趋势不变→稳健", "type": "与 Fig 6 同构对照双面板", "self_evidence": "中——须与 Fig 6 并排对读"}
    ],
    "checks": [
      "GM(1,1) 历史回测：声明式，无误差指标（p.10）",
      "g 函数训练验证：最小化实际-预测保费差，无数字（p.16）",
      "敏感度/消融：§7 单独成章——仅对熵权系数做 ablation，换权重重跑三情景（p.21-22；Fig9 p.22）；全文最主要检验",
      "跨区域外推复用：同一 MGWR 框架改坐标+人口重拟亚洲六国（Table3, p.13）——可迁移性的间接证据",
      "缺项（诚实登记）：MGWR 无 R²/AICc/带宽诊断；无样本外交叉验证；无蒙特卡洛；熵权未与主观赋权组合对照；插值与阈值判别无独立验证（依据：p.8-13 全部方法节无诊断表）"
    ],
    "wordsmith": [
      {"quote": "This study presents a comprehensive analytical framework addressing the sustainability of the property insurance sector under extreme weather conditions.", "page": "p.1", "note": "摘要首句模板：『对象+框架+条件』一句立起全文，19 词无废话"},
      {"quote": "our model predicted insurance amounts for California (a high-risk area) to be $20.1394 million in 2023", "page": "p.1", "note": "摘要必塞『具体地名+精确数字』，证明跑过真数据"},
      {"quote": "Unlike GWR, which assumes a single bandwidth for all covariates, MGWR allows for different spatial scales", "page": "p.8", "note": "对比式方法引入：先立传统方法局限，再给自己的模型留位置"},
      {"quote": "This approach not only aligns with actuarial principles but also embeds an element of social responsibility", "page": "p.7", "note": "双价值收束句：E 题人文维度专用，放模型引入处"},
      {"quote": "despite changes in the model's parameters, the trend of losses caused by extreme weather events continues to fluctuate and rise", "page": "p.21", "note": "敏感度结论句式：『尽管参数变化，趋势不变』——把稳健性写成一句话"}
    ]
  },
  "distinct": "暂缺——需同题对照（本库尚无 2024 E 其他 O 队卡片，按纪律不得单卡填写）。候选三项待比对：① AI 生成插图贯穿全文并在 AI Utilization Report 合规披露（p.3/14/20/25）；② 一个 MGWR 模型三次改写贯穿三问（定价 p.8-9→加保护因子 p.12→改因变量 p.19）；③ 题面要求的信件以完整独立章节交付（p.24）。"
}
```

## 2. 可复用的打法提炼（普通队可直接抄的动作）

1. **一个核心模型贯穿三问，逐问做"加法改写"**：MGWR 在 Q1 定价（p.8-9）→ Q2 加保护因子（p.12）→ Q3 改因变量（p.19）。主线天然统一，评委不用每次重新理解模型——"一模型+逐问扩展"是最稳的骨架，而不是每问另起炉灶。
2. **外部数据源三件套并给脚注 URL**：ERA5-Land（96 变量、0.1°×0.1°）、Global Disaster Data Platform、NAIC，脚注直接给可点击链接（p.7）。题面数据不够用时主动补权威源并注明出处——O 队与普通队的常见分野。
3. **预处理链条每步给公式，降维必报方差贡献**：标准化→PCA→样条插值→阈值判别全公式化（p.7-8），四个主成分方差逐一报出并解释物理含义（p.11）。普通队常只写"用 PCA 降维"一句——工作量小、观感差距大。
4. **把人文维度参数化，而不是写成口号**：熵权 HIC、定价系数、权重表（p.9, 13-16）——"人道关怀"落进公式和数字里。
5. **预测做"历史+未来"双段图，配逐年数字表**：Fig3 实测与预测接续（p.12），Table2/3 逐年数值（p.12-13）——摘要的数字可回查到表。
6. **干预有效性用"三情景对照实验"呈现**：三情景同图、双面板（p.18），一图回答"干预有没有用、谁的作用大"——把"建议"升级为"证据"。
7. **检验从简但必须存在，且单独成章**：§7 先承认"超参少"，只做消融+重跑（p.21-22）——"小成本、大覆盖"的稳健性叙事；但注意本文除消融外无样本外/收敛检验，**补一个样本外误差即可超过它**。
8. **交付物形态贴题面 + AI 使用合规披露**：Q3 要 letter 就给完整信件（p.24）；文末 AI Utilization Report 声明 ChatGPT 用于插图与润色（p.25）。题面点名的交付物一个都不能少。

### 瑕疵清单（O 论文也有，反着学）

- §3 与 §1 重名都叫 "Introduction"（p.6）——章节命名要终检
- §7 标题拼写错误 "Senitivity Analysis"（p.21）
- Table 2 数值与摘要对应但表头未标单位（p.12 vs p.1）——表格必须带单位
- Fig 6 正文引用数字与图上线序疑似矛盾（正文称社区干预 125→275，超出面板 y 轴上限 250；p.18）——"图-文数字一致性"终检必须做（此条为渲染观察，已标注待人工复核原图）

## 3. 升档差值视角

本卡是 O 侧第一张卡。升档差值分析（O vs H/M）需要同题 H/M 论文对照后才能做"差值表"——当前可对照的**反向参照**：这篇 O 论文的 5 项检验缺项（无拟合诊断/无样本外/无蒙特卡洛/无组合赋权/插值无验证）说明 **H 档与 O 档的差距未必在检验数量**，而更可能在：数据源的主动扩展（打法 2）、模型链条的贯穿性（打法 1）、人文维度的参数化（打法 4）。待 H/M 卡片入库后逐项验证。

## 4. 自查（代理产出，站长复核通过）

- 字段页码逐条核过（PDF 页码，对照 25 页渲染图）
- 无臆测：两处诚实登记（"未报告验证"为缺项记录；Fig 6 矛盾标"疑似待复核"）
- distinct 按纪律填"暂缺——需同题对照"
