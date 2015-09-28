./getFaces

br -algorithm AgeEstimation -enroll ~/Desktop/OpenQuery/face.jpg  ~/Desktop/OpenQuery/face.jpg age.csv

br -algorithm GenderEstimation -enroll ~/Desktop/OpenQuery/face.jpg ~/Desktop/OpenQuery/face.jpg gender.csv

python getCSVData.py
