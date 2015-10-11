./home/sherrardtr/Desktop/OpenQuery/img/tempFaces/getFacesFromPic /img/sample/face.jpg
for f in *.jpg
do
br -algorithm FaceRecognition -enroll /home/sherrardtr/Desktop/OpenQuery/img test.gal
br -algorithm FaceRecognition -compare  /home/sherrardtr/Desktop/OpenQuery/$f test.gal match_scores.csv
python getCSVData.py
done
