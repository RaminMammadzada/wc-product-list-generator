import PySimpleGUI as sg




def gui3():
    # Next demo is to show how to create custom windows with animations
    layout = [[sg.Image(filename=r'/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/photo.jpg',
                        enable_events=True,
                        background_color='white',
                        key='_IMAGE_',
                        right_click_menu=['UNUSED', 'Exit'])],]

    window = sg.Window('My new window', no_titlebar=True, grab_anywhere=True, keep_on_top=True, background_color='white', alpha_channel=.8, margins=(0,0)).Layout(layout)

    offset = 0
    while True:                                     # Event Loop
        event, values = window.Read(timeout=10)     # loop every 10 ms to show that the 100 ms value below is used for animation
        if event in (None, 'Exit', 'Cancel'):
            break
                 # get a new gif image
        # update the animation in the window
        window.Element('_IMAGE_').UpdateAnimation(r'/Volumes/G-DRIVE mobile SSD R-Series/Shoes/Web saytlar/newkamuelshoes/pythongui_trial/photo.jpg',  time_between_frames=100)