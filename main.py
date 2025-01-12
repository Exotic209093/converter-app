import PySimpleGUI as sg

# Apply a sleek and modern theme
sg.theme('LightBlue')

# Define conversion categories and units
conversions = {
    "Length": ["km to mile", "mile to km", "meter to feet", "feet to meter"],
    "Weight": ["kg to pound", "pound to kg", "ounce to gram", "gram to ounce"],
    "Time": ["sec to min", "min to sec", "hours to days", "days to hours"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
}

# Function to perform conversions
def perform_conversion(value, conversion_type, precision):
    try:
        value = float(value)
        if conversion_type == "km to mile":
            return f"{value} km = {value * 0.621371:.{precision}f} miles"
        elif conversion_type == "mile to km":
            return f"{value} miles = {value / 0.621371:.{precision}f} km"
        elif conversion_type == "meter to feet":
            return f"{value} meters = {value * 3.28084:.{precision}f} feet"
        elif conversion_type == "feet to meter":
            return f"{value} feet = {value / 3.28084:.{precision}f} meters"
        elif conversion_type == "kg to pound":
            return f"{value} kg = {value * 2.20462:.{precision}f} pounds"
        elif conversion_type == "pound to kg":
            return f"{value} pounds = {value / 2.20462:.{precision}f} kg"
        elif conversion_type == "ounce to gram":
            return f"{value} ounces = {value * 28.3495:.{precision}f} grams"
        elif conversion_type == "gram to ounce":
            return f"{value} grams = {value / 28.3495:.{precision}f} ounces"
        elif conversion_type == "sec to min":
            return f"{value} seconds = {value / 60:.{precision}f} minutes"
        elif conversion_type == "min to sec":
            return f"{value} minutes = {value * 60:.{precision}f} seconds"
        elif conversion_type == "hours to days":
            return f"{value} hours = {value / 24:.{precision}f} days"
        elif conversion_type == "days to hours":
            return f"{value} days = {value * 24:.{precision}f} hours"
        elif conversion_type == "Celsius to Fahrenheit":
            return f"{value} °C = {(value * 9/5) + 32:.{precision}f} °F"
        elif conversion_type == "Fahrenheit to Celsius":
            return f"{value} °F = {(value - 32) * 5/9:.{precision}f} °C"
        else:
            return "Invalid conversion type selected."
    except ValueError:
        return "Please enter a valid number."

# Define layout
layout = [
    [sg.Text('Enhanced Unit Converter', font=('Helvetica', 16), justification='center', expand_x=True)],
    [sg.HorizontalSeparator()],
    [sg.Text('Enter value:', size=(12, 1)), sg.Input('', key='-INPUT-', size=(20, 1))],
    [sg.Text('Category:', size=(12, 1)), sg.Combo(
        list(conversions.keys()), default_value='Length', key='-CATEGORY-', size=(15, 1),
        enable_events=True)],
    [sg.Text('Conversion type:', size=(12, 1)), sg.Combo(
        conversions["Length"], key='-CONVERSION-', size=(20, 1))],
    [sg.Text('Precision (decimals):', size=(15, 1)), sg.Spin(
        [0, 1, 2, 3, 4, 5], initial_value=2, key='-PRECISION-', size=(5, 1))],
    [sg.Button('Convert', key='-CONVERT-', size=(10, 1)), sg.Button('Clear', key='-CLEAR-', size=(10, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text('Result:', size=(10, 1)), sg.Text('', key='-OUTPUT-', size=(40, 1), text_color='blue', font=('Helvetica', 12))]
]

# Create the window
window = sg.Window('Enhanced Unit Converter', layout, element_justification='center', finalize=True)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-CATEGORY-':
        # Update conversion types based on selected category
        selected_category = values['-CATEGORY-']
        window['-CONVERSION-'].update(values=conversions[selected_category])

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        conversion_type = values['-CONVERSION-']
        precision = int(values['-PRECISION-'])

        result = perform_conversion(input_value, conversion_type, precision)
        window['-OUTPUT-'].update(result)

    if event == '-CLEAR-':
        # Clear the input and output fields
        window['-INPUT-'].update('')
        window['-OUTPUT-'].update('')

# Close the window
window.close()
