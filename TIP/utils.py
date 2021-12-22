
import numpy as np
from PIL import Image,ImageDraw
import random
import cv2

def seperate_background(img_name,threshold=100):
    # https://stackoverflow.com/questions/5365589/white-background-to-transparent-background-using-pil-python
    
    dist=5
    # print(img_name)
    img=Image.open(img_name).convert('RGBA')
    # img = img.rotate(100)
    # np.asarray(img) is read only. Wrap it in np.array to make it modifiable.
    arr=np.array(np.asarray(img))
    r,g,b,a=np.rollaxis(arr,axis=-1)    
    mask=((r>threshold)
        & (g>threshold)
        & (b>threshold)
        & (np.abs(r-g)<dist)
        & (np.abs(r-b)<dist)
        & (np.abs(g-b)<dist)
        )
    arr[mask,3]=0
    img=Image.fromarray(arr,mode='RGBA')
    img.rotate(90)
    img.save('tmpc.png')
    return 'tmpc.png'



def rotate_image(img_path):
    """
    Rotate image by random angle theta
    """
    angle= random.randint(0,360)
    Image.open(img_path).rotate(angle,expand=True).save('tmpr.png')
    return 'tmpr.png'

def FillHole(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    len_contour = len (contours)
    contour_list = []
    for i in range(len_contour):
        drawing = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv2.drawContours(drawing, contours, i, (255, 255, 255), -1)
        contour_list.append(img_contour)

    out = sum(contour_list)
    return out

def morpholize_image(img_path):
    """
    Takes an image path and returns a binarized image with all morphological operation as in paper
    """
    # img = cv2.imread(img_path)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    ### 1. Binarize image by thresholding
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,img_bin = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

    ### 2. Dilation
    img_dilated = cv2.dilate(img_bin.copy(), None)

    ### 3.Hole Filling 
    img_filled = FillHole(img_dilated)

    ### 4. Erosion

    img_eroded = cv2.erode(img_filled.copy(), None)
    return img_eroded



def rect(image, shape):
    draw = ImageDraw.Draw(image)
    draw.rectangle(shape,outline='red',width=10)
    return image

def get_bounding_box(threat,background):
    """
    Finds best insertion point and returns the bounding box
    Algorithm/Logic


    Since we know the size. and our morpohlogicalized image all has 255 in the region of interest
    We can simply check if the end position of the threat image has value 255.
    So we can check the total of 4 coordinates

    """
    count  = 0
    W,H = threat.size
    total_checks = 1
    is_not_valid = True

    x,y = background.nonzero() # Non zero index
    max_possible_insertion_points = len(x)

    RETRY = 1000
    # Finding valid points for insertion
    while is_not_valid and RETRY!=0:
        RETRY-=1
        print(RETRY)
        rand_point = np.random.randint(max_possible_insertion_points)
        # print(f"Testing on point = ({x[rand_point]},{y[rand_point]})")
        
        ## Check if the position is good.
        ## Algorithm (not given in ppaer,)
        """
        Since we know the size. and our morpohlogicalized image all has 255 in the region of interest
        We can simply check if the end position of the threat image has value 255.
        So we can check the total of 4 coordinates
        """
        positions_to_check  =  [
            (x[rand_point], y[rand_point]), # TOP LEFFT
            (x[rand_point] + W, y[rand_point]), # TOP Right
            (x[rand_point], y[rand_point] + H), # Bottom LEFFT
            (x[rand_point] + W, y[rand_point] + H), # Bottom Right
        ]
        # print(f'Bounding box: {positions_to_check}')
        
        for points in positions_to_check:
            # if image superposition is outside the target image. We will get an error. Handle it pythonic way
            # otherwise check all pixels have 255 value
            try:
                if background[points]==255: # valid point
                    is_not_valid = False
                else:
                    is_not_valid = True
            except:
                # print(f'{points} is outside bounds of Target image. Stopping check for this point')
                is_not_valid = True
                break
        # result = "Valid" if is_not_valid==False else "Invalid"
        # print(f'Verdict:{result}\n')              
                    
        total_checks+=1
    bbox = positions_to_check
    if RETRY==0:
        raise Exception('Error')
    return bbox



def insert_image(threat_path, background_path,threshold=100):
    """
    Insert threat into background. Returns the image and the bbox
    """
    # morpholize background image to find insertion point
    img_morpholized = morpholize_image(background_path)
    
    # read background image to use for insertion
    background = Image.open(background_path).convert('RGB')

    # Read and rotate and threshold threat image
    img_clean  = seperate_background(threat_path,threshold) # image with background removed
     
    img_rotated  = rotate_image(img_clean) # Rotate randomly for diversity
    img = Image.open(img_rotated) # Read rotated and final threat image
    
    bbox = get_bounding_box(img,img_morpholized) # find bounding boxes
    
    temp_back = background.copy()

    temp_back.paste(img, bbox[0], img)
    tenp_no_bbox = temp_back.copy()

    temp_back = rect(temp_back, shape = [bbox[0],bbox[-1]])
    return tenp_no_bbox, temp_back ,bbox