import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader

# OpenAI API key 설정
api_key = st.secrets["apikey"]
client = OpenAI(api_key=api_key)

st.set_page_config(layout="wide")

# Streamlit 애플리케이션
st.title("ChatGPT PDF Application")


# PDF 파일 열기
file = st.file_uploader("Upload PDF", type="pdf")
if file:
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

def get_chat_response(message, text):
    chat_completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": f"""{text}\n
            위 내용을 토대로 사용자의 질문인, //{message}//에 대한 답변을 생성합니다. 답변은 markdown을 사용하여 표현된다는 것을 인지하여 작성합니다. 반드시 한국말로 설명합니다."""},
            {"role": "user", "content": message}
        ]
    )
    return chat_completion.choices[0].message.content


message = st.text_area("Enter your message:")
if st.button("Get Response"):
    response = get_chat_response(message, text)
    st.markdown(response)