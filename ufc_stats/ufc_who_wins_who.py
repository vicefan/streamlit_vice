import streamlit as st

# 이름 리스트 (예시)
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

# 서브시퀀스 매칭 함수 (문자 순서만 중요)
def is_subsequence(query, name):
    query = query.lower()
    name = name.lower()
    i = 0
    for char in name:
        if i < len(query) and char == query[i]:
            i += 1
    return i == len(query)

# UI
st.title("유저 이름 이니셜 검색기")
user_input = st.text_input("검색어를 입력하세요 (예: t, td, dc 등):")

# 매칭 이름 필터링
if user_input:
    matches = [name for name in people if is_subsequence(user_input, name)].sort()
else:
    matches = people  # 아무것도 입력 안 하면 전체 보여주기

# 결과 표시
st.subheader("검색 결과:")
if matches:
    for name in matches:
        st.write(f"• {name}")
else:
    st.write("🔍 일치하는 이름이 없습니다.")
