import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader

# OpenAI API key 설정
api_key = st.secrets["api_key"]
client = OpenAI(api_key=api_key)

st.set_page_config(layout="wide")

# Streamlit 애플리케이션
st.title("ChatGPT PDF Application")

text = ''

# PDF 파일 열기
file = st.file_uploader("Upload PDF", type="pdf")
if file:
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
else:
    text = "PDF가 입력되지 않았습니다."


def get_chat_response(message, text):
    chat_completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": f"""사용자의 PDF (PDF가 없으면 'PDF가 입력되지 않았습니다.') : {text}\n
            사용자의 질문(답변도 한국어로 작성) : {message}"""},
            {"role": "user", "content": message}
        ],
        max_completion_tokens=1000
    )
    return chat_completion.choices[0].message.content


message = st.text_area("Enter your message:")
if st.button("Get Response"):
    response = get_chat_response(message, text)
    st.markdown(response)