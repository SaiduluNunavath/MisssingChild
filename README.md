In India a countless number of children are reported missing every year. Among the 
missing child cases a large percentage of children remain untraced. It is estimated that a 
child goes missing in India every eight minutes. This project presents a novel use of deep 
learning methodology for identifying the reported missing child from the photos of 
multitude of children available, with the help of face recognition. The public can upload 
photographs of suspicious child into a common portal with landmarks and remarks.
 The MISSING CHILD IDENTIFICATION system utilizes a Support Vector 
Machine (SVM) classifier to match uploaded images with registered photos of missing 
children from a repository. To begin, images from the repository are preprocessed, 
converted to grayscale, and resized to a fixed dimension of 64x64 pixels. These processed 
images are then flattened into 1D arrays for efficient processing. Next, the system loads 
images and their corresponding labels from various folders, each representing a different 
missing child, organizing them based on the children's names. Once loaded, the images 
and labels are transformed into numpy arrays in preparation for training. The dataset is 
then split into training and testing sets to assess the model's performance. Subsequently, a 
SVM classifier with a linear kernel is trained using the training data, allowing it to learn to 
classify input images into the corresponding classes based on the extracted features. 
Following training, the SVM model predicts the classes of the images in the testing set. 
Finally, the accuracy of the trained SVM model is calculated by comparing the predicted 
classes with the actual classes of the testing images. This system streamlines the process 
of comparing uploaded images with the repository of missing children, aiding in the 
identification and potential recovery of missing individuals
