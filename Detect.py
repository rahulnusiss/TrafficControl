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
      self.labelDict = dict()
      self.routeDict = dict()

  def captureImage(self,count):
      self.camera.start_preview()
      time.sleep(5)
      print('count is {0}' .format(count))
      self.camera.capture('image_' + str(count) +'.jpg')

  def processImage(self,filePath):
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
      
      for label in labels:
          self.labelDict[label.description] = label.score
      print(self.labelDict)
      
  def createJSON(self,routeNo,configFile):
    with open(configFile) as data_file:
      self.routeDict = json.load(data_file)
    for key in self.labelDict.keys():
      if ('congestion' in key):
        if(self.labelDict[key]>0.70):
          self.routeDict[routeNo] = 1
          print('Congestion on {0}' .format(routeNo))
          break
        else:
          self.routeDict[routeNo] = 0
          print('No Congestion')
      
    print self.routeDict
    with open('config.json', 'w') as outfile:
      json.dump(self.routeDict,outfile)

def main():
      detect=Detect()
      count = 1
      while (count<5):
        if len(sys.argv) > 1:
          filePath = sys.argv[1]
          routeNo = sys.argv[2]
          configFile = sys.argv[3]
          detect.processImage(filePath)
          detect.createJSON(routeNo,configFile)
          break
        else:
          detect.captureImage(count)
          path = '/home/pi/Desktop/TrafficCongestion/TrafficControl/image_' + str(count) + '.jpg'
          detect.processImage(path)
          count = count+1
       
          

if __name__ == "__main__":
    main()
















