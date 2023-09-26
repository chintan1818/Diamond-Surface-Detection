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

    for y in range(1, edges.shape[1], 1) :
        if edges[x][y] == 255 :
            arLeft.append([x,y])



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
    edges[val[0]][val[1]] =10
    edges[val[0]][val[1]+1] = 10
    edges[val[0]][val[1]+2] = 10
    edges[val[0]][val[1]+3] = 10

for val in criticalRight:
    edges[val[0]][val[1]] =10
    edges[val[0]][val[1]-1] = 10
    edges[val[0]][val[1]-2] = 10
    edges[val[0]][val[1]-3] = 10



cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)

cv2.destroyAllWindows()