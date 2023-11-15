import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-Do App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new to-do item")
