import streamlit as st


input_label, button_label, output_label = st.columns(3)

input_label.subheader("Input")
button_label.subheader("")
output_label.subheader("Output")

input_text = input_label.text_input("Input Number")
output_text = output_label.text("")

b_k2m = button_label.button("km/L to mile/gallon")
b_m2k = button_label.button("mile/gallon to km/L")

if b_k2m:
    output_label.text(str(float(input_text) * 2.35214583))

if b_m2k:
    output_label.text(str(float(input_text) / 2.35214583))

# // 참조 //
# https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# https://docs.streamlit.io/develop/api-reference/layout/st.columns

# streamlit 링크 : https://appvice-s2uaxjv6y3jrdpwscswunf.streamlit.app/