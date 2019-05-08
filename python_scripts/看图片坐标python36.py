import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
path = input('please enter your pic path: ')
img = plt.imread(path)
plt.imshow(img)
plt.show()
