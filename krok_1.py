import os
import rawpy
import matplotlib.pylab as plt



path = r"C:\Users\User\Desktop\zachod_rgb\zdjecia"


for n in os.listdir(path):
    pw = str(os.path.join(path, n))
    raw = rawpy.imread(pw)
    image = raw.raw_image
    rgb = raw.postprocess()
    plt.imsave(str(n)[0:len(n)-4] + ".tiff",rgb)
    