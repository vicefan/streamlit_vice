import streamlit as st
import pandas as pd

data = st.file_uploader("File Upload", type={"csv", "txt"})

if data is not None:
    # Read Data
    df = pd.read_csv(data)
    df = df[::-1]

    # Layout Setting
    x_col, y_col, b_enter = st.columns(3)
    error_label = st.text("")

    # Setting axis name
    x_input = x_col.text_input("X축 이름", key="x_col")
    y_input = y_col.text_input("Y축 이름", key="y_col")

    # Button
    b_enter.text("")
    b_fin = b_enter.button("📝")
    st.write(df)

    # Draw Graph with user input
    if b_fin:
        if x_input == "" or y_input == "":
            error_label.error("***값을 입력하세요.***", icon="🚨")
        elif x_input not in df.columns or y_input not in df.columns:
            error_label.error('***존재하지 않는 값*** 입니다.', icon="🚨")
        else:
            error_label.subheader("""✅ 생성 완료!""")
            st.line_chart(df, x=x_input, y=y_input)