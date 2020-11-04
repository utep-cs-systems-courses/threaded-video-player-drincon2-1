#!/usr/bin/env python3

from threading import Lock, Semaphore

class Queue:
   
   def init(self):
      self.frame_queue = []
      self.lock = Lock()
      self.full = Semaphore(0)
      self.empty = Semaphore(10)
      
   def enqueue(self, frame):
      self.empty.acquire()
      self.lock.acquire()
      self.frame_queue.append(frame)
      self.lock.release()
      self.full.release()
   
   def dequeue(self):
      self.full.acquire()
      self.lock.acquire()
      frame = self.frame_queue[0]
      self.frame_queue.remove(frame)
      self.lock.release()
      self.empty.release()
      return frame
