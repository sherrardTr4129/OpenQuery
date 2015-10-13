cd ..
./getFaces
convert face.jpg -resize "175x175!" face.jpg
./fischerFaces labels.csv /. face.jpg 1
