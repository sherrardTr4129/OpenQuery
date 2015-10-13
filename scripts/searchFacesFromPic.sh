cd ..
./getFacesFromPic sample/face.jpg
for f in *.jpg
do
convert $f -resize "175x175!" $f
./fischerFaces labels.csv /. $f 1
done
