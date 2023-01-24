from PIL import Image, ImageDraw
import numpy as np
from scipy.cluster.vq import vq, kmeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import os

# === Main code starts here ===
fname = 'colours'  # folder name
nframes = 151  # number of frames
im_height = 90  # image height
im_width = 120  # image width


def getcurpath():
    return os.path.dirname(os.path.abspath(__file__))


curpath = getcurpath()
imagepath = os.path.join(curpath, fname)
imname = '%s\dwc%03d.png' % (imagepath, 1)
im = Image.open(imname).convert('RGB')

im.show()

# for i in range( nframes ):
# imname    = '%s/dwc%03d.png' % ( fname, i+1 )
# im        = Image.open( imname ).convert( 'RGB' )
# colors[i] = np.asarray(im, dtype = np.uint8)
# grays[i]  = np.asarray(im.convert( 'L' ))
