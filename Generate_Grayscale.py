# ====================================================================== #
# Purpose: Generating grayscales form 1D data
# Author: Vico Zhang
# Version 1.0 (2022/4/10) Generating the code.
# ==================================================================

import numpy as np
import random
import re
import imageio
import matplotlib.pyplot as plt


def load_data(filename):
    data = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        line = line.replace("\n", '')
        line = re.split(r"[ ]+", line)
        if line[0]:
            data.append(eval(line[0]))
        else:
            continue
    file.close()
    return data


def turn_grayscale(data):
    lens = len(data)
    max_start = lens - 4096
    starts = []
    grayscales = []
    for i in range(500):
        while True:
            start = random.randint(0, max_start)
            if start not in starts:
                starts.append(start)
                break
        temp = data[start: start + 4096]
        temp = np.array(temp)
        gray_temp = temp.reshape(64, 64)
        grayscales.append(gray_temp)
    return grayscales


def draw_grayscale(graydata):
    np.savez("graydatas", *graydata)


def npz_visionlization(filename):
    npz_file = np.load(filename, allow_pickle=True)
    for file in npz_file:
        temp = npz_file['{}.npy'.format(file)]
        plt.imshow(temp)
        imageio.imwrite("depth.jpg", temp)
        plt.savefig('temp.jpg')
        plt.show()
        break
    return


if __name__ == '__main__':
    DataSet = load_data('data.txt')
    graydata_temp = turn_grayscale(DataSet)
    draw_grayscale(graydata_temp)
    npz_visionlization('graydatas.npz')
    print('success!')

