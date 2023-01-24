import numpy as np
import cv2
import os

fname = 'image'  # folder name
def getcurpath():
    return os.path.dirname(os.path.abspath(__file__))


curpath = getcurpath()
imagepath = os.path.join(curpath, fname)
imname = '%s\Cattura.png' % (imagepath)
img = cv2.imread(imname, 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
