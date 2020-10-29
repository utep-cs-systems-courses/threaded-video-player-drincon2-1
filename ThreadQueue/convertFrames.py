#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2
import os
import displayFrames

# Queue for producer and consumer
convertQueue = Queue()
# Queue for consumer and displayFrames consumer
sendQueue = displayFrames.ProducerThread(Queue())
# Output dir
outputDir = 'frames'


# Producer. Read frames from file.
class ProducerThread(Thread):
   # Extract frames from file, and read frames
   def run(self):
      global convertQueue, outputDir
      
      # File
      clipFileName = 'clip.mp4'
      # Initialize frame count
      count = 0
      # Open the video clip
      vidcap = cv2.VideoCapture(clipFileName)

      # Create the output directory if it doesn't exist
      if not os.path.exists(outputDir):
         print(f"Output directory {outputDir} didn't exist, creating")
         os.makedirs(outputDir)

      # Read one frame
      success,image = vidcap.read()

      print(f'Reading frame {count} {success}')
      while success and count < 72:

         # Write the current frame out as a jpeg image
         cv2.imwrite(f"{outputDir}/frame_{count:04d}.bmp", image)   
         success,image = vidcap.read()
         print(f'Reading frame {count}')
         
         # Pass current frame to convertQueue
         convertQueue.enqueue(f"{outputDir}/frame_{count:04d}.bmp")
         # TODO use semaphore to signal consumer
         
         count += 1


# Consumer. Convert frames to grayscale and send to next producer-consumer.
class ConsumerThread(Thread):   
   # Get read frame from queue
   def getFrame(self, frames):
      global convertQueue
      return convertQueue.dequeue()
   
   # Convert frame to grayscale  
   def run(self):
      global convertQueue, outputDir, sendQueue
      # TODO use semaphore to get signal from Producer

      # Initialize frame count
      count = 0

      # Get the next frame file name
      inFileName = self.getFrame()

      # Load the next file
      inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

      while inputFrame is not None and count < 72:
         print(f'Converting frame {count}')

         # Convert the image to grayscale
         grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
    
         # Generate output file name
         outFileName = f'{outputDir}/grayscale_{count:04d}.bmp'

         # Write output file
         cv2.imwrite(outFileName, grayscaleFrame)
         # Send converted frame to displayFrames producer queue
         sendQueue.ProducerThread.enqueue(outFileName)
         # TODO use semaphore to signal displayFrames producer

         count += 1

         # TODO use semaphore to get signal from Producer
         # Generate input file name for the next frame
         inFileName = self.getFrame()
    
         # Load the next frame
         inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)
