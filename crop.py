from PIL import Image
from os.path import basename
import os


def crop(path_to_image, x, y, save_path):
    img = Image.open(path_to_image)
    img_width, img_height = img.size
    crop_width = img_width / x
    crop_height = img_height / y
    save_file_name = os.path.splitext(basename(path_to_image))[0]
    save_file_extension = os.path.splitext(basename(path_to_image))[1]
    count = 0
    for i in range(x):
        for j in range(y):
            count += 1
            crop_area = (i*crop_width, j*crop_height, (i+1)
                         * crop_width, (j+1)*crop_height)
            cropped_img = img.crop(crop_area)
            cropped_img.save(save_path + save_file_name +
                             "." + str(count)+save_file_extension)
