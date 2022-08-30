from PIL import Image
import PySimpleGUI as sg
import numpy as np
from numpy import asarray, average, int8
import pathlib
import cv2
from image import IMAGE


class HELP:

    def __init__(self):
        self.layout = []
        sg.theme('DarkTanBlue')
        self.FIRST_COLOR = f'#E7E7E7 on #041B2D'
        self.SECOND_COLOR = '#041B2D on #9B9B9B '
        self.menu_def = [['&File', ['&Open (Ctrl+O)', '&Save', 'Exit']], ]
        
    def components(self):
        mid_col = sg.Column([
            [sg.Text("import image:")],
            [sg.Image(key="-IMAGE-", size=(300, 300),background_color='white')],
            [sg.B('Cartonify', button_color=self.SECOND_COLOR, pad=(100, 0))]
            
        ], pad=(70, 0))
        
        self.layout = [
            [sg.MenubarCustom(self.menu_def)],
            [mid_col]
        ]
        return self.layout
    
    def open_file(self):
        filename = sg.popup_get_file('Open', no_window=True)
        if filename:
            file = pathlib.Path(filename)
            return file
        
    def cartoonify(self, image):
        arr = asarray(image)
        gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        # Cartoonization
        color = cv2.bilateralFilter(arr, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return Image.fromarray(cartoon)
