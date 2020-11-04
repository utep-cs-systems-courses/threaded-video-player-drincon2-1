#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2
import os


# Read frames from file and extract them.
def extractFrames(color_queue):
   # File
   clipFileName = 'clip.mp4'
   # Initialize frame count
   count = 0
   # Open the video clip
   vidcap = cv2.VideoCapture(clipFileName)

   # Read one frame
   success,image = vidcap.read()
   print(f'Reading frame {count} {success}')
   
   while success:
      # Put read frame into gray_queue
      color_queue.enqueue(image)
      
      # Read next frame of file  
      success,image = vidcap.read()
      print(f'Reading frame {count}')
              
      count += 1      
      

# Convert frames to grayscale and send to next producer-consumer.
def convertFrames(color_queue, gray_queue):
   # Initialize frame count
   count = 0

   # Load the next frame
   inputFrame = color_queue.dequeue()

   while inputFrame is not None:
      print(f'Converting frame {count}')

      # Convert the image to grayscale
      grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
    
      # Put converted frame into gray_queue
      gray_queue.enqueue(grayscaleFrame)
      
      count += 1
    
      # Load the next frame
      inputFrame = color_queue.dequeue() 

