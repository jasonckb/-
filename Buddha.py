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
        display_diamond_sutra()

def fetch_docx_content(url, convert=False):
    try:
        st.write(f"Fetching content from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        doc = Document(io.BytesIO(response.content))
        full_text = []
        for para in doc.paragraphs:
            text = para.text
            if convert:
                text = cc.convert(text)  # Convert to traditional Chinese if needed
            full_text.append(text)
        content = '\n'.join(full_text)
        st.write(f"Fetched content (first 100 characters): {content[:100]}...")
        return content
    except requests.exceptions.RequestException as e:
        st.error(f"無法獲取文件內容。錯誤：{str(e)}")
        return ""
    except Exception as e:
        st.error(f"處理文件時出錯。錯誤：{str(e)}")
        return ""


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

def process_diamond_sutra_content(content):
    lines = content.split('\n')
    formatted_content = '<div class="diamond-sutra">'
    current_quote = ""
    current_explanation = ""
    in_quote = True

    for line in lines:
        line = line.strip()
        if line.startswith(('1.', '2.', '3.', '4.', '5.')):
            if current_quote or current_explanation:
                formatted_content += format_quote_and_explanation(current_quote, current_explanation)
            current_quote = line
            current_explanation = ""
            in_quote = True
        elif line:
            if in_quote:
                current_quote += " " + line
                in_quote = False
            else:
                current_explanation += line + "<br>"
        else:
            in_quote = True

    # Add the last quote and explanation
    if current_quote or current_explanation:
        formatted_content += format_quote_and_explanation(current_quote, current_explanation)

    formatted_content += '</div>'
    return formatted_content

def format_quote_and_explanation(quote, explanation):
    formatted = '<div class="sutra-item">'
    formatted += f'<div class="quote">{quote}</div>'
    if explanation:
        formatted += f'<div class="explanation">{explanation}</div>'
    formatted += '</div>'
    return formatted

def display_diamond_sutra():
    st.header("金剛經精句")
    
    # Custom CSS for the diamond sutra display
    st.markdown("""
    <style>
    .diamond-sutra {
        font-size: 18px;
        line-height: 1.6;
    }
    .diamond-sutra .sutra-item {
        margin-bottom: 30px;
    }
    .diamond-sutra .quote {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
        text-decoration: underline;
        text-underline-offset: 5px;
    }
    .diamond-sutra .explanation {
        font-size: 18px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display content from 金剛經精句.docx file
    url = "https://github.com/jasonckb/Buddha/raw/main/%E9%87%91%E5%89%9B%E7%B6%93%E7%B2%BE%E5%8F%A5.docx"
    content = fetch_docx_content(url)
    
    if content:
        # Process and format the content
        formatted_content = process_diamond_sutra_content(content)
        st.markdown(formatted_content, unsafe_allow_html=True)
    else:
        st.error("無法顯示金剛經內容。請檢查網絡連接或文件鏈接。")
    
    # Button for 經文及翻譯
    if st.button("經文及翻譯"):
        display_diamond_sutra_translation()
    
    # Display source
    st.write("來源：")
    st.markdown("[金剛經 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle335)")


if __name__ == "__main__":
    main()
