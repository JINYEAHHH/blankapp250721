import streamlit as st  # Streamlit 라이브러리 임포트
import pandas as pd  # 데이터프레임 및 CSV 처리
import numpy as np  # 수치형 데이터 예시용

st.title('CSV 파일 데이터 시각화')  # 페이지 제목

# CSV 파일 업로드 위젯
uploaded_file = st.file_uploader('CSV 파일을 업로드하세요', type=['csv'])

if uploaded_file is not None:
    # 업로드된 CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.write('업로드된 데이터 미리보기:')
    st.dataframe(df)  # 데이터프레임 표시

    # 수치형 컬럼만 자동으로 추출
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 1:
        st.write('수치형 컬럼 차트:')
        st.line_chart(df[numeric_cols])  # 수치형 데이터 라인 차트
        st.bar_chart(df[numeric_cols])   # 수치형 데이터 바 차트
    else:
        st.info('시각화할 수치형 컬럼이 없습니다.')
else:
    st.caption('CSV 파일을 업로드하면 데이터와 차트가 표시됩니다.')
