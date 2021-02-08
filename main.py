import numpy as np
import cv2

src = cv2.imread('src.jpeg')
src_gray = cv2.imread('src.jpeg', 0)
temp = cv2.imread('temp.jpeg', 0)
match = cv2.matchTemplate(src_gray, temp, cv2.TM_CCOEFF_NORMED)
best_match = np.where(match > 0.49)
weight, height = temp.shape[::-1]

for ind in range(0, best_match[0].size - 1):
    end = best_match[0][ind]
    start = best_match[1][ind]
    cv2.rectangle(src, (start, end), (start + weight, end + height), (29, 8, 1), 1)

cv2.imshow('Source picture', src)
cv2.waitKey()
cv2.destroyAllWindows()