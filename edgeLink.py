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
import interp

def edgeLink(M, Mag, Ori):
  # TODO: your code here
  edgeMap=M*Mag
  updatedMap=edgeMap
  mean=np.mean(Mag)
  median=np.median(Mag)
  std_dev=np.std(Mag)
  # print("mean",mean)
  # print("median",median)
  # print("dev",std_dev)
  # low_threshold=int(max(0, (1.0 - sigma) * np.median(Mag)))
  # high_threshold=int(min(255, (1.0 + sigma) * np.median(Mag)))
  high_threshold=mean*0.9
  low_threshold=mean*0.65
  print("high",high_threshold)
  print("low",low_threshold)
  # high_threshold=np.mean(Mag)*0.8
  # low_threshold=np.mean(Mag)
  strongEdgeMap=(edgeMap>high_threshold)*1
  weakEdgeMap=np.logical_and(edgeMap>low_threshold,edgeMap<high_threshold)*1

  X,Y=np.meshgrid(np.arange(M.shape[1]),np.arange(M.shape[0]))

  OriEdge1=Ori+(np.pi/2)
  x1=X+np.cos(OriEdge1)
  y1=Y+np.sin(OriEdge1)
  OriEdge2=Ori-(np.pi/2)
  x2=X+np.cos(OriEdge2)
  y2=Y+np.sin(OriEdge2)

  edge1x=weakEdgeMap*x1
  edge1y=weakEdgeMap*y1
  edge2x=weakEdgeMap*x2
  edge2y=weakEdgeMap*y2

  strongEdgeMap_old=np.empty(strongEdgeMap.shape)
  weakEdgeMap_new=weakEdgeMap
  while True:
    side1=weakEdgeMap_new*(interp.interp2(updatedMap,edge1x,edge1y)>high_threshold)
    side2=weakEdgeMap_new*(interp.interp2(updatedMap,edge2x,edge2y)>high_threshold)
    sides=np.asarray(side1+side2,dtype=bool)
    updatedMap=edgeMap+sides*high_threshold
    weakEdgeMap_new=weakEdgeMap-sides
    strongEdgeMap=np.asarray(strongEdgeMap+sides,dtype=bool)
    edge1x=weakEdgeMap_new*x1
    edge1y=weakEdgeMap_new*y1
    edge2x=weakEdgeMap_new*x2
    edge2y=weakEdgeMap_new*y2
    # print(np.sum(strongEdgeMap))
    if(strongEdgeMap_old==strongEdgeMap).all():
      return strongEdgeMap
    else:
      strongEdgeMap_old=strongEdgeMap
