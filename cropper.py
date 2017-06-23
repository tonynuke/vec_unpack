import cv2
import os
import json

JSON_PATH = 'jsons/'
IMG_PATH = '/home/tony/samples/anton/'
SAMPLES_PATH = 'rgb_samples/'

# all json files with object coordinates
jsons = os.listdir(JSON_PATH)
print('Total', len(jsons))

# arr = []


#  check scaling
def check_scale(x, y, w, h):
    scale = h / w

    # arr.append(scale)

    if scale > 2:
        t = scale / 2
        _w = w * t

        indent = (_w - w)/2
        w += indent*2
        x -= indent

    elif scale < 2:
        t = scale / 2
        _h = h * t

        indent = (_h - h) / 2
        h += indent*2
        y -= indent

    return int(x), int(y), int(w), int(h)


# crop picture with params
def picture_crop(image_name, x, y, w, h, class_name):

    x, y, w, h = check_scale(x, y, w, h)

    img = cv2.imread(image_name)
    crop_img = img[y:y + h, x:x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400
    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

    fname = ''.join([SAMPLES_PATH, class_name, '.jpg'])
    cv2.imwrite(fname, crop_img)


for js in jsons:
    json_path = JSON_PATH + js
    # print(json_path)

    with open(json_path) as data_file:
        count = 0

        data = json.load(data_file)
        # print(data)

        for description in data:
            annotation = description['annotations']

            filename = IMG_PATH + description['filename'].split('/')[-1]
            print(filename)

            if len(annotation) > 0:
                for tag in annotation:
                    # print(tag)
                    x = int(tag['x'])
                    y = int(tag['y'])
                    h = int(tag['height'])
                    w = int(tag['width'])
                    class_name = js

                    # print(class_name, x, y, w, h)

                    picture_crop(filename, x, y, w, h, class_name + '_' + str(count))
                    count += 1

## min scaling
# print(min(arr))