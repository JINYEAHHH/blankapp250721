import streamlit as st  # Streamlit 라이브러리 임포트
import pandas as pd  # 데이터프레임 및 CSV 처리
import numpy as np  # 난수 생성
import time  # 실시간 차트 시뮬레이션용

st.title('데이터 시각화 예시 페이지')  # 페이지 제목

# 1. 지도 기반 위치 시각화 예시
st.header('1. 지도 기반 위치 시각화')
# 임의의 위도/경도 데이터 생성
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.5665, 126.9780],  # 서울 근처 좌표
    columns=['lat', 'lon']
)
st.map(map_data)  # 지도 위에 데이터 표시

# 2. CSV 파일 업로드 및 시각화 예시
st.header('2. CSV 파일 업로드 및 시각화')
uploaded_file = st.file_uploader('CSV 파일을 업로드하세요', type=['csv'])  # 파일 업로더
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # CSV 파일 읽기
    st.write('업로드된 데이터 미리보기:')
    st.dataframe(df)  # 데이터프레임 표시
    # 수치형 컬럼만 선택하여 차트로 시각화
    numeric_cols = df.select_dtypes(include=np.number).columns
    if len(numeric_cols) >= 2:
        st.line_chart(df[numeric_cols])  # 수치형 데이터 라인 차트
    else:
        st.info('시각화할 수치형 컬럼이 2개 이상 필요합니다.')
else:
    st.caption('CSV 파일을 업로드하면 데이터와 차트가 표시됩니다.')

# 3. 난수 스트리밍을 시뮬레이션한 실시간 라인 차트
st.header('3. 실시간 난수 스트리밍 라인 차트')
chart_placeholder = st.empty()  # 차트가 표시될 자리
N = 50  # 차트에 표시할 데이터 포인트 개수
run_stream = st.button('실시간 차트 시작')  # 차트 시작 버튼
if run_stream:
    data = np.random.randn(N)
    for i in range(100):  # 100번 반복 (100프레임)
        new_val = data[-1] + np.random.randn() * 0.5  # 이전 값에 난수 더하기
        data = np.append(data[1:], new_val)  # 데이터 갱신
        chart_placeholder.line_chart(data)  # 차트 업데이트
        time.sleep(0.05)  # 0.05초 대기 (약 20fps)
    st.success('실시간 차트 시뮬레이션 종료!')
else:
    st.caption('버튼을 누르면 실시간 차트가 시작됩니다.')
