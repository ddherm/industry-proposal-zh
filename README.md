# 企业横向项目本子

用于编写企业委托研发项目的可研、技术方案和技术标，随附可编辑 PowerPoint 技术路线母版、场景图实例、论文网络图及引用说明。

技能入口为 [SKILL.md](SKILL.md)。在对话中调用 `$industry-proposal-zh`，并提供本项目的指南、需求、既有文稿或章节要求。

## 新范本怎么上传

**在这台电脑上最省事。** 把新的 Word、PDF 或 PPT 放到 `E:\项目工作\优质本子\industry-proposal-zh\templates\inbox`，然后在对话里说明文件名和希望学习的地方。例如：

> 将 templates/inbox 里新加的冷链监测可研蒸馏进 industry-proposal-zh。重点学习业务背景、技术路线图和图文衔接，更新 GitHub 仓库，并同步本机已安装的 skill。

**在 GitHub 网页上上传。** 打开 [新范本待处理目录](templates/inbox)，点击 **Add file → Upload files**，拖入文件，填上文件名和版本信息后点击 **Commit changes**。随后把仓库链接和新文件名发到对话中，说明希望吸收的章节或图。详细操作见 [待处理目录说明](templates/inbox/README.md)。[GitHub 上传说明](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository?platform=windows)

上传后继续执行一次蒸馏更新，才能把新范本中的写法加入技能。需要查看已经吸收了哪些范本，可读 [范本目录](templates/catalog.md)。

## 更新会做什么

从新材料中核对章节、代表性段落、图表和上下游关系，提炼适用的写作决定。通用规则进入 [技能入口](SKILL.md)，具体写法和图文实例进入 [写作参考](references/proposal-writing.md) 与相应图示说明。可复用图模板放到 `assets`，按原生形状继续编辑。一次更新完成后，将说明和资产一并提交 GitHub，并按本次要求同步本机技能。具体做法见 [范本更新流程](references/template-updates.md)。

## 随附材料

| 材料 | 用途 |
| --- | --- |
| [范本与写作示例](references/proposal-writing.md) | 四份初始范本的章、图、表定位，研究任务与验收写法 |
| [技术路线母版](assets/技术路线图母版.pptx) | 由 OTDR 路线页直接改成的原生可编辑 PPT |
| [母版使用方法](references/route-map.md) | 根据实际依赖增删节点、导出并插入正文 |
| [场景与论文配图](references/figures.md) | 生图、裁图、图前图后衔接 |
| [论文图实例及出处](references/paper-example.md) | 原图定位、图注与 CC BY 4.0 许可 |
| [PDF 裁图脚本](scripts/crop_paper_figure.py) | 从可见 PDF 页面按比例坐标导出选定区域 |

论文图的署名和许可随资产保留。新项目的指标、实绩和试点情况依据本项目材料填写。
