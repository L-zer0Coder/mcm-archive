# 模式卡片 · 2024 MCM A · 队伍 2405424（Xi'an Jiaotong University）

> **身份验证链**：论文 PDF（队伍号 2405424，正文匿名 Team Control Number）→ 派单方对官方 `2024_A_Results.pdf` 名册验证：**Xi'an Jiaotong University / 顾问 Yiqing Wang / 2024 A Outstanding Winner**。
> **页码纪律**：本卡页码 = PDF 页码 = 印刷页码（页眉 'Page X of 25'；p.1 Summary Sheet、p.2 Contents、p.25 References + AI 使用报告，全文 25 页——对照 Wuhan 卡 24 页）。
> **论文题目**：Lamprey: a Vivid Example of the Doctrine of the Mean（p.1）——题目即全文主题句（中庸 = 利弊权衡），Conclusion 首尾呼应（p.24）。
> **版权纪律**：PDF 存本地学习目录（不进公开仓库）；本页只放本站原创分析与 ≤25 词短引注。
> 论文经拆解代理逐页深读（25/25 页）+ 站内方法清单（03_题型打法/A_连续、02_知识模块/02_微分方程与动力学）交叉对照；同题 O 卡对照基线：05_论文拆解/06_卡片_2024A_Wuhan.html（Wuhan 2400996，INFORMS 奖）。本卡存 _corpus_local 暂存，入库时链接路径需按站点结构改写。

## 1. 模式卡片

