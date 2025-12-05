import streamlit as st

# --- 1. 웹페이지 기본 설정 ---
st.set_page_config(page_title="완벽한 계산기", layout="centered")

# --- 2. CSS 스타일 적용 (일반 계산기 모양 구현) ---
st.markdown("""
<style>
/* Streamlit 기본 스타일 숨기기 (필요한 경우) */
header {visibility: hidden;}
footer {visibility: hidden;}

/* 전체 계산기 컨테이너 스타일 */
.calculator-container {
    max-width: 340px; /* 계산기 최대 너비 */
    margin: 30px auto;
    padding: 15px;
    border-radius: 10px;
    background-color: #333333; /* 계산기 배경 */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
}

/* 결과 출력 화면 (Streamlit의 텍스트 입력 위젯을 활용) */
.stTextInput > div > div > input {
    font-size: 2.5em !important;
    text-align: right;
    height: 70px;
    background-color: #f0f0f0 !important; /* 디스플레이 배경 */
    color: #333333 !important;
    border-radius: 5px;
    border: none;
    padding: 10px;
}

/* 버튼 컨테이너 (Streamlit 컬럼의 간격을 조정) */
div[data-testid="stHorizontalBlock"] {
    gap: 8px; /* 버튼 사이 간격 */
}

/* 모든 버튼 기본 스타일 */
div.stButton > button:first-child {
    width: 100%;
    height: 60px;
    border-radius: 5px;
    font-size: 1.5em;
    border: none;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: background-color 0.1s;
    color: white; 
}

/* 숫자 및 특수 버튼 (0
