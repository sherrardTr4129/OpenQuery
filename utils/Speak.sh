read -p "Enter your phrase : " name
pico2wave -w msg.wav "$name"
sshpass -p "faceharold" scp msg.wav pi@faceharold.csh.rit.edu:~/
sshpass -p "faceharold" ssh pi@faceharold.csh.rit.edu aplay msg.wav
