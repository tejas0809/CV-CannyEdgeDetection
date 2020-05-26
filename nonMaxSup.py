'''
  File name: nonMaxSup.py
  Author:
  Date created:
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''
import utils, helpers
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import signal
from PIL import Image
import interp

def nonMaxSup(Mag, Ori):
  # TODO: your code here
  X,Y=np.meshgrid(np.arange(Mag.shape[1]),np.arange(Mag.shape[0]))
  cosTheta=np.cos(Ori)
  sinTheta=np.sin(Ori)
  xq=X+cosTheta
  yq=Y+sinTheta
  side1=interp.interp2(Mag,xq,yq)
  Ori1=Ori+np.pi
  cosTheta1=np.cos(Ori1)
  sinTheta1=np.sin(Ori1)
  xq1=X+cosTheta1
  yq1=Y+sinTheta1
  side2=interp.interp2(Mag,xq1,yq1)
  grad1=Mag>side2
  grad2=Mag>side1
  ans=(np.logical_and(grad1,grad2))*1
  return ans
