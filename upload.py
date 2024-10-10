import streamlit as st
import pandas as pd

data = st.file_uploader("File Upload", type={"csv", "txt"})

if data is not None:
    # Read Data
    df = pd.read_csv(data)
    df = df[::-1]
    df['time'] = df.index
    # Layout Setting
    x_col, y_col, b_enter = st.columns(3)

    # Setting axis name
    x_input = x_col.text_input("X축 이름", key="x_col")
    y_input = y_col.text_input("Y축 이름", key="y_col")

    # Button
    b_enter.header("")
    b_fin = b_enter.button("완료")
    st.write(df)

    # Draw Graph with user input
    if b_fin:
        st.line_chart(df, x=x_input, y=y_input)