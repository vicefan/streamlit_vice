import streamlit as st
import pandas as pd

data = st.file_uploader("***파일 업로드***", type={"csv", "txt"})

if data is not None:
    # Read Data
    df = pd.read_csv(data)
    df = df[::-1]

    # Layout Setting
    x_col, y_col, b_enter = st.columns(3)
    error_label = st.text("")

    # Setting axis name
    x_input = x_col.selectbox("***X축***", df.columns, key="x_col")
    y_input = y_col.selectbox("***Y축***", df.columns, key="y_col")

    # Button
    b_enter.text("")
    b_fin = b_enter.button("📝")
    st.write(df)

    # Draw Graph with user input
    if b_fin:
        error_label.subheader("""✅ 생성 완료!""")
        st.line_chart(df, x=x_input, y=y_input)