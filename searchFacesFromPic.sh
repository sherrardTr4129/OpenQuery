./getFacesFromPic /img/sample/face.jpg
br -algorithm FaceRecognition -enroll /home/sherrardtr/Desktop/OpenQuery/img test.gal
br -algorithm FaceRecognition -compare  /home/sherrardtr/Desktop/OpenQuery/face.jpg test.gal match_scores.csv
python getCSVData.py
rm hello.mp3
