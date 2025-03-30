import streamlit as st

st.title("📈 투자매력도 평가 툴")

code = st.text_input("종목 코드를 입력하세요:")
if code:
    st.success(f"입력한 종목: {code}")
    st.write("👉 여기에 분석 결과가 나올 예정입니다!")