```json
{
  "team": "2405424（Xi'an Jiaotong University，顾问 Yiqing Wang；2024 A Outstanding Winner，官方 2024_A_Results.pdf 交叉验证；PDF 正文匿名，仅 Team Control Number）",
  "problem": "2024-A（Resource Availability and Sex Ratios：七鳃鳗 adaptive sex ratio 对种群与生态系统的影响；连续型；与 Wuhan 卡同题）",
  "tiers": {
    "summary": {
      "背景问题": "七鳃鳗是地球上最古老生物之一，资源可用性影响其性别比——研究它已成为 'inescapable topic'（p.1）",
      "任务重述": "四问逐段作答，每段 'For Task X, we...' 加粗结论：Task 1 生态系统影响（资源总量下降、有七鳃鳗时存活物种数最高）；Task 2 种群利弊（变性别比稳但种群规模小，win some lose some）；Task 3 稳定性评估（熵权法：寄生虫降稳、七鳃鳗显著缓解）；Task 4 对其他寄生虫的影响（周期波动、负反馈放大）（p.1）",
      "方法主线": "以 Lotka-Volterra 捕食-猎物模型 + Nicholson-Bailey 宿主-寄生模型为建模基础，构造三模型：Ideal Reference Model / Constant Sex Ratio Model / Models of Changing Sex Ratios；Task 3 用熵权重法（entropy weighting method）；Task 4 三模型整合（p.1 首段）",
      "关键结果数字": "摘要零数字——结论全为粗体定性断言；数字只在正文（基线资源 ~4.89×10^9 kJ、主要物种 ~8.88, p.8；ESI 0.63/0.54/0.61, p.19；种群 ~1×10^6 vs 最低 ~2×10^6, p.18）（p.1；对照 Wuhan 摘要含 3 个百分数）",
      "结论建议": "模型检验两步走：先讨论实验结果合理性（对应 §5.1），再从人类活动扰动与初值变化两视角做敏感度 → 更抗不确定因子、适用不同初值 → reliability and universality；最后优劣分析并提出对应优化方案（= §6.2 的 Possible solution, p.24）（p.1 末段）",
      "关键词": "Changing Sex Ratios, Ideal Reference Model, Constant Sex Ratio Model, Model of Changing Sex Ratios, Entropy Weighting Method（p.1）"
    },
    "structure": [
      "Summary Sheet（p.1，含论文题目）",
      "Contents（p.2，'Page 2 of 25'）",
      "1 Introduction：1.1 Research Background[1]（生活史 5-8 年+寄生习性+种群动态，Fig 1 实物照片）/ 1.2 Restatement（四问 bullets）/ 1.3 Literature Review（L-V + N-B 双模型选型，Fig 2 建模思路图）/ 1.4 Our Work（5 步列表）（p.3-5）",
      "2 Model Preparation：2.1 Assumptions（3 条主假设各带 justification+文献号，声明 'other assumptions will be given at appropriate places'——分布式假设策略）/ 2.2 Notations（未编号符号表 10 项）（p.5-6）",
      "3 Establishment of Models：3.1 Ideal Reference Model（p.6-8）/ 3.2 Constant Sex Ratio Model（2:1 常规寄生种对照）（p.8-12）/ 3.3 Models of Changing Sex Ratios（p.12-14）/ 3.4 Evaluation Indicators and Stability Analysis（熵权法预告）（p.14）",
      "4 Problem Solutions：开头交代实验设置（n1=10、3 种为七鳃鳗宿主, p.14）；4.1→Q1（p.15-17）/ 4.2→Q2（p.17-18）/ 4.3→Q3（p.18-19）/ 4.4→Q4（p.19-21）——严格按题号顺序作答（对照 Wuhan 按模型层级作答）",
      "5 Rationalization Analysis and Sensitivity Testing：5.1 合理化三查（p.22）/ 5.2 敏感度（1.人类活动 2.初值）（p.22-23）",
      "6 Strengths and Weaknesses（每条 weakness 配 Possible solution）+ 7 Conclusion（p.24）",
      "References（8 条，对照 Wuhan 14 条）+ Report on Use of AI：'No AI tools were used in this article.'（p.25——2024 首设 AI 报告要素）"
    ],
    "models": [
      {"name": "Ideal Reference Model（无七鳃鳗基线）", "type": "资源-物种离散 L-V 差分方程组（资源当猎物、物种当捕食者）", "assumptions": "全部物种直接从环境资源取能（假设3, p.5）；资源式 λ(t+1)−λ(t)=σλ−qλ²−Σμi λNi（eq1, p.7）；物种式 −aiNi 死亡 + biNiλ 取能 − piNi² 种内竞争（eq2, p.7）；q 视为常数，σ(t)/ai/bi/pi/μi 为随机变量但分布未给（p.8）", "validation": "初值 10 物种×240,000、资源 4.5×10^9 kJ，100 生殖轮仿真多组平均：资源 ~4.89×10^9 kJ、主要物种 ~8.88（2 优势 1 劣势 2 灭绝）（Fig 4, p.8）；定位为 '后续生态系统指标评估的参照'（p.6）", "pages": "eq1-3, p.7-8"},
      {"name": "Constant Sex Ratio Model（常规寄生种对照，2:1）", "type": "基线结构 + 寄生种 N 的出生-资源-寄生耦合", "assumptions": "焦点种性别比固定 2:1（m=0.67, p.12；Fig 12 图例即 'the parasite'——对照物种是常规寄生种而非关掉开关的七鳃鳗）；出生式 N(t+1)=k(1−m)^1.25 N(t)，ρ=1.25 由仿真选定、k 未给值（eq4, p.10）；s(t)=λ/(N+ΣNi) 在常性别比下影响小、暂忽略并预告下一模型起大作用（eq5, p.10）；竞争式加 βλN 资源消耗项（eq6, p.10）；寄生用改进 Nicholson-Bailey：1935 原型 eq7 → 密度 10^6 标度+logistic 修正 eq8 → 竞争/寄生双部分 γ 加权 eq9 → 出生+寄生综合 eq10（p.10-11）", "validation": "作为对照组在 §4 与 Changing Sex Ratio 并排跑（Fig 11, p.16；Fig 12 恶化实验, p.17）", "pages": "eq4-11, p.10-12"},
      {"name": "Models of Changing Sex Ratios（七鳃鳗处理组）", "type": "Constant Sex Ratio 结构 + m(s) 动态化（种群级资源→性别比桥）", "assumptions": "资源稀缺→偏雄、充足→趋 1:1（题面+文献[7], p.12）；端点标定：s→0 时 m→1、s=s0（资源过小生存线）时女:男=1:5 即 m=0.83；Logistic 型 m(s)=1/2+1/(2+e^{b̄(s−s0)})（eq12, p.12；形状参数 b̄ 未给值）；完整系统 eq13 七行（p.14）", "validation": "Fig 6 S 曲线自证（实线段=模型域 [0.50,0.83], p.13）；Fig 7 负反馈闭环图（p.13）；改造声明 'the sex ratio m is no longer a fixed value, but a variable'（p.14）", "pages": "eq12-13, p.12-14"},
      {"name": "ESI 熵权评估模型", "type": "评价类（两指标+熵权法打分）迁入连续题", "assumptions": "稳定性由总资源+存活物种数两指标决定（文献[8], p.14）；ESI=ω1·x̄+ω2·π̄1（eq14, p.18）；信息熵 Ej=−Σpij ln pij / ln n0（eq15, p.19）；权重由三模型多组仿真数据标准化后按信息冗余度反推（p.19）", "validation": "Table 1 三模型打分：存活物种 0.75/0.77/0.84、资源 0.55/0.38/0.45、稳定性 0.63/0.54/0.61 → 常规寄生种降稳（0.63→0.54）、七鳃鳗缓解（0.61）（p.19）", "pages": "p.14, 18-19"},
      {"name": "整合模型（Task 4：七鳃鳗+常规寄生虫同域）", "type": "10 物种系统（两条寄生链耦合）", "assumptions": "七鳃鳗宿主 3 种（i=5..7）、寄生虫宿主 2 种（i=8,9）、不被寄生 4 种（i=1..4）；寄生虫性别比 1:1（m10=1/2, p.20-21）；七鳃鳗走变性别比 m(s)、寄生虫走固定 m10（eq16）", "validation": "Fig 15：寄生虫与七鳃鳗周期波动、峰谷对应→相互制衡、负反馈放大；寄生虫曲线从'大幅不规则震荡'变为'固定周期与振幅'（p.21）", "pages": "eq16, p.20-21"}
    ],
    "figures": [
      {"id": "Fig 1", "page": "p.3", "claim": "七鳃鳗实物照片", "type": "照片", "self_evidence": "低——装饰性"},
      {"id": "Fig 2", "page": "p.4", "claim": "建模思路图：Others/Lamprey/Host/Environmental resource 四节点，蓝=L-V 直接影响、绿=N-B 直接影响、红=间接影响——双基础模型选型一图辩护", "type": "概念关系图（颜色编码）", "self_evidence": "高"},
      {"id": "Fig 3", "page": "p.7", "claim": "理想参考生态系统：资源自然增长+内部竞争，能量流向各物种、物种各自种内竞争", "type": "流程示意图", "self_evidence": "中-高"},
      {"id": "Fig 4", "page": "p.8", "claim": "基线仿真 100 轮：10 物种轨迹（蓝）+总资源（红右轴）；多组平均给出基线数字（资源 ~4.89×10^9 kJ、主要物种 ~8.88）", "type": "双轴多线时序", "self_evidence": "中"},
      {"id": "Fig 5", "page": "p.9", "claim": "常性别比生态系统反馈图：出生率(+)/死亡率(−)/个体资源获取(−)/种间关系(不确定)——三因素分解图化", "type": "反馈回路图", "self_evidence": "中"},
      {"id": "Fig 6", "page": "p.13", "claim": "m–s S 型下降曲线，标注 (s0, 0.83)；实线段=模型域（雄性占比 [0.50,0.83]）——桥函数 eq12 自证图", "type": "函数曲线图", "self_evidence": "高——桥函数核心图"},
      {"id": "Fig 7", "page": "p.13", "claim": "变性别比生态系统负反馈闭环：雄比例↔雌比例↔种群总量↔个体资源↔死亡率多环相扣", "type": "反馈回路图", "self_evidence": "高（机理叙事）"},
      {"id": "Fig 8", "page": "p.15", "claim": "100 实验组总资源对比：Ideal（黑）显著高于 Constant（红）/Changing（蓝）——寄生者消耗资源", "type": "三线对比（实验组序为横轴）", "self_evidence": "中-高"},
      {"id": "Fig 9", "page": "p.15", "claim": "100 实验组主要物种数（不含七鳃鳗）：Changing（红）> Constant（蓝）> Ideal（黑）——单图支撑 Q1 多样性结论", "type": "三线对比（实验组序为横轴）", "self_evidence": "中-高"},
      {"id": "Fig 10", "page": "p.16", "claim": "Changing Sex Ratio 模型 100 轮时序：资源/七鳃鳗/宿主/其他物种（双轴）", "type": "双轴多线时序", "self_evidence": "中——须与 Fig 11 并排对读"},
      {"id": "Fig 11", "page": "p.16", "claim": "Constant Sex Ratio 模型同式时序：其他物种普遍低于 Fig 10——常规寄生种压力更大", "type": "双轴多线时序", "self_evidence": "中"},
      {"id": "Fig 12", "page": "p.17", "claim": "Constant Sex Ratio + 环境恶化（σ(t) 方差放大）：资源与焦点种（图例 'the parasite'）剧烈震荡——Q2 对照侧证据", "type": "双轴多线时序", "self_evidence": "中-高"},
      {"id": "Fig 13", "page": "p.18", "claim": "Changing Sex Ratio + 环境恶化：资源仍大波动但七鳃鳗稳定 ~1×10^6——Q2 关键证据图", "type": "双轴多线时序", "self_evidence": "高"},
      {"id": "Fig 14", "page": "p.20", "claim": "仅寄生虫（性别比 1:1）+环境恶化：寄生虫与资源高度同步的不规则大幅震荡——无七鳃鳗基线", "type": "双轴多线时序", "self_evidence": "中-高"},
      {"id": "Fig 15", "page": "p.21", "claim": "七鳃鳗+寄生虫共存：两种群周期波动、峰谷对应——相互制衡、负反馈放大，寄生虫抗逆增强——Q4 关键证据图", "type": "双轴多线时序", "self_evidence": "高"},
      {"id": "Fig 16", "page": "p.22", "claim": "T0 时刻人类捕捞脉冲：种群骤降后快速恢复至捕捞前状态——抗扰性检验", "type": "双轴多线时序+事件标注", "self_evidence": "中-高"},
      {"id": "Fig 17", "page": "p.23", "claim": "初值扫描：初始规模增大时存活主要物种数稳于 ~9.2、总资源持续下降——泛化性检验", "type": "双轴双线（均值曲线）", "self_evidence": "中"}
    ],
    "checks": [
      "蒙特卡洛 ensemble 平均：系数为随机变量 → 实验随机均分组、逐组取平均（'divided these experiments into several groups randomly and evenly', p.15）；Fig 8/9 横轴即 100 个实验组（p.15）",
      "环境恶化应力测试：不引入新冲击，直接放大 eq11 中随机变量 σ(t) 的方差（Q2, p.17）；Q4 复用同一手法（p.19）——随机模型的恶化操作子",
      "ESI 熵权三模型对比（Table 1, p.19）：稳定性 0.63（Ideal）/0.54（Constant）/0.61（Changing）——Q3 的定量答案",
      "合理化分析三查（§5.1, p.22）：物种数趋稳（生态稳定性）、种群与资源同频同向波动（环境依赖）、寄生者相互制约动态平衡（自调节）——模型行为对表生态学原则，无实测数据的行为面检验",
      "敏感度①人类活动：T0 捕捞脉冲（Fig 16, p.22-23）→ 'did not collapse, but quickly recovered'（p.23）→ 抗扰可靠",
      "敏感度②初值扫描（Fig 17, p.23）→ 物种数稳于 ~9.2 → generalizability；合并结论：模型抗外部不确定、具普适性（p.23）",
      "缺项（诚实登记）：无收敛性/数值设置报告（rtol/atol/步长全篇未出现；求解为生殖轮差分迭代+随机项, p.7-14）；无参数账——k、b̄、γ、φi、ai/bi/pi/μi 均无数值（来源一句 'After experimentation with the computer software, the appropriate value of the correlation coefficient can be determined', p.8），仅 ρ=1.25 给值（p.10），且无参数汇总表（仅 Notations 表 p.6）；无实测对账（全文无模型 vs 真实种群数据对照图）；σ(t) 方差放大无量化倍数（p.17, p.19）；随机变量分布类型未给（p.8）；无平衡点/线性化稳定性分析（稳定性走 ESI 仿真评估路线）；符号滑移——Notations 表 n=initial/n1=final（p.6），p.14 却写 'the initial number of species in the ecosystem, n1, is 10'"
    ],
    "wordsmith": [
      {"quote": "However, win some, lose some. With higher resilience to environmental risk comes lower population size", "page": "p.1", "note": "摘要权衡句：俚语引出利弊对举——Task 2 结论一句话说两面"},
      {"quote": "the environmental resources can be regarded as the prey and each species as the predator", "page": "p.4", "note": "建模视角转换句：resources-as-prey 把竞争与捕食统一进 L-V——全文方法论枢纽"},
      {"quote": "the sex ratio m is no longer a fixed value, but a variable", "page": "p.14", "note": "模型改造声明句：改造点一句话钉死"},
      {"quote": "which may be the reason why the lamprey has been able to survive for 360 million years on the earth", "page": "p.18", "note": "结果升华句：模型输出接到深时生物学事实（3.6 亿年生存）——机理可信度的修辞加持"},
      {"quote": "after human fishing, the ecosystem did not collapse, but quickly recovered to the state before human fishing", "page": "p.23", "note": "敏感度结论句：扰动→未崩溃→快速恢复三段式，一句收抗扰检验"},
      {"quote": "Possible solution: Introduce advanced consumers while hierarchizing the model based on different trophic levels.", "page": "p.24", "note": "弱点配药方句式：每条 weakness 后跟 Possible solution——弱点节升档写法"},
      {"quote": "which is sufficient to reflect the doctrine of the mean of the lamprey to the ecosystem", "page": "p.24", "note": "首尾呼应句：Conclusion 重现题目 'Doctrine of the Mean'——利弊权衡上升为可记忆主题"},
      {"quote": "No AI tools were used in this article.", "page": "p.25", "note": "2024 首设 AI 使用报告：独立成节置于 References 后——参赛格式新要素"}
    ]
  },
  "distinct": "与 Wuhan 卡（2400996）对照后填写：本篇独有的是『三模型阶梯对照设计』——先建无七鳃鳗的 Ideal Reference Model 作基线（兼作后续评估参照, p.6），再加 Constant Sex Ratio（常规寄生种, m=0.67）与 Changing Sex Ratio（七鳃鳗, m(s)）两个处理模型，全部结论来自跨模型比较；Wuhan 的对照是单模型内的开关机制（同模型开/关 sex-ratio 调节），无基线生态系统。两个支撑件亦独有：① resources-as-prey 视角（资源当猎物, p.4）统一捕食与种间竞争——Wuhan 直接建物种间互作矩阵；② 改进 Nicholson-Bailey 寄生链（密度 10^6 标度, eq7→10, p.11）显式建寄生动力学，使 Q4 能直接耦合两种寄生者（eq16, p.20-21）——Wuhan 无寄生动力学、Q4 走 LV 矩阵扩展；③ 熵权法 ESI（评价类方法迁入连续题, p.18-19）——Wuhan 用自造 BDS/扰动方差指标。"
}
```

