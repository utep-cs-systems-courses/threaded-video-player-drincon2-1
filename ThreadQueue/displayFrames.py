#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2
import time

# Queue for producer and consumer
displayQueue = Queue()

# Producer. Extract converted frames from convertFrames.
class ProducerThread(Thread):
   def __init__(self, q):
      self.queue = q
      
   def run(self):
      global displayQueue
      # TODO use semaphore to get signal from convertFrames consumer
      
      # initialize frame count
      count = 0

      # Generate the filename for the first frame 
      frameFileName = self.queue.dequeue()
      # Pass current converted frame to displayQueue
      displayQueue.enqueue(frameFileName)
      # TODO use semaphore to signal consumer 
      

# Consumer. Display extracted frames.
class ConsumerThread(Thread):
   def run(self):
      global displayQueue
      # TODO use semaphore to get signal from producer
      # load the frame
      frame = cv2.imread(displayQueue.dequeue())

      while frame is not None:
    
         print(f'Displaying frame {count}')
         # Display the frame in a window called "Video"
         cv2.imshow('Video', frame)

         # Wait for 42 ms and check if the user wants to quit
         if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break    
    
         # get the next frame filename
         count += 1
         # TODO use semaphore to get signal from producer
         frameFileName = displayQueue.dequeue()

         # Read the next frame file
         frame = cv2.imread(frameFileName)

      # make sure we cleanup the windows, otherwise we might end up with a mess
      cv2.destroyAllWindows()
