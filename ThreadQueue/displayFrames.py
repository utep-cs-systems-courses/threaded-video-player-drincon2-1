#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import convertFrames
import cv2


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
extract_f = Thread(target = convertFrames.extractFrames, args = (color_queue,))
convert_f = Thread(target = convertFrames.convertFrames, args = (color_queue, gray_queue))
display_f = Thread(target = displayFrames, args = (gray_queue,))

extract_f.start()
convert_f.start()
display_f.start()

