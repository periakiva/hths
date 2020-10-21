# HTHS Internship

Hi! Here we will assemble some resources and information that will be useful to you. 

### General notes
* Tutorials will be in the form of jupyer notebooks or google collabs. A jupyter notebook is an interactive file with the extension ```.ipynb```, which allows you to execute lines or blocks of code indepndetly of other blocks. A jupyer notebook file can be loaded into Google Collab by clicking on 
``` File > Upload Notebook > Choose File ```
* Contacts:
``` 
    Peri: peri.akiva@rutgers.edu
    Faith: faith.johnson@rutgers.edu
```

#### Python background and tutorial

- [CS231n Python Tutorlal](https://colab.research.google.com/github/cs231n/cs231n.github.io/blob/master/python-colab.ipynb#scrollTo=Nji1_UjYL9fY)


#### OpenCV Tutorial

Note that this is a "top-down" learning of the machine learning and OpenCV. It starts by learning the process of how to work through a machine learning pipeline in an end-to-end fashion without going through the heavy mathemtical prerequisites. Generally, the "bottom-up" approach requires covering the math and theory behind those tools which are harder and not necessary for the purpose of this internship. 

You can choose which sections are most relevant to you.

##### Setting up the environment for any notebook in the OpenCV tutorial
- Download this repository to your machine
- Unzip the folder
- Go to [Google Colab](colab.research.google.com) and click on ``` File > Upload Notebook > Choose File ``` and select the tutorial you choose to use. 
- Click on the files icon on the left
- Right click on the white space, then click on "New Folder", and name it "images"
- Right click on the images folder and select "Upload"
- Go to the unzipped repository and select all the images in the images directory.
- Repeat this process with the "detect" and "videos" folders.
- There is an option to add the data to your google drive and synch it with colab, which would make it easier in future work. 

##### OpenCV Version Compatability
- Make sure the OpenCV version is 3.4.2.16
- OpenCV version can be checked inside the python screen by running this command:
``` import cv2
    print(cv2.__version__)
```
- Otherwise, include those two lines in the top of the file (before the import statements):
```
!pip install opencv-python==3.4.2.16
!pip install opencv-contrib-python==3.4.2.16
```
- Make sure to re-run blocks if you encoutered an error and then re-installed OpenCV

###### Section 1: general tools
- Loading and showing images
- Drawing shapes on images
- Adding text to iamges
- Modifying images

###### Section 2: Edge detection
- Sobel operator for edge detection
- Canny edge detection

###### Section 3: Keypoint and Feature Extraction
- Scale Invariant Feature Transform (SIFT) feature extraction
- Keypoint detection using SIFT
- keypoint and feature matching

###### Section 4: Homography and Geometric Transformations
- Image translation, rotation
- Affine transformation
- Homography
- Homography from SIFT matching

###### Section 5: Face Detection
- Face Cascade

###### Section 6: Classification
- SVM
- Bag of Words

###### Section 7: Tracking
- Object tracking in videos

### Useful datasets:
- https://www.kaggle.com/datasets
- https://archive.ics.uci.edu/ml/index.php
- https://datasetsearch.research.google.com
- https://github.com/awesomedata/awesome-public-datasets
- https://www.visualdata.io/discovery