import streamlit as st
import uuid

# initialize
if 'var' not in st.session_state:
    st.session_state.var = [None]
if 'uuid' not in st.session_state:
    st.session_state.uuid = [None]
selectbox_list = ['A', 'B', 'C']


# add new cell
def add_cell(index):
    element_id = str(uuid.uuid4())
    st.session_state.uuid.insert(index, element_id)
    st.session_state.var.insert(index, None)


# delete the cell
def delete_cell(index):
    if len(st.session_state.uuid) > 1:
        del st.session_state.uuid[index]
        del st.session_state.var[index]


# generate cell by feature saved at st.session_state
def gen_cell(index):
    element_id = st.session_state.uuid[index]
    cols = st.columns(2)

    # selectbox
    with cols[0]:
        if st.session_state.var[index] is None:
            selectbox_value = st.selectbox(f'Cell {index}', selectbox_list, index=None, key=f'selectbox_{element_id}')
        else:
            selectbox_value = st.selectbox(f'Cell {index}', selectbox_list,
                                           index=selectbox_list.index(st.session_state.var[index]),
                                           key=f'selectbox_{element_id}')
    # button
    with cols[1]:
        cols2 = st.columns(3)
        with cols2[1]:
            st.write('')
            st.write('')
            st.button('\+', key=f"add_{element_id}", on_click=add_cell, args=[index + 1])
        with cols2[2]:
            st.write('')
            st.write('')
            st.button("\-", key=f"delete_{element_id}", on_click=delete_cell, args=[index])

    return {'var': selectbox_value}


# feature save
rows_collection = []
for index in range(len(st.session_state.var)):
    row_data = gen_cell(index)
    rows_collection.append(row_data)

# asign feature
if len(rows_collection) > 0:
    for i in range(len(rows_collection)):
        st.session_state.var[i] = rows_collection[i]['var']