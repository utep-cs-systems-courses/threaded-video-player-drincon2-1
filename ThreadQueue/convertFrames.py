#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2
import os

# Queue for producer and consumer
queue = Queue()

# Producer. Read frames from file.
class ProducerThread(Thread):
   def run(self):


# Consumer. Convert frames to grayscale and send to next producer-consumer.
class ConsumerThread(Thread):
   def run(self):
