import streamlit as st
import pandas as pd
import numpy as np

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randint(0,10,size=(100,4)), columns = ['A','B','C','D'])

df = st.session_state.df

st.write(df)

n = st.number_input('Number of selections', step=1)

def selection_row(i):
    cols = st.columns(3)
    a = cols[0].selectbox(f'A ({i})',df['A'].unique())
    b = cols[1].selectbox(f'B ({i})',df[df['A']==a]['B'].unique())
    c = cols[2].selectbox(f'C ({i})',df[df['A']==a][df['B']==b]['C'].unique())
    return (a,b,c)

selections = []

for row in range(n):
    selections.append(selection_row(row))

st.write('Result:')
st.dataframe(selections)