import cv2 as cv
import sys

print(cv.__version__)

# Load images
img = cv.imread(cv.samples.findFile("hitler.jpeg"))

if img is None:
    sys.exit("Could not read image")

cv.imshow("Display Window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("idola.png", img)