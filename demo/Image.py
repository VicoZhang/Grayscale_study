import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import imageio


Alldata = np.load('graydatas.npz', allow_pickle=True)
for file in Alldata:
    temp = Alldata['{}.npy'.format(file)]
    plt.imshow(temp)
    imageio.imwrite("depth.jpg", temp)
    plt.savefig('temp.jpg')
    plt.show()
    break

    # 若要将图像存为灰度图，可以执行如下两行代码
    # import scipy.misc
    # scipy.misc.imsave("depth.png", depthmap)


