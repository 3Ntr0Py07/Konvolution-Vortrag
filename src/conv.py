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

def convolve2D(signal: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    '''convolve two 2-dimensional lists of floats \n
    kernel must be smaller than signal in both dimensions'''

    xKernelShape = kernel.shape[0]
    yKernelShape = kernel.shape[1]
    xSignalShape = signal.shape[0]
    ySignalShape = signal.shape[1]

    padding = xKernelShape - 1

    signalPadded = np.zeros((xSignalShape + padding*2, ySignalShape + padding*2))
    signalPadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = signal

    output = np.zeros((signalPadded.shape[0] - padding, signalPadded.shape[1] - padding))

    for y in range(signalPadded.shape[1]):
        for x in range(signalPadded.shape[0]):
            try:
                output[x, y] = (kernel * signalPadded[x: x + xKernelShape, y: y + yKernelShape]).sum()
            except:
                break

    return output


list1 = np.array([[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.]])
list2 = np.full((7,7),.02040816)

#print(convolve2D(list1,list2,padding=2))