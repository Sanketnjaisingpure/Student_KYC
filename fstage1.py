import cv2
import pytesseract
from PIL import Image
import os


def extract_text_from_image(image_path):
    image = cv2.imread(image_path)

    # Preprocessing the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (1080, 1080))
    image = cv2.resize(image, (1080, 1080))

    edged = cv2.Canny(image, 68, 37)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w > 250 and h > 250:
            idx += 1
            new_img = image[y:y + h, x:x + w]
            new_img = cv2.resize(new_img, (1000, 600))

    gaussian_blur = cv2.GaussianBlur(new_img, (9, 9), 5)
    sharpened1 = cv2.addWeighted(new_img, 5.5, gaussian_blur, -4.5, 0)

    regions = [
        [442, 288, 641, 329],
        [450, 330, 815, 404],
        [445, 403, 605, 450],
        [446, 446, 705, 517],
        [440, 515, 604, 564]
    ]

    # Save the preprocessed image in the upload folder
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'saved_data')
    image_path = os.path.join(UPLOAD_FOLDER, "1.png")
    cv2.imwrite(image_path, sharpened1)

    # Read the saved image with Pillow library
    image = Image.open(image_path)

    info = []
    for region in regions:
        cropped_image = image.crop(region)
        text1 = pytesseract.image_to_string(cropped_image)
        text = text1.strip().replace('\n', '')
        info.append(text)
        
    
    my_info = {}
    my_info = {
        "Student id": int(info[0]),
        "Name": info[1],
        "Section": info[2],
        "Program": info[3],
        "Year of Admission": info[4],
    }

         
    return my_info


     




def extract_id_from_image(image_path):

    my_info = extract_text_from_image(image_path)

    return my_info['Student id']
    

