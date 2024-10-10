import streamlit as st
import pandas as pd

data = st.file_uploader("upload file", type={"csv", "txt"})
if data is not None:
    df = pd.read_csv(data)
    df = df[::-1]
    df['time'] = df.index
    x_col, y_col, b_enter = st.columns(3)
    x_input = x_col.text_input("X축 이름", key="x_col")
    y_input = y_col.text_input("Y축 이름", key="y_col")
    b_enter.header("")
    b_fin = b_enter.button("완료")
    st.write(df)
    if b_fin:
        st.line_chart(df, x=x_input, y=y_input)