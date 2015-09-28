./getFaces
br -algorithm FaceRecognition -enroll /home/sherrardtr/Desktop/OpenQuery/img test.gal
br -algorithm FaceRecognition -compare ~/Desktop/OpenQuery/face.jpg test.gal match_scores.csv
python getCSVData.py
mpg123 hello.mp3
rm face.jpg
rm hello.mp3
