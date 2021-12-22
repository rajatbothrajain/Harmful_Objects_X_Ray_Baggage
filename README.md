# Harmful Objects X-Ray Baggage
Identify Harmful Objects in the X-Ray Image of Baggage. 

## Challenges For X-ray Image Object Detection :
 
a) they are transparent, pixel values represent the attenuation by multiple objects

b) they may be very cluttered, which dramatically increases the no of meaningless interest points.

c) Noisy due to low energy X-ray imaging


## Major Challenge : 

1) Train the model on data similar to actual testing data, different X-Ray machines produces different type of images.

2) Too Many Classes & Too Many Different Variations Of Object To Classify and To Less Data To Train

   Popular Datasets available For Training mainly contains only 4 classes of Objects: Knife, Razor/Blade, Shuriken and Gun 
   
   But actual machines used at site contains more than 12 classes of objects : Gun, Knife, Bomb, Scissor, Blade, Spanner,
   Tools, GunParts, Mobile, BatteryBank, Charger, Battery etc.


## Compare Model Trained With Synthetic Data with Model Trained with Real Data :

This code is divided into two parts :

1) [Model Training : Yolov3-tiny ](darknet_yolov3-tiny/README.md)

2) [Synthetic Data Generation : TIP](TIP/README.md)




