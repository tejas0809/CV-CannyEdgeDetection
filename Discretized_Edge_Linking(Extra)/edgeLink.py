'''
  File name: edgeLink.py
  Author:
  Date created:
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map
'''
import utils, helpers
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import signal
from PIL import Image

def edgeLink(M, Mag, Ori):
  # TODO: your code here
  EdgeMap=M*Mag
  mean=np.mean(Mag)
  median=np.median(Mag)
  std_dev=np.std(Mag)
  print('mean:',mean)
  print('median:',median)
  print('std_dev:',std_dev)
  low_threshold=mean*0.7
  high_threshold=mean*1
  strongEdgeMap=EdgeMap>high_threshold
  strongEdgeMap=1*strongEdgeMap
  weakEdgeMap=np.logical_and(EdgeMap<high_threshold,EdgeMap>low_threshold)*1
  weakEdgeMap=1*weakEdgeMap
  OriEdge=Ori+(np.pi*0.5)

  OriEdge[np.logical_and(OriEdge>0,OriEdge<np.pi/8)]=0
  OriEdge[np.logical_and(OriEdge>np.pi/8,OriEdge<np.pi*3/8)]=np.pi/4
  OriEdge[np.logical_and(OriEdge>np.pi*3/8,OriEdge<np.pi*5/8)]=np.pi/2
  OriEdge[np.logical_and(OriEdge>np.pi*5/8,OriEdge<np.pi*7/8)]=np.pi*3/4

  angle0=OriEdge==0
  angle1=OriEdge==np.pi/4
  angle2=OriEdge==np.pi/2
  angle3=OriEdge==np.pi*3/4

  angle0=1*angle0
  angle1=1*angle1
  angle2=1*angle2
  angle3=1*angle3


  ans=strongEdgeMap
  ansOld=np.empty(M.shape)
  # print("stron",np.sum(strongEdgeMap))
  while True:
    zer=np.pad(ans,[[1,1],[1,1]],mode='constant')
    left=zer[1:-1,0:-2]
    right=zer[1:-1,2:]
    up=zer[0:-2,1:-1]
    down=zer[2:,1:-1]
    upleft=zer[0:-2,0:-2]
    downright=zer[2:,2:]
    upright=zer[0:-2,2:]
    downleft=zer[2:,0:-2]
    ans=ans+weakEdgeMap*((angle0*left)+(angle0*right)+(angle1*upright)+(angle1*downleft)+(angle2*up)+(angle2*down)+(angle3*upleft)+(angle3*downright))
    ans=np.asarray(ans,dtype=bool)
    print(np.sum(ans))
    if (ans==ansOld).all():
      # plt.imshow(ans,cmap='gray')
      return ans
    else:
      ansOld=np.asarray(ans, dtype=bool)
