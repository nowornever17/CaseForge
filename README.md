# 城市设计案例研究助手

> AI 驱动的学术案例文献精华提取工具 · v1.2

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![API](https://img.shields.io/badge/API-5%20providers-green)]()

## ✨ 功能

- 🔍 **自动提取三维度精华** — 背景与冲突 / 关键决策 / 经验教训
- 🌐 **学术搜索** — Semantic Scholar 英文文献搜索 + AI 批量摘要
- 🤖 **5 家 AI API** — DeepSeek / 智谱(免费) / 通义 / Moonshot(Kimi) / 文心
- 📦 **降级保护** — API 失败自动切本地 TF-IDF，不中断工作流
- 💾 **双格式输出** — Markdown + JSON
- ⚡ **去重缓存** — 同一篇文章不重复调用 API
- 🎬 **Demo 开箱即用** — `demo_xixi.py` 西溪湿地案例一秒体验

## 🚀 快速开始

```bash
pip install -r requirements.txt
cp config.example.py config.py    # 填入任意一家 API Key
python main.py                    # 交互式菜单
python main.py --demo             # 演示模式
python main.py --api zhipu        # 切换免费智谱
```

## 📁 项目结构

```
├── main.py              # 入口 + CLI
├── api_client.py        # AI API 调用（可切换 5 家供应商）
├── search.py            # Semantic Scholar + 网页抓取
├── cache.py             # 去重缓存
├── formatter.py         # 格式化 + 保存
├── case_extractor.py    # TF-IDF 降级方案 + 向后兼容
├── config.example.py    # 配置模板（不含真实 Key）
├── demo_xixi.py         # 西溪湿地演示
├── prompts/
│   └── extract.md       # AI Prompt 模板（可独立编辑）
└── requirements.txt     # Python 依赖
```

## 🛠 CLI 命令

```bash
python main.py --help           # 帮助
python main.py --list-apis      # 列出所有 API
python main.py --api <name>     # 切换 API 供应商
python main.py --tfidf          # 强制本地 TF-IDF
python main.py --demo           # 西溪湿地演示
```

## 🤝 贡献

欢迎提 Issue 和 PR。本项目在使用中不断迭代，路线图见 [PROJECT.md](./PROJECT.md)。
