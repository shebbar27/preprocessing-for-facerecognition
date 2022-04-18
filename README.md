# preprocessing-for-facerecognition

## Description

This python script uses OpenCV based library haarcascades to detect a human face in the images stored in /input-images folder and then crops the images so that the human face fits prefectly in the image.
The cropped image is resized to original dimensions and stored in /output-images folder.
If no human face is detected then the image is skipped and won't be processed.

## Limitations

- can detect only human faces with front view orientation
- if multiple human faces are present in the image, this script selects only one face. But it can easily modifed to get all the faces.