## 2. 同题 O-O 对比（vs 05_论文拆解/06_卡片_2024A_Wuhan.html，队伍 2400996）

1. **对照组的构造：模型阶梯 vs 机制开关**。XJTU 建三个完整模型——Ideal Reference（无七鳃鳗基线, p.6-8）→ Constant Sex Ratio（常规寄生种 m=0.67, p.8-12）→ Changing Sex Ratio（m(s), p.12-14），结论全部来自跨模型比较（Fig 8/9 三线并排, p.15；Fig 10/11 成对对读, p.16）；Wuhan 是同一模型开/关 sex-ratio 调节机制（控制组仅改性别概率、其余全同, Wuhan p.15-16），外加 K 砍半/恢复时间线（Wuhan Fig 10, p.16）。基线模型还兼任稳定性评估参照（p.6）——一份建模两处用。作答组织随之分流：XJTU 严格按题号 4.1→4.4 对应 Q1→Q4（p.14-21），Wuhan 按模型层级作答并显式写 'answer to the question X'（Wuhan p.17-21）。
2. **"环境→性别比"桥：种群级资源桥 vs 个体级生长年桥**。XJTU 用人均资源占有 s(t)（eq5, p.10）驱动 Logistic 型 m(s)=1/2+1/(2+e^{b̄(s−s0)})（eq12, p.12），端点由文献[7]钉死（s0 处女:男 1:5 → m=0.83, p.12）；Wuhan 用个体生物量阈值→变态生长年 x~N(xb,σ²)→P=1−e^{α+βx}（Wuhan eq11-16, p.11-12，bioenergetic 机理）。同一生物学事实（资源少偏雄）在两支 O 队落在不同标度：种群人均资源 vs 个体生长年——桥函数设计自由度的直接证据。
3. **寄生动力学显式与否决定 Q4 答法**。XJTU 走 N-B 链：1935 原型（eq7, p.11）→ 密度/logistic 修正（eq8）→ 竞争寄生 γ 混合（eq9）→ 出生+寄生综合（eq10），Q4 把七鳃鳗与 1:1 寄生虫放进同一 10 物种系统（eq16, p.20-21），得到峰谷对应的周期波动 = 负反馈放大（Fig 15, p.21）；Wuhan 未建寄生动力学，Q4 用六物种 LV 互作矩阵 + 寄生虫物种轨迹对照回答（Wuhan Fig 17/18, p.20）。要答"对其他物种（如寄生虫）的影响"，显式寄生链让机制叙事直接可读。
4. **稳定性评估机器：熵权打分 vs 自造扰动指标**。XJTU 引入评价类范式：ESI=ω1x̄+ω2π̄1（eq14, p.18）+ 熵权法定权（eq15, p.19），三模型标准化打分（Table 1: 0.63/0.54/0.61, p.19）；Wuhan 自造 BDS 三指标（B 总生物量 / D Shannon-Wiener / S 扰动均方差）+ 统一优化率 R（Wuhan eq17-21, p.13/16）。两篇都绕开平衡点线性化——A 题 O 论文的"稳定性"一致走实验/评估路线（02 模块 §1.3 的解析路线两条 O 都没用，第二例证）。
5. **摘要风格：零数字粗体断言 vs 三个百分数**。XJTU 摘要无一个数字，靠每问一段粗体结论句收束（p.1）；Wuhan 摘要 3 个百分数（73.3%/5.87%/5.90%, Wuhan p.1）。同题两 O 对照后，"摘要数字密度" heuristic 应校准为"可核查的具体论点"——粗体论点句是零数字摘要的替代承重结构。共同点也登记：两篇均无收敛性检验、均无实测对账、桥函数均自设——O 档的共同缺项。

