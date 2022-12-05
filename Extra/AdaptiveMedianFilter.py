import numpy as np


def adaptiveMedianFilter(img, x, y, window_size, Smax):
    """
    Adaptive Median Filter on (x, y) location
    :param img: Image Object
    :param x: coordinate x (count in horizontal direction)
    :param y: coordinate y (count in vertical direction)
    :param window_size: Size of window (Mask) is applied on Image at (x,y) location
    :param Smax: max allowed size of Sxy
    :return: Output value
    """
    mask = img[range(y - window_size // 2, y + window_size // 2 + 1), :][:,
           range(x - window_size // 2, x + window_size // 2 + 1)]
    print("Mask", mask)
    Zmed = np.median(mask)
    Zmax = np.max(mask)
    Zmin = np.min(mask)

    if window_size > Smax:
        return Zmed

    A1 = Zmed - Zmin
    A2 = Zmed - Zmax
    print("A1 = ", A1, "A2 = ", A2)

    if A1 > 0 > A2:
        Zxy = int(img[y, x])
        print("Zxy = ", Zxy)
        B1 = Zxy - Zmin
        B2 = Zxy - Zmax
        print("B1 = ", B1, "B2 = ", B2)

        if B1 > 0 > B2:
            return Zxy
        else:
            return Zmed
    else:
        window_size += 2
        return adaptiveMedianFilter(img, x, y, window_size, Smax)


_img = [
    [130, 127, 125, 127, 125, 125, 127, 125, 127],
    [125, 125, 125, 125, 125, 130, 125, 130, 130],
    [127, 255, 125, 129, 125, 127, 132, 125, 131],
    [130, 129, 127, 0, 130, 125, 130, 125, 127],
    [127, 0, 255, 129, 127, 255, 0, 130, 130],
    [129, 125, 0, 125, 127, 130, 0, 127, 132],
    [130, 129, 129, 129, 130, 0, 125, 130, 127],
    [127, 255, 125, 129, 125, 255, 127, 129, 0],
    [255, 129, 0, 0, 130, 125, 255, 255, 127],
    [130, 0, 255, 129, 127, 255, 255, 129, 127],
    [127, 255, 127, 127, 130, 125, 127, 0, 130],
]
_img = np.array(_img, dtype='uint8')
print(adaptiveMedianFilter(img=_img, x=6, y=8, window_size=3, Smax=7))
