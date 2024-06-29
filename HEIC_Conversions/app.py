import os
from PIL import Image
import numpy as np
import cv2
import pillow_heif

print ("initiating batch conversions")
dir = os.getcwd()

for item in os.listdir():
    name, file_extension = os.path.splitext(f"{item}")
    if file_extension.lower() == '.heic':
        print(name, file_extension)

        heif_file = pillow_heif.open_heif(f"{name}.heic", convert_hdr_to_8bit=False, bgr_mode=True)
        np_array = np.asarray(heif_file)
        cv2.imwrite(f"{name}.png", np_array)
