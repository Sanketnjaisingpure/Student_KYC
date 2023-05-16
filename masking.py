import cv2 as cv
from cv2 import bitwise_and
import numpy as np
from pytesseract import image_to_string

img = cv.imread(r"save_images_files\photo5.jpg")

cv.imshow('Cat',img)
print(img.shape)

# Masking allows us on focusing on certain parts of an image

blank  = np.zeros((800, 1280),dtype='uint8') # we 
print(blank.shape)
# cv.imshow('Blank',blank)[580 , 580 , 950 , 670],
                                # (width,height)
mask = cv.rectangle(blank.copy(),(580,500),(950,600)  ,255,-1)

#     [580,380,950,450],
#     [580,450,950,530], 
#     [580,500,950,600], 
#     [580,580,950,670],
#     [580,680,850,720]  

# cv.imshow('Mask',mask)
# # this is extremely important that, the dimension of the mask have to be the same size as that of the image
# #otherwise it not goona work properly

# rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

# circle = cv.circle(blank.copy(),(200,200),200,255,-1)
# cv.imshow('Rectangle',rectangle)

# cv.imshow('Circle',circle)



# Bitwise_and = cv.bitwise_and(rectangle,circle)
# cv.imshow('Bitwise And',Bitwise_and)



masked_img = cv.bitwise_and(img,img,mask=mask)

# cv.imshow('Masked Image',masked_img)

gray = cv.cvtColor(masked_img,cv.COLOR_BGR2GRAY) # converting color image to gray image
# cv.imshow('Gray Image',gray)



# blur_image=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur Image',blur_image)

canny=cv.Canny(gray,100,175)
cv.imshow('Canny Image',canny)
adaptive_thresh1 = cv.adaptiveThreshold(gray ,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,5)

cv.imshow("Adaptive Thrshold" , adaptive_thresh1)

text = image_to_string(adaptive_thresh1)


print(text)


cv.waitKey(0)