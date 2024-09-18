import streamlit as st
import requests
import io
from docx import Document

st.set_page_config(page_title="佛法修行", layout="wide")

# Custom CSS for the golden yellow text
st.markdown("""
    <style>
    .golden-text {
        font-size: 24px;
        font-weight: bold;
        color: #e0be02;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("佛法修行")

# Adding the text in large, bold, golden yellow font
st.markdown("""
    <p class="golden-text">
    願以此功德，莊嚴佛淨土，<br>
    上報四重恩，下濟三途苦。<br>
    若有見聞者，悉發菩提心，<br>
    盡此一報身，同生極樂國。
    </p>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    st.sidebar.title("修行內容")
    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()

def fetch_docx_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        doc = Document(io.BytesIO(response.content))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except requests.exceptions.RequestException as e:
        return f"無法獲取文件內容。錯誤：{str(e)}"
    except Exception as e:
        return f"處理文件時出錯。錯誤：{str(e)}"

def display_hui_xiang_ji():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%9B%9E%E5%90%91%E5%81%88.docx"
    content = fetch_docx_content(url)
    
    st.header("迴向偈")
    st.write(content)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

if __name__ == "__main__":
    main()
