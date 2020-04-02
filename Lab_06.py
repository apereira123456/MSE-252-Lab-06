import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

a = 73
x, r, g, b = np.zeros(a), np.zeros(a), np.zeros(a), np.zeros(a)

def color(imageName):
    
    r, g, b, a, num = 0, 0, 0, 0, 0
    
    im = Image.open(imageName)
    pix = im.load()
    dim = im.size
    
    for i in range(dim[0]):
        for j in range(dim[1]):
            p = pix[i,j]
            r += p[0] ** 2
            g += p[1] ** 2
            b += p[2] ** 2
            a += p[3] ** 2
            num += 1
        
    avg = np.array([np.sqrt(r / num), np.sqrt(g / num), \
                    np.sqrt(b / num), np.sqrt(a / num)])

    return avg

def toTuple(array):
    return tuple(array.astype(int))

def concat_h(im1, im2):
    img = Image.new('RGBA', (im1.width + im2.width, im1.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (im1.width, 0))
    return img

c = color('white.png')
print(c)

c = color('hdpe.png')
print(c)

c = color('hdpe_ps.png')
print(c)

c = color('1.png')
x[0], r[0], g[0], b[0] = 1, c[0], c[1], c[2]

c = toTuple(c)
img = Image.new('RGBA', (100, 2000), color = c)       

for n in range(2,a + 1):
    c = color(str(n) +'.png')
    x[n-1], r[n-1], g[n-1], b[n-1] = n, c[0], c[1], c[2]
    
    c = toTuple(c)
    im = Image.new('RGBA', (100, 2000), color = c)       
    img = concat_h(img, im)
    
img.show()

fig = plt.figure(figsize=(12.80,7.20))

s1 = plt.scatter(x, r, c = 'r')
s2 = plt.scatter(x, g, c = 'g')
s3 = plt.scatter(x, b, c = 'b')

plt.legend((s1, s2, s3), ('Red Intensity', 'Green Intensity', 'Blue Intensity'), \
           loc = 'lower right')
plt.title('RGB Intensity')
plt.xlabel('Extrusion Sample')
plt.ylabel('Intensity')
plt.ylim(0,260)

plt.show()