import streamlit as st

# --- 웹페이지 기본 설정 (제목) ---
st.set_page_config(page_title="간단 계산기", layout="centered")

st.title("간단 계산기 🧮")

# --- CSS 스타일 적용 (계산기 모양) ---
# 기존 HTML/CSS 디자인을 Streamlit에서도 사용하고 싶다면 st.markdown을 사용합니다.
st.markdown("""
<style>
/* CSS 영역 */
.calculator {
    width: 300px; /* 여기서 300px 같은 단위 사용 가능 */
    margin: 50px auto;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    background-color: #f0f0f0;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# --- 계산기 기능 구현 ---
# 1. 숫자 입력 위젯
st.subheader("숫자를 입력해 주세요")

# session_state를 사용하여 값 유지
if 'num1' not in st.session_state:
    st.session_state['num1'] = 0
if 'num2' not in st.session_state:
    st.session_state['num2'] = 0
if 'result' not in st.session_state:
    st.session_state['result'] = 0

num1 = st.number_input("첫 번째 숫자:", value=st.session_state['num1'], step=1)
num2 = st.number_input("두 번째 숫자:", value=st.session_state['num2'], step=1)
st.session_state['num1'] = num1
st.session_state['num2'] = num2


# 2. 연산 버튼
col1, col2, col3, col4 = st.columns(4)
operation = None

with col1:
    if st.button("+"):
        operation = '+'
with col2:
    if st.button("-"):
        operation = '-'
with col3:
    if st.button("×"):
        operation = '*'
with col4:
    if st.button("÷"):
        operation = '/'

# 3. 계산 로직
if operation:
    try:
        if operation == '+':
            st.session_state['result'] = num1 + num2
        elif operation == '-':
            st.session_state['result'] = num1 - num2
        elif operation == '*':
            st.session_state['result'] = num1 * num2
        elif operation == '/':
            if num2 != 0:
                st.session_state['result'] = num1 / num2
            else:
                st.error("0으로 나눌 수 없습니다.")
                st.session_state['result'] = "오류"
    except Exception as e:
        st.error(f"계산 중 오류 발생: {e}")

# --- 결과 출력 ---
st.subheader("결과")
st.code(f"{st.session_state['result']}")
