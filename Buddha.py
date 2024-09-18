import streamlit as st
import requests

st.set_page_config(page_title="佛法修行", layout="wide")
st.title("佛法修行")

def main():
    # Sidebar
    st.sidebar.title("修行內容")
    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"無法獲取文件內容。錯誤：{str(e)}"

def display_hui_xiang_ji():
    url = "https://raw.githubusercontent.com/jasonckb/Buddha/main/%E5%9B%9E%E5%90%91%E5%81%88.txt"
    content = fetch_content(url)
    
    st.header("迴向偈")
    st.write(content)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

if __name__ == "__main__":
    main()
