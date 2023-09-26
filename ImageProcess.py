import cv2

# Read the original image
img = cv2.imread('11.png')
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1.2)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=1)  # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1)  # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images

# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)

# Canny Edge Detection

# edges = cv2.Canny(image=img_blur, threshold1=25, threshold2=25)  # Canny Edge Detection


edges = cv2.Canny(image=img_blur, threshold1=18, threshold2=31)  # Canny Edge Detection


#
# def nothing(x):
#     pass
#
# cv2.namedWindow("Canny")
# cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)
# cv2.createTrackbar("Threshold1", "Canny", 0, 255, nothing)
# while True:
#     a = cv2.getTrackbarPos('Threshold', 'Canny')
#
#     print(a)
#
#     b = cv2.getTrackbarPos('Threshold1', 'Canny')
#     print(b)
#     res = cv2.Canny(img_blur, a, b)
#     cv2.imshow("Canny", res)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()





# Display Canny Edge Detection Image


arLeft=[]

for x in range(1, edges.shape[0], 1) :
    flag=0
    lastright = 0
    for y in range(1, edges.shape[1], 1) :

        if edges[x][y] == 255 :
            flag=1
            arLeft.append([x,y])
            lastright= y



        if flag == 0 :
            edges[x][y]=255

    for r in range(lastright,edges.shape[1],1) :
        edges[x][r]=255




tempx=0
criticalLeft =[]
criticalRight=[]
pre=arLeft[0]

for val in arLeft:

  if(val[0]!= tempx):
      tempx=val[0]
      criticalLeft.append(val)

  if(val[0] ==pre[0]) :
      pre=val
  else:
      criticalRight.append(pre)
      pre=val

criticalRight.append(arLeft[len(arLeft)-1])

for val in criticalLeft:
    edges[val[0]][val[1]] =255
    edges[val[0]][val[1]+1] = 255
    edges[val[0]][val[1]+2] = 255
    edges[val[0]][val[1]+3] = 255
    edges[val[0]][val[1] + 4] = 255
    edges[val[0]][val[1] + 5] = 255
    edges[val[0]][val[1] + 6] = 255
    edges[val[0]][val[1] + 7] = 255
    edges[val[0]][val[1] + 8] = 255
    edges[val[0]][val[1] + 9] = 255

for val in criticalRight:
    edges[val[0]][val[1]] =255
    edges[val[0]][val[1]-1] = 255
    edges[val[0]][val[1]-2] = 255
    edges[val[0]][val[1]-3] = 255
    edges[val[0]][val[1] - 4] = 255
    edges[val[0]][val[1] - 5] = 255
    edges[val[0]][val[1] - 6] = 255
    edges[val[0]][val[1] - 7] = 255
    edges[val[0]][val[1] - 8] = 255
    edges[val[0]][val[1] - 9] = 255


#for top reduction
for x in range(criticalLeft[0][0],criticalLeft[0][0]+20,1) :
    for y in range(1,edges.shape[1],1):
        edges[x][y]=255

cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)

cv2.destroyAllWindows()






##finder



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = edges
img2 = img.copy()
template = cv.imread('smallpart.png',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = [ 'cv.TM_SQDIFF']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 100, 10)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()


    cv.waitKey(0)

    cv.destroyAllWindows()