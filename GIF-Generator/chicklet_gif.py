import imageio.v3 as iio

imageName = ['chicklet1.png','chicklet2.png','chicklet3.png','chicklet4.png']
images = [ ]

for image in imageName:
    images.append(iio.imread(image))

iio.imwrite('chicklet.gif',images,duration = 500,loop=0)


