import streamlit as st  # Streamlit 라이브러리 임포트
import matplotlib.pyplot as plt  # matplotlib 임포트
import numpy as np  # 데이터 생성용
from matplotlib import font_manager, rc  # 한글 폰트 설정용

st.title('Matplotlib 데이터 시각화 예시')  # 페이지 제목

# 한글 폰트 설정 (NanumGothic, 맑은 고딕 등 시스템에 따라 다름)

# NanumGothic-Regular.ttf 폰트 파일을 직접 불러와서 한글 폰트로 지정
import os
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')  # 폰트 파일 경로
font_manager.fontManager.addfont(font_path)  # 폰트 매니저에 폰트 추가
rc('font', family='NanumGothic')  # 폰트 패밀리 지정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 예시 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선')  # 한글 라벨
ax.set_title('Matplotlib 한글 그래프 예시')  # 한글 제목
ax.set_xlabel('x축')  # x축 라벨
ax.set_ylabel('y축')  # y축 라벨
ax.legend()

# Streamlit에 그래프 출력
st.pyplot(fig)
