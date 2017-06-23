import struct,array
import subprocess
import cv2
import numpy as np
import os


# create sample using opencv create samples
def create_samples():
    command = \
        'opencv_createsamples ' \
        '-img ~/Загрузки/dobr.jpg ' \
        '-num 100 ' \
        '-vec samples1.vec ' \
        '-maxxangle 0.6 ' \
        '-maxyangle 0 ' \
        '-maxzangle 0.3 ' \
        '-maxidev 100 ' \
        '-bgcolor 0 ' \
        '-bgthresh 0 ' \
        '-w 150 ' \
        '-h 300'

    os.system(command)
    # test = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE)
    # output = test.communicate()[0]


# unpack vec to images
def showvec(fn, width=150, height=300, resize=2.0):
    f = open(fn, 'rb')
    HEADERTYP = '<iihh' # img count, img size, min, max

    # read header
    imgcount, imgsize, _, _ = struct.unpack(HEADERTYP, f.read(12))

    for i in range(imgcount):
        img = np.zeros((height, width), np.uint8)

        f.read(1) # read gap byte

        data = array.array('h')

        ###  buf = f.read(imgsize*2)
        ###  data.fromstring(buf)

        data.fromfile(f, imgsize)

        for r in range(height):
            for c in range(width):
                img[r, c] = data[r * width + c]

        img = cv2.resize(img, (0, 0), fx=resize, fy=resize, interpolation=cv2.INTER_LINEAR)
        # cv2.imshow('vec_img', img)

        #save img
        fname = ''.join(['samples/', 'img', str(i), '.jpg'])
        cv2.imwrite(fname, img)

        # k = 0xFF & cv2.waitKey(0)
        # if k == 27:         # esc to exit
        #     break

# create_samples()
showvec('samples.vec')