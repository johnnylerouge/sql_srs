import streamlit as st
import pandas as pd

st.write("Hello world")
data = {"a": [1, 2, 3], "b": [3, 4, 5]}
df = pd.DataFrame(data)

st.write('''
Spaced Repetition System SQL
''')

option = st.selectbox("How would you like to be contacted",
                      ["Joins", "Group By", "Window function"],
                       index = None,
                       placeholder = "select your theme...")

st.write("Your selected option is:", option)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    input_text = st.text_area(label = 'entrez votre input')
    st.write(input_text)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

