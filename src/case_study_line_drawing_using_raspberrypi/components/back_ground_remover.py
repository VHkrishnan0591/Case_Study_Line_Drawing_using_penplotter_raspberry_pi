from rembg import remove
import numpy as np
import cv2
import matplotlib as plt
from src.case_study_line_drawing_using_raspberrypi.constants import *
from src.case_study_line_drawing_using_raspberrypi.utils.commons import read_yaml
class Backgroundremover:
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

    def background_remover(self, input):
        output = remove(input)
        height, width = output.shape[:2]
        # Create a white background (255, 255, 255 for RGB white)
        background = np.ones((height, width, 3), dtype=np.uint8) * 255
        rgb = output[:, :, :3]
        alpha = (output[:, :, 3] / 255.0)  # Normalize alpha to 0-1 range

        # Overlay the RGB array onto the white background using alpha transparency
        for c in range(3):
            background[:, :, c] = (alpha * rgb[:, :, c] + (1 - alpha) * background[:, :, c]).astype(np.uint8)
        image = background
        return image
    
    def watermark_at_top_right(self, image):
        logo = cv2.imread(self.config['logo_file']['path'])
        image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        logo = cv2.resize(logo, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
        h1, w1, _ = image.shape
        h2, w2, _ = logo.shape
        # Calculate the position to place the smaller image on the larger image
        x_offset = w1 - w2
        y_offset = 0
        roi = image[y_offset:y_offset+h2, x_offset:x_offset+w2]
        result = cv2.addWeighted(roi, 0.8, logo, 0.2, 0)
        image[y_offset:y_offset+h2, x_offset:x_offset+w2] = result
        return image
    
    def watermark_at_centre(self,image):
        logo = cv2.imread(self.config['logo_file']['path'])
        image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        logo = cv2.resize(logo, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
        h1, w1, _ = image.shape
        h2, w2, _ = logo.shape
        h1, w1, _ = image.shape
        h2, w2, _ = logo.shape
        print(image.shape)
        print(logo.shape)
        cx ,cy = int(w1/2) , int(h1/2)
        left_x = cx - int(w2/2)
        right_x = left_x + w2
        top_y = cy - int(h2/2)
        bottom_y = top_y + h2
        roi = image[top_y:bottom_y,left_x:right_x]
        addweighted = cv2.addWeighted(roi,0.8, logo,0.3,0)
        image[top_y:bottom_y,left_x:right_x] = addweighted
        return image
