import streamlit as st
import requests
import io
from docx import Document
from PIL import Image
from opencc import OpenCC

st.set_page_config(page_title="佛法修行 - Jason Chan", layout="wide")

# Initialize OpenCC converter
cc = OpenCC('s2t')  # Simplified to Traditional

# Custom CSS for the golden yellow text, responsive video, and larger content text
st.markdown("""
    <style>
    .golden-text {
        font-size: 24px;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
    }
    .video-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
        overflow: hidden;
    }
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .large-content {
        font-size: 20px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("佛法修行 - Jason Chan")

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
    st.title("佛法修行")

    # Sidebar
    st.sidebar.title("修行內容")
    
    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()
    
    # 持咒 section
    st.sidebar.header("持咒")
    if st.sidebar.button("藥師咒"):
        display_medicine_buddha_mantra()
    if st.sidebar.button("大悲咒"):
        display_great_compassion_mantra()
    
    # 三想破瓦法 section
    st.sidebar.header("三想破瓦法")
    if st.sidebar.button("破瓦法"):
        display_phowa_practice()
    
    # 佛經 section
    st.sidebar.header("佛經")
    if st.sidebar.button("金剛經"):
        st.session_state.show_translation = False
        display_diamond_sutra()

    if st.session_state.show_translation:
        display_diamond_sutra_translation()

    # Debug information
    st.sidebar.write("Debug Info:")
    st.sidebar.write(f"show_translation: {st.session_state.show_translation}")

def fetch_txt_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.error(f"Error fetching content: {str(e)}")
        return None

def display_hui_xiang_ji():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%9B%9E%E5%90%91%E5%81%88.docx"
    content = fetch_docx_content(url)
    
    st.header("迴向偈")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

def display_medicine_buddha_mantra():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E8%97%A5%E5%B8%AB%E5%92%92.docx"
    content = fetch_docx_content(url)
    
    st.header("藥師咒")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("藥師咒影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/5UnbgjkbgUI?start=1218&end=1242" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("影片來源：")
    st.markdown("[藥師咒 - YouTube](https://www.youtube.com/watch?v=5UnbgjkbgUI&t=1218s)")

def display_great_compassion_mantra():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%A4%A7%E6%82%B2%E5%92%92.docx"
    content = fetch_docx_content(url)
    
    st.header("大悲咒")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("大悲咒影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/Hr9zmoDWppA?start=0&end=162" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("影片來源：")
    st.markdown("[大悲咒 - YouTube](https://www.youtube.com/watch?v=Hr9zmoDWppA)")

def display_phowa_practice():
    st.header("三想破瓦法")
    
    # Display image
    image_url = "https://github.com/jasonckb/Buddha/raw/main/%E4%B8%89%E6%83%B3%E7%A0%B4%E7%93%A6%E6%B3%95.jpg"
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    st.image(img, use_column_width=True)
    
    # Display content from docx file
    url = "https://github.com/jasonckb/Buddha/raw/main/%E4%B8%89%E6%83%B3%E7%A0%B4%E7%93%A6%E6%B3%95.docx"
    content = fetch_docx_content(url)
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    # Display source
    st.write("文字來源：")
    st.markdown("[三想破瓦法 - 佛教在線](http://read.goodweb.net.cn/news/news_view.asp?newsid=74024)")
    
    # Display video
    st.write("破瓦法影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/wDVoBVC5s2c?start=536&end=2375" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    # Display video source
    st.write("影片來源：")
    st.markdown("[破瓦法 - YouTube](https://www.youtube.com/watch?v=wDVoBVC5s2c&t=1072s)")

# Diamond Sutra Functions
def parse_diamond_sutra_content(content):
    if not content:
        return []
    sections = content.split('##')[1:]
    parsed_content = []
    for section in sections:
        parts = section.split('---')
        if len(parts) == 2:
            quote = parts[0].strip()
            explanation = parts[1].strip()
            parsed_content.append((quote, explanation))
    return parsed_content

def parse_diamond_sutra_translation(content):
    if not content:
        return []
    chapters = content.split('###')[1:]
    parsed_content = []
    for chapter in chapters:
        chapter_parts = chapter.strip().split('\n\n')
        chapter_title = chapter_parts[0].strip()
        sections = []
        for part in chapter_parts[1:]:
            if part.startswith('##'):
                quote, explanation = part.split('---')
                sections.append((quote.replace('##', '').strip(), explanation.strip()))
        parsed_content.append((chapter_title, sections))
    return parsed_content

def display_diamond_sutra():
    st.header("金剛經精句")
    
    url = "https://raw.githubusercontent.com/jasonckb/Buddha/main/%E9%87%91%E5%89%9B%E7%B6%93%E7%B2%BE%E5%8F%A5.txt"
    content = fetch_txt_content(url)
    
    if content:
        try:
            parsed_content = parse_diamond_sutra_content(content)
            for quote, explanation in parsed_content:
                st.markdown(f"**{quote}**")
                st.write(explanation)
                st.write("---")
        except Exception as e:
            st.error(f"Error parsing content: {str(e)}")
    else:
        st.error("無法顯示金剛經內容。請檢查網絡連接或文件鏈接。")
    
    if st.button("經文及翻譯", key="translation_button"):
        st.session_state.show_translation = True
        st.experimental_rerun()

def display_diamond_sutra_translation():
    st.header("金剛經經文及翻譯")
    
    url = "https://raw.githubusercontent.com/jasonckb/Buddha/main/%E9%87%91%E5%89%9B%E7%B6%93%E5%8E%9F%E5%85%B8%E8%88%87%E7%99%BD%E8%A9%B1%E8%AD%AF%E9%87%8B.txt"
    content = fetch_txt_content(url)
    
    if content:
        try:
            parsed_content = parse_diamond_sutra_translation(content)
            for chapter_title, sections in parsed_content:
                st.subheader(chapter_title)
                for quote, explanation in sections:
                    st.markdown(f"**{quote}**")
                    st.write(explanation)
                    st.write("---")
        except Exception as e:
            st.error(f"Error parsing content: {str(e)}")
    else:
        st.error("無法顯示金剛經經文及翻譯。請檢查網絡連接或文件鏈接。")

if __name__ == "__main__":
    main()
