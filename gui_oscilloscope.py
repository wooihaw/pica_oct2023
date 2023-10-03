import PySimpleGUI as sg  # Import the PySimpleGUI library

# Define the available channels, vertical scales, and timebase scales
channels = tuple(range(1, 5))
vscales = ('100mV', '200mV', '500mV', '1V', '2V', '5V')
tscales = ('50us', '100us', '200us', '500us', '1ms', '2ms', '5ms')

# Define the sizes of the text and button elements
text_size = (13, 1)
button_size = (6, 1)

# Define the layout of the GUI using PySimpleGUI elements
layout = [  [sg.Text('Channel', size=text_size), sg.Combo(channels, default_value=channels[0], key='-channel-', expand_x=True)],
            [sg.Text('Vertical scale', size=text_size), sg.Combo(vscales, key='-vscale-', default_value=vscales[3], expand_x=True)],
            [sg.Text('Vertical Offset', size=text_size), sg.Slider(range=(-5.0, 5.0), default_value=0.0, resolution=0.1, orientation='h', key='-voffset-', expand_x=True)],
            # Add the timebase scale and position elements here
            [sg.Button('Connect', size=button_size), sg.Button('Send', size=button_size, disabled=True), sg.Button('Close', size=button_size)]
]

# Create the GUI window using the defined layout
window = sg.Window('Oscilloscope', layout, element_justification='center')

# Start the event loop for the GUI
while True:
    event, values = window.read()  # Wait for an event to occur
    if event in (sg.WIN_CLOSED, 'Close'):  # If the user closes the window or clicks the Close button
        break  # Exit the event loop
    if event == 'Connect':  # If the user clicks the Connect button, enable the send button
        ...
    elif event == 'Send':  # If the user clicks the Send button
        # Display a popup with the selected channel, vertical scale, vertical offset, timebase scale, and timebase position
        ...

window.close()  # Close the GUI window when the event loop exits