class Queue:
   
   def init(self):
      self.frames = []
   
   def isEmpty(self):
      if len(self.size()) == 0:
         return true
      else:
         return false
   
   def enqueue(self, frame):
      self.frames.append()
   
   def dequeue(self):
      temp_frame = self.frame[0]
      self.frame.remove(temp_frame)
      return temp_frame
      
   def size(def):
      return len(self.frames)
   
   
      
