import streamlit as slt
import functions

filepath = 'todos.txt'
todos = functions.get_todos(filepath=filepath)

def add_todo():
    todo = slt.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos,filepath=filepath)

def complete_todo():
    todo = slt.session_state["new_todo"]

    todos.remove(todo)
    functions.write_todos(todos,filepath=filepath)


slt.title("My todo app")
slt.subheader("This is my new program")
slt.write("I'm writing sth new for you")

for todo in functions.get_todos(filepath=filepath):
    CheckBox = slt.checkbox(todo,key=todo)
    if CheckBox:
        todos.remove(todo)
        functions.write_todos(todos,filepath=filepath)
        del slt.session_state[todo]
        slt.experimental_rerun()

print(slt.text_input(label="todo",label_visibility="hidden",placeholder="Enter a phrase here",
               on_change=add_todo,key="new_todo"))