### 对照后的跨卡裁决（回写 Wuhan 卡候选）

- Wuhan 卡 distinct 候选①（个体级迭代算法 Algorithm 1）③（统一优化率 R）对照后成立——XJTU 全篇种群级差分（t=生殖轮, p.6），无个体标签机制、无统一 R 指标。
- Wuhan 卡候选②（resilience/resistance 词汇对）**不成立**：XJTU 亦用该词汇（resilience p.1；resistance p.18/p.21/p.23）——应从 Wuhan 卡候选中移除。
- 两支 O 队的公共骨架（可视为连续题 O 档"最大公约数"）：基础模型改造留痕 + 对照实验 + 自造/引入评估指标 + 应力测试 + 敏感度两式（抗扰+泛化）。

## 3. 打法提炼（连续题特有动作）

1. **基线生态系统先行，一份建模两处用**（p.6-8）：先建 Ideal Reference Model（无七鳃鳗）跑出基线（资源 ~4.89×10^9 kJ、主要物种 ~8.88, Fig 4 p.8），既作影响比较的对照（Fig 8/9, p.15），又作稳定性评估的参照（p.6）——影响类问题的通用起手式：先有 reference 再谈 impact。
2. **resources-as-prey 视角转换**（p.4, p.6-7）：把环境资源当猎物、每个物种当捕食者，一个 L-V 结构同时覆盖资源-物种关系与（间接的）种间竞争——用视角换方程数，模型个数减一。
3. **自设桥函数的最小可信化配置：端点文献钉死 + 曲线画图自证**（p.12-13）：m(s) 形状参数 b̄ 虽未给值，但两端点有文献[7]背书（s→0 时 m→1；s0 处 m=0.83），且 Fig 6 把 S 曲线与模型域 [0.50,0.83] 画出来——自设函数至少要做到"端点有出处、形状有图"。
4. **基础模型改造留痕：原型→缺陷→修正→综合**（p.11）：N-B 1935 原型（eq7）→ 指出 'great fluctuation' 不适用（p.11）→ 密度 10^6 标度+logistic 修正（eq8）→ 与竞争模型 γ 混合（eq9）→ 与出生式综合（eq10）——评委能逐步跟随每个"为什么要改"，与 Wuhan 的 L-V 拆半式改造（Wuhan p.9）同构。
5. **随机模型的恶化操作子：放大已有随机项方差**（p.17, p.19）：环境恶化不外加新冲击，直接放大 eq11 中随机变量 σ(t) 的方差——对随机模型，应力测试的自然落点是调大环境不确定性；同一手法在 Q2/Q4 复用，保持实验可加性。
6. **无实测数据时的行为面检验：合理化分析三查**（p.22）：物种数趋稳（稳定性）、种群与资源同频波动（环境依赖）、寄生者相互制约动态平衡（自调节）——模型输出对表领域常识；这是没有对账数据时的降级检验路线（弱于实测对账，备赛时应优先补实测对账）。
7. **敏感度两问式：抗扰 + 泛化**（p.22-23）：T0 人类捕捞脉冲（Fig 16）测抗扰可靠性；初值扫描（Fig 17，物种数稳于 ~9.2）测泛化性——两个实验分别对准两个评价词（reliability/universality），摘要末段的检验声明由此落地。
8. **弱点配药方 + 首尾呼应主题句**（p.24, p.1）：每条 weakness 后跟 'Possible solution'（两条各配升级路线：加物种数、按营养级分层引入高级消费者）；Conclusion 重现题目 'Doctrine of the Mean'（p.24）——把利弊权衡上升为可记忆主题，题目-结论闭环。

