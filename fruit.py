import streamlit as st


count = 0

st.header("Count " + str(count))

def fruitClick():
    global count
    count += 1
    # st.header("Count " + str(count))

col1, col2, col3 = st.columns(3)
col1.button("Apple", on_click = fruitClick)
col2.button("Banana", on_click = fruitClick)
col3.button("Orange", on_click = fruitClick)


