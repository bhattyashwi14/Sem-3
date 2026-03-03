# To-Do List App
# Let the user enter a task in a text input and add it via a button.
# - Show all added tasks in a checkbox list.
# - When a checkbox is ticked, mark the task as completed (use st.success() message).
import streamlit as st
st.title("To-Do List")
task=st.text_input("Enter your task:")
if "task_list" not in st.session_state:
    st.session_state.task_list = []

if st.button("Add task"):
    st.session_state.task_list.append(task)
if st.button("Display"):
    st.header("Task List")
    for i in range(len(st.session_state.task_list)):
        res=st.checkbox(st.session_state.task_list[i])
        if res:
            st.success("Task completed!")