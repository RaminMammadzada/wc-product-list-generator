import PySimpleGUI as sg
from PIL import Image as ImagePIL

im = ImagePIL.open('/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/photo.jpg')
im.save('/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/photo.png')

def gui():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')],
              [sg.Image(r'/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/photo.png')]
            ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()