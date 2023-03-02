import numpy as np
from scipy.signal import convolve2d

def convolve1D(list1: list[float], list2: list[float]) -> list[float]:
    '''convolve two 1-dimensional lists of floats\n
    padding is ignored'''
    
    #swap lists if necessary
    if list1 < list2: 
        list1, list2 = list2, list1

    #preallocate convolved list 
    convolution = (len(list1) - len(list2)) * [0.0]

    for l in range(len(convolution)):
        for i in range(len(list2)):
            convolution[l] += list1[l - i + len(list2)] * list2[i]
    return convolution

def convolve2D(signal: np.ndarray, kernel: np.ndarray, padding = 0) -> np.ndarray:
    '''convolve two 2-dimensional lists of floats \n
    kernel must be smaller than signal in both dimensions'''

    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = signal.shape[0]
    yImgShape = signal.shape[1]

    xOutput = int(((xImgShape - xKernShape + 2 * padding)) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding)) + 1)
    output = np.zeros((xOutput, yOutput))

    if padding != 0:
        signalPadded = np.zeros((signal.shape[0] + padding*2, signal.shape[1] + padding*2))
        signalPadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = signal
    else:
        signalPadded = signal

    for y in range(signalPadded.shape[1]):
        for x in range(signalPadded.shape[0]):
            output[x, y] = (kernel * signalPadded[x: x + xKernShape, y: y + yKernShape]).sum()

    return output


list1 = np.array([[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.]])
list2 = np.full((7,7),.02040816)

#print(convolve2D(list1,list2,padding=2))