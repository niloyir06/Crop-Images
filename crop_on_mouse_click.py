import cv2
import os
INPUT_DIR = "./input_images"
OUTPUT_DIR = "./output_images"
CROP_HEIGHT = 224
CROP_WIDTH = 224



def onMouse(event, x, y, flags, param):
    global n, mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX,mouseY, n = x,y, event

os.makedirs(OUTPUT_DIR, exist_ok= True)

for image_file in os.listdir(INPUT_DIR):
    img = cv2.imread(os.path.join(INPUT_DIR, image_file))
    filename = os.path.splitext(image_file)[0]
    n = 0
    cv2.namedWindow("image")
    cv2.setMouseCallback('image', onMouse)
    
    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if n == cv2.EVENT_LBUTTONDOWN:
            cv2.destroyAllWindows()    
            break    
    cropped_img = img[mouseY: mouseY + CROP_HEIGHT, mouseX: mouseX + CROP_WIDTH]
    h, w, _ = cropped_img.shape
    
    required_height_padding = max(0,CROP_HEIGHT-h)
    required_width_padding = max(0,CROP_WIDTH-w)

    cropped_img= cv2.copyMakeBorder(cropped_img,0, required_height_padding, 0, required_width_padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename + '.png'), cropped_img)
    