**连续题打法骨架对照**（03_题型打法/A_连续 骨架 × 本文实测）：机理方程 ✓（留痕改造 eq7→10）、无量纲化 ✗、数值解 ✓（生殖轮差分+随机系数）、收敛检验 ✗、稳定性走仿真评估 ✓ / 解析型 ✗、敏感度 ✓（脉冲+初值）、优化 ✗（题面未要求）——与 Wuhan 卡实测完全同构：**O 档的检验可以"选对路线"而非"全做"**；本卡为该推断提供第二例证（两 O 同缺收敛检验与解析稳定性，仍双双 O）。

### 瑕疵清单（O 论文也有，反着学）

- 无参数账（最大攻击面）：k、b̄、γ、φi、ai/bi/pi/μi 等关键系数无数值，来源以一句 'After experimentation with the computer software...' 带过（p.8）；仅 ρ=1.25 给值（p.10）；无参数汇总表——对照 Wuhan 的 Table 3 十参数账（Wuhan p.15），可复现性差距明显
- 无收敛性/数值设置报告（rtol/atol/步长全篇未报；差分迭代, p.7-14）——两 O 共同缺项（02 模块 §4.1 死法）
- 无实测对账：全文无模型 vs 真实种群数据对照图
- σ(t) 方差放大量无倍数、随机变量分布类型未给（p.8, p.17, p.19）
- 符号滑移：Notations 表 n=initial/n1=final（p.6），p.14 却以 n1 作 initial 使用
- 语言/排版：Fig 5 注释 'negativelylly'（p.9）；§5.1 'between th lampreys'（p.22）；'Figure 8and Figure 9' 空格缺失（p.15）
- 摘要零数字（p.1）——风格选择而非错误，但与"摘要数字密度"信号相悖，需按 §2 第 5 条重新校准该 heuristic

## 4. 自查（代理产出，待站长复核）

- 页码逐条核过（PDF 25 页 = 印刷页 Page X of 25，逐页渲染图对照；eq1-16 / Fig1-17 / Table1 / Notations 表锚点逐一登记）
- 无臆测：缺项与瑕疵逐处给页码；引用均 ≤25 词；报数（4.89×10^9 kJ / 8.88 / 0.63-0.54-0.61 / 1×10^6 / 2×10^6 / 9.2 / 240,000 / ρ=1.25）均为论文原文数字，无原始随机数可复算故未复算、无一处脑补数值
- distinct 已与 Wuhan 卡对照后填写，并反向裁决 Wuhan 卡三候选（①③成立、②不成立）；两处跨卡推断（公共骨架 / 数字密度校准）已标注为拆解者结论
