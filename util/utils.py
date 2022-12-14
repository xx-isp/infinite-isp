import random
import numpy as np


def introduce_defect(img, total_defective_pixels, padding):
    
    """
    This function randomly replaces pixels values with extremely high or low pixel values to create dead pixels (Dps).
    Note that the defective pixel values are never introduced on the periphery of the image to ensure that there 
    are no adjacent DPs. 
    
    Parameters
    ----------
    img: 2D ndarray
    total_defective_pixels: number of Dps to introduce in img.
    padding: bool value (set to True to add padding)
    
    Returns
    -------
    defective image: image/padded img containing specified (by TOTAL_DEFECTIVE_PIXELS) 
    number of dead pixels.
    orig_val: ndarray of size same as img/padded img containing original pixel values in place of introduced DPs 
    and zero elsewhere. 
    """
    
    if padding:
        padded_img = np.pad(img, ((2,2), (2,2)), "reflect")
    else:
        padded_img  = img.copy()
   
    orig_val   = np.zeros((padded_img.shape[0], padded_img.shape[1])) 
    
    while total_defective_pixels:
        defect     = [random.randrange(1,15), random.randrange(4081, 4095)]   # stuck low int b/w 1 and 15, stuck high float b/w 4081 and 4095
        defect_val = defect[random.randint(0,1)] 
        random_row, random_col   = random.randint(2, img.shape[0]-3), random.randint(2, img.shape[1]-3)
        left, right  = orig_val[random_row, random_col-2], orig_val[random_row, random_col+2]
        top, bottom  = orig_val[random_row-2, random_col], orig_val[random_row+2, random_col]
        neighbours   = [left, right, top, bottom]
        
        if not any(neighbours) and orig_val[random_row, random_col]==0: # if all neighbouring values in orig_val are 0 and the pixel itself is not defective
            orig_val[random_row, random_col]   = padded_img[random_row, random_col]
            padded_img[random_row, random_col] = defect_val
            total_defective_pixels-=1
    
    return padded_img, orig_val    
    