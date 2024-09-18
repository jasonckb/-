import streamlit as st
import requests
import io
from docx import Document

def main():
    st.set_page_config(page_title="佛法修行", layout="wide")
    st.title("佛法修行")

    # Sidebar
    st.sidebar.title("修行內容")

    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()

def fetch_docx_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        doc = Document(io.BytesIO(response.content))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    else:
        return "無法獲取文件內容。請檢查網絡連接或文件鏈接。"

def display_hui_xiang_ji():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%9B%9E%E5%90%91%E5%81%88.docx"
    content = fetch_docx_content(url)
    
    st.header("迴向偈")
    st.write(content)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

if __name__ == "__main__":
    main()
