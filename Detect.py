import io
import os
import time
import picamera
import sys
import json

from google.cloud import vision

class Detect:
  def __init__(self):
      self.camera=picamera.PiCamera()
      # Instantiates a client
      self.vision_client = vision.Client()
      # Instantiates a empty Dictionary
      self.labelDictForRoute1 = dict()
      self.labelDictForRoute2 = dict()
      self.routeDict = dict()
      self.congestionPresentonRoute1 = False
      self.congestionPresentonRoute2 = False

  def captureImage(self,count):
      self.camera.start_preview()
      time.sleep(5)
      print('count is {0}' .format(count))
      self.camera.capture('image_' + str(count) +'.jpg')

  def processImage(self,filePath,routeNo):
      # The name of the image file to annotate
      file_name = os.path.join(
       os.path.dirname(__file__), filePath)
      # Loads the image into memory
      with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = self.vision_client.image(content=content)
        # Performs label detection on the image file
        labels = image.detect_labels()
        print('Labels:')
      if routeNo==1:
        for label in labels:
          self.labelDictForRoute1[label.description] = label.score
        print('Labels for Route 1:')
        print(self.labelDictForRoute1)
      if routeNo==2:
        for label in labels:
          self.labelDictForRoute2[label.description] = label.score
        print('Labels for Route 2:')
        print(self.labelDictForRoute1)  
      
      
  def createJSON(self,configFile):
    with open(configFile) as data_file:
      self.routeDict = json.load(data_file)
      
    for key in self.labelDictForRoute1.keys():
      if('congestion' in key):
        self.congestionPresentonRoute1 = True
        break
    for key in self.labelDictForRoute2.keys():
      if('congestion' in key):
        self.congestionPresentonRoute2 = True
        break    

    if self.congestionPresentonRoute1 == True:
      self.routeDict["Route1"] = 1
    else:
      self.routeDict["Route1"] = 0

    if self.congestionPresentonRoute2 == True:
      self.routeDict["Route2"] = 1
    else:
      self.routeDict["Route2"] = 0 
      
    with open(configFile, 'w') as outfile:
      json.dump(self.routeDict,outfile)

def main():
      detect=Detect()
      count = 1
      while (count<5):
        if len(sys.argv) > 1:
          filePath_1 = sys.argv[1]
          filePath_2 = sys.argv[2]
          configFile = sys.argv[3]
          detect.processImage(filePath_1,1)
          detect.processImage(filePath_2,2)
          detect.createJSON(configFile)
          break
        else:
          detect.captureImage(count)
          path = '/home/pi/Desktop/TrafficCongestion/TrafficControl/image_' + str(count) + '.jpg'
          detect.processImage(path)
          count = count+1
       
          

if __name__ == "__main__":
    main()
















