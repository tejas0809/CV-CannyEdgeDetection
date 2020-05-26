'''
  File name: findDerivatives.py
  Author:
  Date created:
'''

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''

import utils, helpers
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import signal
from PIL import Image
def findDerivatives(I_gray):
  # TODO: your code here
  Gausian=utils.GaussianPDF_2D(0.1,1,5,5)
  dx,dy=np.gradient(Gausian,axis=(1,0))
  Ix = signal.convolve2d(I_gray,dx,'same')
  Iy = signal.convolve2d(I_gray,dy,'same')
  Im = np.sqrt(Ix*Ix + Iy*Iy)
  Ori=np.arctan(Iy/Ix)
  return Im,Ix,Iy,Ori
