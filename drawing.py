import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Thiccness 5 (root, from, to, color, thiccness)
cv.line(img, (0,0), (512,512), (255, 0, 0), 5)

# Drawing a rectangle (Root and Top-left and Bottom-right and Color and THICCness)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Circle (root, center, radius, color, THICCNESS)
cv.circle(img, (447, 63), 63, (0,0,255), 3)

# Drawing a polygon
pts = np.array([[10, 5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Writing text on images (root, text, Coordinates-bottom-left, fonttype, fontscale, color, thicness, cv.LINE_AA for better look)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255,255,255),2, cv.LINE_AA)

cv.imshow("Image", img)
k = cv.waitKey(0)