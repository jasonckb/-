import streamlit as st
import requests

def main():
    st.set_page_config(page_title="佛法修行", layout="wide")
    st.title("佛法修行")

    # Sidebar
    st.sidebar.title("修行内容")

    # 回向 section
    st.sidebar.header("回向")
    if st.sidebar.button("回向偈"):
        display_hui_xiang_ji()

def display_hui_xiang_ji():
    # In a real application, you would fetch the content from the GitHub link
    # For now, we'll use a placeholder text
    hui_xiang_ji_text = """
    愿以此功德，庄严佛净土。
    上报四重恩，下济三途苦。
    若有见闻者，悉发菩提心。
    尽此一报身，同生极乐国。
    """
    
    st.header("回向偈")
    st.write(hui_xiang_ji_text)
    
    st.write("更多信息：")
    st.markdown("[回向偈 - 星云大师著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

if __name__ == "__main__":
    main()
