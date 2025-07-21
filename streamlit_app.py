import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# 제목 및 설명 요소
# -----------------------------
st.title("Streamlit 요소 데모 페이지")  # 페이지 제목
st.header("📋 다양한 Streamlit UI 요소")  # 섹션 제목
st.subheader("기본 텍스트 및 인터페이스 구성 요소")  # 하위 섹션 제목
st.text("이 페이지는 Streamlit에서 사용할 수 있는 거의 모든 기본 요소를 시연합니다.")  # 일반 텍스트
st.markdown("**이 페이지는 마크다운 형식을 사용할 수 있습니다!**")  # 마크다운 지원
st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록 출력
st.latex(r"E = mc^2")  # LaTeX 수식 출력

# -----------------------------
# 데이터 표시 관련 요소
# -----------------------------
df = pd.DataFrame({
    "숫자": np.random.randint(1, 100, 10),
    "카테고리": list("ABCDEFGHIJ")
})
st.subheader("📊 데이터 출력")
st.dataframe(df)  # 인터랙티브한 데이터프레임
st.table(df.head())  # 정적인 표 형태
st.json({"name": "Streamlit", "type": "Web App Framework"})  # JSON 형식 출력

# -----------------------------
# 차트 요소
# -----------------------------
st.subheader("📈 차트와 그래프")
st.line_chart(np.random.randn(20, 3))  # 선형 차트
st.bar_chart(np.random.randn(20, 3))   # 막대 차트
st.area_chart(np.random.randn(20, 3))  # 영역 차트



# -----------------------------
# 미디어 요소
# -----------------------------
st.subheader("📷 이미지, 오디오, 비디오")
st.image("https://via.placeholder.com/150", caption="예시 이미지", use_column_width=True)  # 이미지 표시
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 재생
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 재생

# -----------------------------
# 위젯 (사용자 입력)
# -----------------------------
st.subheader("🎛️ 사용자 입력 위젯")

# 텍스트 입력
name = st.text_input("이름을 입력하세요")  # 텍스트 입력 필드
st.write(f"안녕하세요, {name}님!")

# 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력 필드

# 슬라이더
score = st.slider("점수를 선택하세요", 0, 100, 50)  # 슬라이더 위젯

# 체크박스
show_data = st.checkbox("데이터 보이기")  # 체크박스
if show_data:
    st.write(df)

# 라디오 버튼
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼

# 셀렉트 박스
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])  # 셀렉트 박스

# 멀티 셀렉트
hobbies = st.multiselect("취미를 선택하세요", ["독서", "영화", "운동", "게임"])  # 다중 선택

# 날짜, 시간
date = st.date_input("날짜 선택")  # 날짜 선택
time = st.time_input("시간 선택")  # 시간 선택

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드
if uploaded_file:
    st.write("업로드된 파일 이름:", uploaded_file.name)

# 버튼
if st.button("버튼을 클릭하세요"):  # 버튼 클릭 시 반응
    st.success("버튼이 클릭되었습니다!")

# -----------------------------
# 상태 표시
# -----------------------------
st.subheader("🛠️ 상태 및 진행 표시")
st.success("성공 메시지")  # 성공 알림
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("오류 메시지")  # 오류 메시지
st.exception(Exception("예외 발생"))  # 예외 객체 출력

# 진행 바
import time
with st.spinner("잠시 기다려 주세요..."):
    time.sleep(1)
st.progress(100)  # 진행 바 완료

# -----------------------
