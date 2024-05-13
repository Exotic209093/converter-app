import PySimpleGUI as sg

layout = [
    [
        sg.Input('', key='-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Result:'), sg.Text('', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        unit = values['-UNITS-']

        # Check if input is a valid number
        if input_value.isnumeric():
            input_value = float(input_value)  # Convert input to float
            conversion_result = None

            # Perform conversion based on selected unit
            if unit == 'km to mile':
                conversion_result = input_value * 0.621371
                output = f'{input_value} km is {conversion_result} miles'
            elif unit == 'kg to pound':
                conversion_result = input_value * 2.20462
                output = f'{input_value} kg is {conversion_result} pounds'
            elif unit == 'sec to min':
                conversion_result = input_value / 60
                output = f'{input_value} sec is {conversion_result} minutes'
            else:
                output = 'Invalid unit selection'
        else:
            output = 'Invalid input'

        window['-OUTPUT-'].update(output)

window.close()
