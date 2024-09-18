import streamlit as st

def main():
    st.set_page_config(page_title="佛法修行", layout="wide")
    st.title("佛法修行")

    # Sidebar
    st.sidebar.title("修行內容")

    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()

def display_hui_xiang_ji():
    hui_xiang_ji_text = """
    願以此功德，莊嚴佛淨土。
    上報四重恩，下濟三途苦。
    若有見聞者，悉發菩提心。
    盡此一報身，同生極樂國。
    """
    
    st.header("迴向偈")
    st.write(hui_xiang_ji_text)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

if __name__ == "__main__":
    main()
