import numpy as np
import time
from numba import njit,jit,prange
from PIL import Image, ImageShow, ImagePalette


@njit()
def A(x,i,j):
    start1 = i - 1
    end1 = i + 1
    start2 = j - 1
    end2 = j + 1
    if end2 > 999:
        end2 = 998
    if end1 > 999:
        end1 = 998
    if start1 < 0:
        start1 = 0  
    if start2 < 0 :
        start2 = 0 
    ne = x[start1:end1 + 1,start2:end2 + 1]
    if np.count_nonzero((0<ne) & (ne<7)) >=2 :
        return True
    else:
        return False

@njit()
def l(x,a,b):
    new = np.zeros_like(x)
    for i in range(0,1000):
        for j in range(0,1000):
            a = x[i,j]
            if a == 1 or a == 2 or a== 3 or a == 4 or a == 5 or a == 6:
                new[i,j] = a + 1
            elif a == 0:
                if A(x,i,j) is True:
                    new[i,j] = 1
            elif a == 7:
                new[i,j] = 0
    return new



def loop():
    x = np.random.choice(a = [0,1,2,3,4,5,6,7], p =[0.7,0.3,0,0,0,0,0,0], size = (1000,1000))
    a = np.zeros_like(x)
    b = a.copy()
    palette = []
    im = []
    for i in range(256):
        palette.extend((np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)))
    assert len(palette) == 768 
    for gen in range(0,100):
        x = l(x,a,b)
        im.append(Image.fromarray(x).convert('P'))
    im[0].save('z.gif', save_all=True, append_images=im[1:],
           optimize=True, duration=5, loop=True, palette = palette)
    return 


if __name__ == "__main__":
    c = time.time()           
    loop()
    print(time.time() - c)
