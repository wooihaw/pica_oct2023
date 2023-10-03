import PySimpleGUI as sg
import time

# My function that takes a long time to do...
def my_long_operation():
    time.sleep(10)
    return 'My return value'


def main():
    """
    This function creates a PySimpleGUI window with an input field, an output field, and three buttons.
    The 'Go' button calls the my_long_operation function and displays the return value in the output field.
    The 'Thread' button uses PySimpleGUI to perform the long operation in a separate thread and displays the return value in the output field.
    The 'Dummy' button simply displays the input value in the output field.
    """
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN-')],
                [sg.Text(key='-OUT-')],
                [sg.Button('Go'), sg.Button('Thread'), sg.Button('Dummy')]  ]

    window = sg.Window('Window Title', layout, keep_on_top=True)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Go':
            return_value = my_long_operation()
            window['-OUT-'].update(f'Go return value = {return_value}')
        elif event  == 'Thread':
            # Let PySimpleGUI do the threading for you...
            window.perform_long_operation(my_long_operation, '-OPERATION DONE-')
        elif event  == '-OPERATION DONE-':
            window['-OUT-'].update(f'Thread return value = {values[event]}')
        elif event == 'Dummy':
            window['-OUT-'].update(values['-IN-'])

    window.close()

if __name__ == '__main__':
    main()