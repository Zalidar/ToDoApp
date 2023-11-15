import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlack")

functions.check_file()
label = sg.Text("Enter a to-do item")
input_box = sg.InputText(tooltip="Enter a to-do item", key="todo")
add_button = sg.Button(button_text="Add")
exit_button = sg.Button(button_text="Exit")
todo_list = sg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=(45, 10))
edit_button = sg.Button(button_text="Edit")
complete_button = sg.Button(button_text="Complete")
clock_label = sg.Text("", key="clock")

window = sg.Window(title="My To-Do App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [todo_list, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case sg.WIN_CLOSED | "Exit":
            break

window.close()
