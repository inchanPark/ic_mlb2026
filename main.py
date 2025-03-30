import streamlit as st

st.title("📈 투자매력도 평가 툴")

code = st.text_input("종목 코드를 입력하세요:")
if code:
    st.success(f"입력한 종목: {code}")
    st.write("이 종목의 투자매력도는 **83점**입니다. (샘플 점수)")
