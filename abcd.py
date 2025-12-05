import streamlit as st

# --- 1. 웹페이지 기본 설정 (제목) ---
st.set_page_config(page_title="간단 계산기", layout="centered")

st.title("간단 계산기 🧮")

# --- 2. CSS 스타일 적용 (원래 디자인 요소를 위해 확보) ---
# 이 영역 안에 원래 HTML 파일에 있던 CSS 코드를 넣으시면 디자인이 적용됩니다.
st.markdown("""
<style>
/* 📢 여기에 원하는 CSS 코드를 추가하세요. */
/* 예시: 계산기 전체 컨테이너 스타일 */
.calculator {
    width: 300px; 
    margin: 50px auto;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    background-color: #f0f0f0;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
/* Streamlit 버튼 스타일링 예시 (원래 CSS에 버튼 디자인이 있다면 넣어주세요) */
div.stButton > button:first-child {
    width: 100%;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)


# --- 3. 상태 저장 초기화 (숫자 및 결과 값 유지) ---
if 'num1' not in st.session_state:
    st.session_state['num1'] = 0.0
if 'num2' not in st.session_state:
    st.session_state['num2'] = 0.0
if 'result' not in st.session_state:
    st.session_state['result'] = 0.0


# --- 4. 숫자 입력 위젯 ---
st.subheader("숫자를 입력해 주세요")

# 소수점 계산을 위해 기본값을 0.0으로 설정했습니다.
num1 = st.number_input("첫 번째 숫자:", value=st.session_state['num1'], step=0.1, key='input_num1')
num2 = st.number_input("두 번째 숫자:", value=st.session_state['num2'], step=0.1, key='input_num2')


# --- 5. 연산 버튼 및 로직 ---
col1, col2, col3, col4 = st.columns(4)
operation = None

with col1:
    if st.button("➕"):
        operation = '+'
with col2:
    if st.button("➖"):
        operation = '-'
with col3:
    if st.button("✖️"):
        operation = '*'
with col4:
    if st.button("➗"):
        operation = '/'
        
# '초기화' 버튼
if st.button("초기화 (C)"):
    st.session_state['num1'] = 0.0
    st.session_state['num2'] = 0.0
    st.session_state['result'] = 0.0
    st.rerun() # 앱을 다시 실행하여 초기화된 값을 반영합니다.


# 계산 실행
if operation:
    try:
        # 입력 값을 세션 상태에 저장하여 계산 오류 시에도 값 유지
        st.session_state['num1'] = num1
        st.session_state['num2'] = num2
        
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


# --- 6. 결과 출력 ---
st.subheader("결과")
if st.session_state['result'] == "오류":
    st.code("오류")
else:
    # 결과를 소수점 4자리까지만 표시하도록 설정 (깔끔한 표시)
    st.success(f"결과: {st.session_state['result']:.4f}")

