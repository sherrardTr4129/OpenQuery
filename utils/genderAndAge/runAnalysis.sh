br -algorithm AgeEstimation -enroll ~/Desktop/OpenQuery/genderAndAge/face.jpg  ~/Desktop/OpenQuery/genderAndAge/face.jpg age.csv

br -algorithm GenderEstimation -enroll ~/Desktop/OpenQuery/genderAndAge/face.jpg ~/Desktop/OpenQuery/genderAndAge/face.jpg gender.csv

python getCSVData.py
