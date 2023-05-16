import cv2 as cv
from cv2 import bitwise_and
import numpy as np
from pytesseract import image_to_string


img = cv.imread(r"save_images_files\photo5.jpg")

from save_into_database import save_info



# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# adaptive_thresh1 = cv.adaptiveThreshold(gray ,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,5)

# cv.imshow("Image" , img)
# cv.waitKey(0)

height , width = img.shape[0],img.shape[1]

# Masking allows us on focusing on certain parts of an image
#  [250,30,950,350],
Roi = [


    [580,380,950,450] ,
    [580,450,950,530] , 
    [580,500,950,600], 
    [580,580,950,670],
    [580,680,950,800]  
]

info = []

for x,y,w,h in Roi:

    blank  = np.zeros((height, width),dtype='uint8') 

    mask = cv.rectangle(blank.copy(),(x,y),(w,h),255,-1)
    masked_img = cv.bitwise_or(img,img,mask=mask)
    gray = cv.cvtColor(masked_img,cv.COLOR_BGR2GRAY) # converting color image to gray image
    adaptive_thresh1 = cv.adaptiveThreshold(gray ,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,5)
    text = image_to_string(adaptive_thresh1)
    text1 = text.strip().replace('\n', '')
    info.append(text1)

my_info = {}

my_info["Student id"] = int(info[0])
my_info["Name"] = info[1]
my_info["Section"] = info[2]
my_info["Program"] = info[3]
my_info["Year of Admission"] = info[4]


print(my_info)


