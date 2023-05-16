from skimage.metrics import structural_similarity
import cv2
import numpy

def predict_score(image_path):

    Original = cv2.imread(image_path)
    tampered = cv2.imread(r"save_images_files\tampered.jpg")

# Convert BGR to RGB
    Original = cv2.cvtColor(Original, cv2.COLOR_BGR2RGB)
    tampered = cv2.cvtColor(tampered, cv2.COLOR_BGR2RGB)

# Resized Image
    Resize_Original = cv2.resize(Original, (800, 1280))
    Resize_tampered = cv2.resize(tampered, (800, 1280))

#       Convert to grayscale
    Original_Gray = cv2.cvtColor(Resize_Original, cv2.COLOR_RGB2GRAY)
    tampered_Gray = cv2.cvtColor(Resize_tampered, cv2.COLOR_RGB2GRAY)

    (score, diff) = structural_similarity(Original_Gray, tampered_Gray, full=True)
    diff = (diff * 255).astype("uint8")

    return f"Score is {numpy.round((score * 100),2)} %"


image_path  = r"save_images_files\photo5.jpg"
p = predict_score(image_path)

print(p)
