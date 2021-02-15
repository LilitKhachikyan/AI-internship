import numpy as np
import cv2

src = cv2.imread('src.jpeg')
src_gray = cv2.imread('src.jpeg', 0)
temp = cv2.imread('temp.jpeg', 0)
match = cv2.matchTemplate(src_gray, temp, cv2.TM_CCOEFF_NORMED)
best_match=[]
for i in range(0, match.shape[0]-1):
    for j in range(0, match.shape[1]-1):
        if match[i][j]>0.49:
            best_match.append((j,i))

print(best_match)
weight, height = temp.shape[::-1]

for start in best_match:
    cv2.rectangle(src, start, (start[0]+weight, start[1]+height), (29, 8, 1), 1)

cv2.imshow('Source picture', src)
cv2.waitKey()
cv2.destroyAllWindows()
