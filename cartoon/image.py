from PIL import Image
import PySimpleGUI as sg
import numpy as np
from numpy import asarray, average, int8
from numpy import pad, size
import matplotlib.pyplot as plt
from io import BytesIO



class IMAGE :
    def __init__(self,file):
        self.image = self.get_image(file)
    
    
    def get_image(self,file):
        return Image.open(file)
    
    def convert(self):
        
        self.image.thumbnail((400,400))
        # image = asarray(self.image)
        bio = BytesIO()
        self.image.save(bio, format = 'PNG')
        return bio
