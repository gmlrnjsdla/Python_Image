import cv2
import numpy as np

image = cv2.imread("Image/sample.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Test Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
