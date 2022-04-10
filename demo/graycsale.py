import scipy.io as io
import numpy as np
import random
import sys

normal_0 = io.loadmat("normal/97.mat")["X097_DE_time"].tolist()
normal_1 = io.loadmat("normal/98.mat")["X098_DE_time"].tolist()
normal_2 = io.loadmat("normal/99.mat")["X099_DE_time"].tolist()
normal_3 = io.loadmat("normal/100.mat")["X100_DE_time"].tolist()
normal = [normal_0, normal_1, normal_2, normal_3]

all_data = [normal]
print(len(all_data))


def main(argv=None):
    classes = "normal"

    train_pics = []
    train_labels = []
    test_pics = []
    test_labels = []

    for data_type in range(1):
        # 二类
        # if data_type == 0:
        #     the_type = 0
        # else:
        #     the_type = 1
        # 四类
        # the_type = (data_type + 2) // 3
        # 十类
        the_type = data_type
        data = all_data[data_type-1]
        for load_type in range(4):
            load_data = data[load_type]
            max_start = len(load_data) - 4096
            starts = []
            # 生成训练集
            for i in range(500):
                # 随机一个start，不在starts里，就加入
                while True:
                    start = random.randint(0, max_start)
                    if start not in starts:
                        starts.append(start)
                        break
                # 将4096个数据点转化成64×64的二维图
                temp = load_data[start: start + 4096]
                temp = np.array(temp)
                train_pics.append(temp.reshape(64, 64))
                train_labels.append(the_type)
            # 生成测试集
            for i in range(100):
                while True:
                    start = random.randint(0, max_start)
                    if start not in starts:
                        starts.append(start)
                        break
                temp = load_data[start: start + 4096]
                temp = np.array(temp)
                test_pics.append(temp.reshape(64, 64))
                test_labels.append(the_type)

        print("train_pics", len(train_pics))
        print("train_labels", len(train_labels))
        print("test_pics", len(test_pics))
        print("test_labels", len(test_labels))

    np.savez("train_pics", *train_pics)
    np.savez("train_labels", *train_labels)
    np.savez("test_pics", *test_pics)
    np.savez("test_labels", *test_labels)

    print("save success")
    print(train_pics)


if __name__ == "__main__":
    sys.exit(main())
