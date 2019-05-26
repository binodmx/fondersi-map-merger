import numpy as np
import cv2
import matplotlib.backends.backend_tkagg
from matplotlib import pyplot as plt

def check_image_extension(file_name):
    if file_name[-3:] in ["jpg", "png"]:
        return True
    return False   

def display():
    cv2.imshow('merged_image', merged_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def save(file_name):
    cv2.imwrite(file_name+".jpg", merged_map)
    
def merge(file_names):
    global merged_map

    imgs = []
    
    for file_name in file_names:
        if check_image_extension(file_name):
            img = cv2.imread(file_name, 1)
            imgs.append(img)
        else:
            return None
    
    stitcher = cv2.Stitcher.create()
    ret, pano = stitcher.stitch(imgs)

    if type(pano) != type(None):
        height, width, depth = pano.shape
        ratio = height/width
        dim = (400, int(ratio*400))
        merged_map = cv2.resize(pano, dim)
        return merged_map
    else:    
        return None
    
