import cv2
import numpy as np
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
    # validate file names
    
    imgs = []
    dim = (800, 600)
    for file_name in file_names:
        img = cv2.imread(file_name, 1)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        imgs.append(img)

    stitcher = cv2.createStitcher()
    ret, pano = stitcher.stitch(imgs)

    merged_map = pano
                
    return merged_map
    
