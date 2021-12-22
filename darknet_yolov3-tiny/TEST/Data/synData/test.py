import csv
import cv2
import os

def getClass(className):
  classNum = -1
  if(className == "gun"):
    classNum = 0

  if(className == "knife"):
    classNum = 1

  if(className == "rajor blade"):
    classNum = 2

  if(className == "shuriken"):
    classNum = 3

  return classNum



with open('labels.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  extract_count = 0
  for row in csv_reader:
    line_count += 1
    print(f'Processed {line_count} lines.')
    if(line_count == 100000):
      break
    '''row1 =[]
    for val in row:
      if val!="":
        row1.append(int(float(val)))
    row = row1'''
    counter = 1
    idx = 0
    while(counter):
      counter = counter - 1
      if line_count == 1:
        print("Ignore First Row !")
      else:
        print("Row Size:", row)
        val = row[1]
        filePath = val
        if not(os.path.isfile(filePath)):
          print("Skipping:", filePath)
          continue
        else :
          print("Extract:", filePath)

        pos      = filePath.rfind(".")
        outputFile = filePath[0:pos] + ".txt"
        img      = cv2.imread(filePath)
        imageH   = img.shape[0]
        imageW   = img.shape[1] 
        Label    = 0
        print("Idx:", idx)
        #[1,2, 3,4,5,6, 7,8]
        xval = row[1::2]
        print("Xval:", xval)
        yval = row[2::2]
        print("Yval:", yval)
        extract_count = extract_count + 1
        label    = row[2] 
        Xmin     = int(row[3])
        Ymin     = int(row[4])
        Xmax     = int(row[5])
        Ymax     = int(row[6])
        x_center = ((Xmin+Xmax)/2.0)/imageW
        y_center = ((Ymin+Ymax)/2.0)/imageH
        width    = (Xmax-Xmin)/imageW
        height   = (Ymax-Ymin)/imageH
        fileObj  = open(outputFile, 'a')
        line = str(getClass(label)) + " " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height) 
        fileObj.write(line)
        fileObj.write("\n")
        fileObj.close()
        print("File:", filePath, "Label:", Label, "Coordinates(" , Xmin, Ymin,")" , "(", Xmax, Ymax,")")
        #if(len(row)>7 and idx==0):
        #idx = 4 
        #counter = counter + 1
