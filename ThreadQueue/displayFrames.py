#!/usr/bin/env python3

from threading import Thread, Lock, Semaphore
from threadedQueue import Queue
import cv2
import time
import numpy as np
import base64
import os

# Queue for producer and consumer
queue = Queue()

# Producer. Extract converted frames from convertFrames.
class ProducerThread(Thread):
   def run(self):


# Consumer. Display extracted frames.
class ConsumerThread(Thread):
   def run(self):
