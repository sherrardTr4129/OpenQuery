./getFaces
br -algorithm FaceRecognition -enroll /home/sherrardtr/Desktop/OpenQuery/img test.gal
br -algorithm FaceRecognition -compare  /home/sherrardtr/Desktop/OpenQuery/face.jpg test.gal match_scores.csv
python getCSVData.py
sshpass -p "12-34-98" scp msg.wav pi@faceharold.csh.rit.edu:~/
sshpass -p "12-34-98" ssh pi@faceharold.csh.rit.edu aplay msg.wav

