import cv2
import functions
import database

# Read the image
img = cv2.imread('taken.jfif')

# Segment the leaf
seg1 = functions.segmentation(img)
seg2 = functions.segmentation1(img)

# Compare both segmentation to get most appropriate one
segmented,final = functions.compareTwo(seg1,seg2)

# Apply contrasting
contrasted_img = functions.contrasting(segmented)

# RGB to HSI conversion
hsi= functions.RGB_TO_HSI(contrasted_img)

# Damaged part only
damaded_only = functions.damaged_only(contrasted_img)

hsi2=functions.RGB_TO_HSI(damaded_only)

# Finding damaged part into database
count = cv2.countNonZero(dmaged_only)
Intensity = np.mean(damaged_only)
print("Average Intensity   :",round(Intensity,3))
print("Damaged Area Approx :",round((count*100/final),2),"%","\n")
print(Intensity)
database.disease(Intensiy)


cv2.imshow('original',img)
cv2.imshow('segmented',segmented)
cv2.imshow('contrasted',contrasted_img)
cv2.imshow('HSI',hsi)
cv2.imshow('damaged only',damaded_only)
cv2.imshow('Damaged HSI', hsi2)
cv2.waitKey(0)
