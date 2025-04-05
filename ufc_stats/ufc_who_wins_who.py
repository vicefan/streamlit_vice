import streamlit as st

# 예시 인물 리스트
people = [
    "T.J. Dillashaw",
    "Tyler Durden",
    "Daniel Cormier",
    "Tony Ferguson",
    "Dustin Poirier",
    "Dominick Cruz",
    "Tommy Dreamer",
    "Max Holloway",
]

# 서브시퀀스 매칭 함수
def is_subsequence(query, name):
    query = query.lower()
    name = name.lower()
    i = 0
    for char in name:
        if i < len(query) and char == query[i]:
            i += 1
    return i == len(query)

# UI 구성
st.title("이니셜 검색기")
query = st.text_input("이니셜이나 일부 글자를 입력하세요 (예: 'td'):")

if query:
    matches = [person for person in people if is_subsequence(query, person)]
    if matches:
        st.selectbox(matches)
