from PIL import Image
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from helper import HELP
from image import IMAGE


help = HELP()
layout = help.components()

window = sg.Window('Image Inhancement', layout = layout , margins=(0, 0), resizable=False, return_keyboard_events=True)

while True:
    event, values = window.read()
    # print(event, values)
    if event in [None, 'Exit']:
        break
    
    
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = help.open_file()
        image = IMAGE(file)
        bio = image.convert()
        window["-IMAGE-"].update(data = bio.getvalue())
    if event == 'Cartonify':
        image.image = help.cartoonify(image.image)
        bio = image.convert()
        window["-IMAGE-"].update(data = bio.getvalue())

