# ====================================================================== #
# Purpose: Generating grayscales form 1D data
# Author: Vico Zhang
# Version 1.0 (2022/4/10) Generating the code.
# Version 2.0 (2022/4/10) Revising and Finalizing.
# ====================================================================== #

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
        if line[data_column]:
            data.append(eval(line[data_column]))
        else:
            continue
    file.close()
    return data


def turn_grayscale(data):
    lens = len(data)
    max_start = lens - dimension_grayscale**2
    starts = []
    gray_scales = []
    for i in range(sampling_value):
        while True:
            start = random.randint(0, max_start)
            if start not in starts:
                starts.append(start)
                break
        temp = data[start: start + dimension_grayscale**2]
        temp = np.array(temp)
        gray_temp = temp.reshape(dimension_grayscale, dimension_grayscale)
        gray_scales.append(gray_temp)
    return gray_scales


def draw_grayscale(graydata):
    np.savez(name_npz, *graydata)


def npz_visualization(filename):
    npz_file = np.load(filename, allow_pickle=True)
    for file in npz_file:
        temp = npz_file['{}.npy'.format(file)]
        plt.imshow(temp)
        imageio.imwrite("depth.jpg", temp)
        plt.savefig('temp.jpg')
        plt.show()
        break
    return


def divide_dataset(filename):
    npz_file = np.load(filename, allow_pickle=True)
    for file in npz_file:
        temp = npz_file[file]
        imageio.imwrite("DataSet\\{}.jpg".format(file), temp)
    return


if __name__ == '__main__':
    dimension_grayscale = 256
    data_column = 0
    sampling_value = 500
    name_npz = 'grayscales'
    DataSet = load_data('data.txt')
    graydata_temp = turn_grayscale(DataSet)
    draw_grayscale(graydata_temp)
    # npz_visualization('graydatas.npz')
    divide_dataset(name_npz + '.npz')
    print('success!')

