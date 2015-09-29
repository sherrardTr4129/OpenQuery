
#include <iostream>
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/opencv.hpp>




using namespace cv;
using namespace std;




String face_cascade_name = "haarcascade_frontalface_alt.xml";
CascadeClassifier face_cascade;

Mat detectAndDisplay( Mat frame, CascadeClassifier face_cascade )
{
  std::vector<Rect> faces;
  Mat frame_gray;

  cvtColor( frame, frame_gray, CV_BGR2GRAY );
  equalizeHist( frame_gray, frame_gray );

  //-- Detect faces
  face_cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(20, 20) );

  for( int i = 0; i < faces.size(); i++ )
  {
    Point center( faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5 );
    //ellipse( frame, center, Size( faces[i].width*0.5, faces[i].height*0.5), 0, 0, 360, Scalar( 255, 0, 255 ), 4, 8, 0 );

    Mat faceROI = frame( faces[i] );
    std::ostringstream stringStream;
    stringStream << "face" << i << ".jpg";
    string file = stringStream.str();
    cout << "getting size and faces" << endl;
    if(!faceROI.empty())
    {
         if((faceROI.rows * faceROI.cols) > 20000)
         { 
               imwrite(file, faceROI);
         }
    }
  }
}

int main(int argc, char *argv[])
{
    Mat faces;
    face_cascade.load(face_cascade_name);
    faces = imread(argv[1]);
    detectAndDisplay(faces,face_cascade);
    return 0;    
}
