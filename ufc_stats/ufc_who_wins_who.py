# import streamlit as st
# from st_keyup import st_keyup
#
# # 이름 리스트 (예시)
# people = [
#     "T.J. Dillashaw",
#     "Tyler Durden",
#     "Daniel Cormier",
#     "Tony Ferguson",
#     "Dustin Poirier",
#     "Dominick Cruz",
#     "Tommy Dreamer",
#     "Max Holloway",
# ]
#
# # 서브시퀀스 매칭 함수 (문자 순서만 중요)
# def is_subsequence(query, name):
#     query = query.lower()
#     name = name.lower()
#     i = 0
#     for char in name:
#         if i < len(query) and char == query[i]:
#             i += 1
#     return i == len(query)
#
#
# # UI
# st.title("유저 이름 이니셜 검색기")
# value = st_keyup("Enter a value", key="0")st.subheader("검색 결과:")
#
# # 매칭 이름 필터링
# if user_input:
#     matches = sorted([name for name in people if is_subsequence(user_input, name)])
# else:
#     matches = people  # 아무것도 입력 안 하면 전체 보여주기
#
# if matches:
#     for name in matches:
#         st.write(f"• {name}")
# else:
#     st.write("🔍 일치하는 이름이 없습니다.")


import streamlit as st
from st_keyup import st_keyup

value = st_keyup("Enter a value", key="0")

# Notice that value updates after every key press
st.write(value)

# If you want to set a default value, you can pass one
with_default = st_keyup("Enter a value", value="Example", key="1")

# If you want to limit how often the value gets updated, pass `debounce` value, which
# will force the value to only update after that many milliseconds have passed
with_debounce = st_keyup("Enter a value", debounce=500, key="2")