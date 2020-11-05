#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2


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
      

# Display extracted frames.
def displayFrames(gray_queue):
   # Frame delay
   frameDelay = 42
   # Initialize frame count
   count = 0
   # load the frame
   frame = gray_queue.dequeue()

   while frame is not None:
      print(f'Displaying frame {count}')
      # Display the frame in a window called "Video"
      cv2.imshow('Video', frame)

      # Wait for 42 ms and check if the user wants to quit
      if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
         break    

      count += 1
      
      # Load the next frame file
      frame = gray_queue.dequeue()

   # make sure we cleanup the windows, otherwise we might end up with a mess
   cv2.destroyAllWindows()
      
      
# Producer-consumer thread setup
# Color frame queue
color_queue = Queue()
# Gray frame queue
gray_queue = Queue()
# Threads
extract_f = Thread(target = extractFrames, args = (color_queue,))
convert_f = Thread(target = convertFrames, args = (color_queue, gray_queue))
display_f = Thread(target = displayFrames, args = (gray_queue,))

extract_f.start()
convert_f.start()
display_f.start()

