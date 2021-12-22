Using Darknet Framework For Training and Testing Yolov3-tiny model.

About Darknet framework: http://pjreddie.com/darknet/

Base Repo              : https://github.com/AlexeyAB/darknet/


# Yolov3-tiny for Windows and Linux

## (neural networks for object detection)

## TOOLS USED
    * Language
        python3
        C++
        
    * Libraries
        opencv
        numpy
        matplotlib
        pillow
        skimage
        cuda


## How to compile on Linux (using make) : make -j 4; make

Just run make, to build the darknet binary. Validate the path of Libraries in Makefile.

## Using Pre-Trained Models For Training :
1) TEST/weights/yolov3-tiny_synthetic.weights: Model Trained on Synthetic Image Dataset
2) TEST/weights/yolov3-tiny_real.weights     : Model Trained on Real Image Dataset
   
Note: Both the model training involves transfer learning by using the pre-trained weights of imagenet dataset 

(TEST/weights/yolov3-tiny.weights)

## Files Path :
TEST/cfg/yolov3-tiny.data     : Contains the Paths of TestDataset, TrainDataset, labels path and weight stored path

TEST/cfg/yolov3-tiny_test.cfg : Contains network architecture used for Training. We have configured this architecture 
                                for detection of 4 classes.
                                
Params: cfg/yolov3-tiny.data

classes : No of Classes For Which Model is to be trained 

train   : Training Folder File Path

valid   : Testing Folder File Path

names   : Labels Names

backup  : Path where training weights are stored


                                
## Classes Detected By Model : 4 Classes
0 -> Gun

1 -> Knife

2 -> Razor

3 -> Shuriken


## Training : On Train Path Configured in yolov3-tiny.data

./darknet detector train ./TEST/cfg/yolov3-tiny.data ./TEST/cfg/yolov3-tiny.cfg  ./TEST/weights/yolov3-tiny.weights -dont_show 

-dont_show {Optional} : Disable GUI Display Component of Code 


## Testing : On Testing Path Configured in yolov3-tiny.data

./darknet detector map ./TEST/cfg/yolov3-tiny.data  ./TEST/cfg/yolov3-tiny.cfg  ./TEST/weights/yolov3-tiny.weights -dont_show

-dont_show {Optional} : Disable GUI Display Component of Code 



```
