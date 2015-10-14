# OpenQuery
a face recognition query system for the Computer Science House at RIT 

##Installing 
```bash
cd /install
./Pico2WavInstallonRPi.sh
./InstallOpenCV.sh 
```

##Building 
```bash
cd /src
mkdir build
cd build 
cmake ..
make 
mv getFacesFromPic ..
mv getFaces ..
mv fischerFaces ..
```

##Running
```bash
cd scripts
./searchFaces.sh

or

./searchFacesFromPic
```
