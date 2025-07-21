
import streamlit as st  # Streamlit 라이브러리 임포트
import pandas as pd  # 데이터프레임 처리
import numpy as np  # 통계 계산용

st.title('학생 성적 데이터 시각화')  # 페이지 제목

# 1. 데이터 정의 (문제에서 제시된 학생별 성적)
data = {
    '이름': ['홍길동', '김영희', '이철수', '박민수', '최지은'],
    '수학': [85, 90, 70, 95, 60],
    '영어': [78, 88, 65, 92, 72],
    '과학': [92, 84, 75, 89, 68]
}
df = pd.DataFrame(data)  # 데이터프레임 생성


# 학생별 성적 테이블 표시
st.subheader('학생별 성적 테이블')
st.dataframe(df)  # 데이터프레임 표시


# 학생별 평균 점수를 bar_chart로 시각화
st.subheader('학생별 평균 점수(그래프)')
df['평균'] = df[['수학', '영어', '과학']].mean(axis=1)  # 학생별 평균 컬럼 추가
avg_chart_df = pd.DataFrame({'평균': df['평균'].values}, index=df['이름'])
st.bar_chart(avg_chart_df)  # 학생별 평균 점수 막대그래프




# 과목별 석차를 꺾은선 그래프로 시각화
st.subheader('과목별 석차(그래프)')
rank_df = pd.DataFrame({'이름': df['이름']})  # 이름 컬럼 복사
for subject in ['수학', '영어', '과학']:
    # 내림차순(점수 높을수록 1등)으로 석차 계산
    rank_df[f'{subject} 석차'] = df[subject].rank(ascending=False, method='min').astype(int)
rank_df = rank_df.set_index('이름')
st.line_chart(rank_df)  # 학생별 과목 석차 꺾은선 그래프

# 4. 과목별 평균, 분산, 사분위수, boxplot
for subject in ['수학', '영어', '과학']:
    st.subheader(f'{subject} 성적 통계')
    mean = df[subject].mean()
    var = df[subject].var()
    q1 = df[subject].quantile(0.25)
    q2 = df[subject].quantile(0.5)
    q3 = df[subject].quantile(0.75)
    st.write(f"평균: {mean:.2f}")
    st.write(f"분산: {var:.2f}")
    st.write(f"1사분위수(Q1): {q1:.2f}")
    st.write(f"2사분위수(중앙값, Q2): {q2:.2f}")
    st.write(f"3사분위수(Q3): {q3:.2f}")
    # boxplot 시각화
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.boxplot(df[subject], labels=[subject])
    ax.set_title(f'{subject} 성적 Boxplot')
    st.pyplot(fig)
    st.divider()
