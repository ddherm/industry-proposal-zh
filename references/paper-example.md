# 论文插图实例 · 轴承振动信号的掩码自监督重建

[期刊原图 PNG](../assets/论文框架图示例.png) 可用于讨论设备时序信号中缺少故障标注时如何训练编码器，也可作为选取技术网络图的实例。若项目采用其他预训练目标，应另选与方法相符的图。

## 原图定位

Pengping Luo、Zhiwei Liu，*Unsupervised Bearing Fault Diagnosis Using Masked Self-Supervised Learning and Swin Transformer*，*Machines*，2025 年，第 13 卷第 9 期，文章号 792。第 2 节 Methodology，PDF 第 4 页，图 2。论文版权声明为 © 2025 两位作者，许可为 CC BY 4.0。图题和图内未另列第三方权利人。素材直接取自期刊的独立 PNG，保留全图和原有标注。[论文原文](https://doi.org/10.3390/machines13090792) · [期刊原图](https://mdpi-res.com/machines/machines-13-00792/article_deploy/html/images/machines-13-00792-g002.png) · [许可](https://creativecommons.org/licenses/by/4.0/)

## 在本子里怎么写

**图前示例**　Luo 和 Liu 利用正常轴承的振动信号训练自编码器。训练时遮蔽部分输入，让模型根据可见的采样点重建信号。图中上半部分给出遮蔽后的输入与重建结果，红色箭头表示编码器的隐层特征传入下方的 Swin Transformer 模块。[原文第 2 节](https://www.mdpi.com/2075-1702/13/9/792#sec2-machines-13-00792)

**可用图注**　图 X　轴承振动信号的掩码重建与特征处理网络。引自 Pengping Luo、Zhiwei Liu（2025），*Machines* 13(9)，792，图 2，第 4 页。© 2025 作者，按 CC BY 4.0 转载，原图未改动。[原文](https://doi.org/10.3390/machines13090792) · [许可](https://creativecommons.org/licenses/by/4.0/)

**图后承接**　若用于光时域反射仪（OTDR）项目，应交代两类信号的差别。原图横轴是振动信号的采样时间步，OTDR 单条曲线通常按沿纤距离解释反射事件。只在项目确有相应设计时，接着说明拟遮蔽哪些区段、如何处理反射峰、用哪些线路的曲线检验迁移效果。项目自身的样本组织、训练输出与验证数据另在可编辑路线图中交代。论文报告的轴承试验成绩只适用于其试验条件。

置入 Word 或 PPT 时以文内顺序替换 X，把署名、出处和许可放在图下。若译注、局部裁切或重绘，保留作者和链接，并把「原图未改动」替换为实际改动说明。
