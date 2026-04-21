import os
import re

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

st.set_page_config(page_title="PDF 文档问答助手", page_icon="📄", layout="wide")


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    base_url = os.getenv("OPENAI_BASE_URL")
    kwargs = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url

    return OpenAI(**kwargs)


def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    texts = []

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        if page_text.strip():
            texts.append(f"[第 {i + 1} 页]\n{page_text}")

    return "\n\n".join(texts)


def split_text(text, chunk_size=1000, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])

        if end == len(text):
            break

        start = end - overlap

    return chunks


def tokenize(text):
    return re.findall(r"[\u4e00-\u9fff]|[A-Za-z0-9]+", text.lower())


def retrieve_relevant_chunks(chunks, question, top_k=3):
    q_tokens = set(tokenize(question))
    if not q_tokens:
        return chunks[:top_k]

    scored_chunks = []

    for chunk in chunks:
        c_tokens = set(tokenize(chunk))
        score = len(q_tokens & c_tokens)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    selected = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]
    return selected if selected else chunks[:top_k]


def ask_llm(question, context):
    client = get_client()
    if client is None:
        return "未配置 OPENAI_API_KEY，请先在 .env 文件中填写 API Key。"

    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

    messages = [
        {
            "role": "system",
            "content": "你是一个严谨的文档问答助手。请只根据给定上下文回答问题；如果上下文没有答案，请直接说“文档中没有找到相关信息”。",
        },
        {
            "role": "user",
            "content": f"""下面是文档上下文：

{context}

请回答这个问题：
{question}
""",
        },
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()


def main():
    st.title("📄 PDF 文档问答助手")
    st.write("上传 PDF，然后输入问题，系统会根据文档内容回答。")

    st.caption("提示：这个版本适合初学者，先跑通项目。PDF 如果是扫描图片，可能提取不到文字。")

    uploaded_file = st.file_uploader("上传 PDF 文件", type=["pdf"])

    if uploaded_file is not None:
        with st.spinner("正在提取 PDF 文本..."):
            pdf_text = extract_pdf_text(uploaded_file)

        if not pdf_text.strip():
            st.error("没有提取到文本。请确认这是可复制文本的 PDF，而不是扫描图片版 PDF。")
            return

        st.success(f"文本提取成功，共 {len(pdf_text)} 个字符。")

        with st.expander("查看提取到的文本"):
            st.write(pdf_text[:5000] + ("..." if len(pdf_text) > 5000 else ""))

        question = st.text_input("请输入你的问题", placeholder="例如：这份文档主要讲了什么？")

        if st.button("提问"):
            if not question.strip():
                st.warning("请输入问题后再提问。")
                return

            with st.spinner("正在检索内容并生成回答..."):
                chunks = split_text(pdf_text)
                relevant_chunks = retrieve_relevant_chunks(chunks, question, top_k=3)
                context = "\n\n".join(relevant_chunks)
                answer = ask_llm(question, context)

            st.subheader("回答")
            st.write(answer)

            with st.expander("查看检索到的相关内容"):
                st.write(context)

    else:
        st.info("请先上传一个 PDF 文件。")


if __name__ == "__main__":
    main()