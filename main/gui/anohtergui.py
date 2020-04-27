import PySimpleGUI as sg

def newGUI():
    layout = [
        [sg.Text('Text'), sg.Input('Name'), sg.Button('Button1')],
        [sg.MLine('Multiple Input', size=(30,5)) ],
        [ sg.Slider(range(0,100),
                    orientation='v', size=(7,15), default_value=40),
          sg.Slider(range(0, 100),
                    orientation='h', size=(11, 15), default_value=40)
          ],
        [sg.Image(r'/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/PySimpleGUI_Logo_320.gif')]
    ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in ('Exit', None): # if user closes window or clicks cancel
            break
        print( event, values[0])

        if event == 'Ok':
            print(values)

    window.close()