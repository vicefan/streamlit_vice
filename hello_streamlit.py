import streamlit as st
from math import sqrt, sin, cos, tan

# Initialize session state for the calculator display
if 'display' not in st.session_state:
    st.session_state.display = "0"

# Function to update the display
def update_display(value):
    if st.session_state.display == "0":
        st.session_state.display = value
    else:
        st.session_state.display += value

# Function to evaluate the expression
def evaluate_expression():
    try:
        st.session_state.display = str(eval(st.session_state.display))
    except Exception as e:
        st.session_state.display = "Error"

# Layout of the calculator
st.title("Streamlit Calculator")

st.text_input("Display", value=st.session_state.display, key="display", disabled=True)

# Number buttons
cols = st.columns(3)
for i in range(1, 10):
    if cols[(i-1) % 3].button(str(i)):
        update_display(str(i))

if st.button("0"):
    update_display("0")

# Operation buttons
if st.button("."):
    update_display(".")
if st.button("+"):
    update_display(" + ")
if st.button("-"):
    update_display(" - ")
if st.button("*"):
    update_display(" * ")
if st.button("/"):
    update_display(" / ")
if st.button("**2"):
    update_display(" ** 2")
if st.button("**"):
    update_display(" ** ")
if st.button("abs"):
    update_display("abs(")
if st.button("π"):
    update_display(" 3.141592")
if st.button("sqrt"):
    update_display("sqrt(")
if st.button("sin"):
    update_display("sin(")
if st.button("cos"):
    update_display("cos(")
if st.button("tan"):
    update_display("tan(")
if st.button("("):
    update_display("(")
if st.button(")"):
    update_display(")")

# Special buttons
if st.button("C"):
    st.session_state.display = "0"
if st.button("DEL"):
    st.session_state.display = st.session_state.display[:-1]
if st.button("+/-"):
    if st.session_state.display.startswith("(-"):
        st.session_state.display = st.session_state.display[2:]
    else:
        st.session_state.display = "(-" + st.session_state.display
if st.button("="):
    evaluate_expression()