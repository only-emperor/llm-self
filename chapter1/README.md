# 📄 PDF 文档问答助手

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square\&logo=streamlit\&logoColor=white)

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

一个基于 Python + Streamlit + LLM API 的 PDF 文档问答工具，支持上传 PDF 文件，并根据文档内容进行智能问答。

---

## ✨ 项目简介

本项目实现了一个轻量级的 **PDF 文档问答助手**。

用户可以上传 PDF 文件，系统会自动提取文本内容，并结合大语言模型对用户问题进行回答。

该项目适合作为 **LLM 入门项目**、**RAG Demo** 或 **GitHub 作品集项目** 展示。

---

## ✨ 核心功能

- 📤 支持上传 PDF 文件

- 📝 自动提取文档文本

- 🔍 简单内容检索

- 🤖 调用大模型生成回答

- 🌐 提供简洁的网页交互界面

- 📎 适合作为 LLM 应用入门项目

---

## 🧠 工作流程

Unable to render rich display

Lexical error on line 3. Unrecognized text.
flowchart LR&ﬂ°x20¶ß A\[Upload P
--------------^

For more information, see https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams

flowchart LR

&#x20;   A\[Upload PDF] --> B\[Extract Text]

&#x20;   B --> C\[Split Text]

&#x20;   C --> D\[Retrieve Relevant Chunks]

&#x20;   D --> E\[LLM Generates Answer]

&#x20;   E --> F\[Display Response]

---

## 🛠️ 技术栈

- **Python**

- **Streamlit**

- **pypdf**

- **python-dotenv**

- **OpenAI 兼容接口**

- **DeepSeek / OpenAI / 其他兼容模型服务**

---

## 🚀 快速开始

### 1. 克隆项目

git clone https://github.com/你的用户名/你的仓库名.git

cd 你的仓库名
### 2. 创建虚拟环境

python -m venv venv
### 3. 激活虚拟环境

**Windows:**

venv\\Scripts\\activate
**Mac / Linux:**

source venv/bin/activate
### 4. 安装依赖

pip install -r requirements.txt
### 5. 配置环境变量

在项目根目录创建 .env 文件，并填写你的配置：

OPENAI\_API\_KEY=your\_api\_key\_here

OPENAI\_BASE\_URL=https://api.deepseek.com

MODEL\_NAME=deepseek-chat
注意：.env 不要上传到 GitHub。

建议保留一个 .env.example 作为示例文件。

### 6. 启动项目

python -m streamlit run app.py
---

## 🔐 环境变量说明

| 变量名 | 说明 | 示例 |

|-------|------|------|

| OPENAI\_API\_KEY | API Key | your\_api\_key\_here |

| OPENAI\_BASE\_URL | 模型服务地址 | https://api.deepseek.com |

| MODEL\_NAME | 模型名称 | deepseek-chat |

---

## 💬 使用示例

**问题：** 这份文档主要讲什么？

**回答：** 该文档主要介绍了……

**问题：** 文档中提到了哪些关键概念？

**回答：** 文档中提到的关键概念包括……

---

## 📁 项目结构

pdf-qa-assistant/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── .env.example

└── venv/
---

## 🌱 后续优化

- 支持更多文件格式，如 TXT、DOCX

- 增加回答来源引用

- 增加多轮对话能力

- 支持回答历史记录

- 改进检索逻辑，提升回答准确率

- 支持部署到云平台

---

## 📌 适合简历的写法

- 基于 Python 和 Streamlit 开发 PDF 文档问答系统，支持文件上传、文本提取和自然语言提问

- 结合大模型接口实现智能问答功能，提升文档信息检索效率

- 独立完成项目开发、README 编写与 GitHub 部署

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

感谢开源社区和相关工具库对本项目的支持。
