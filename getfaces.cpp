
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
  face_cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30) );

  for( int i = 0; i < faces.size(); i++ )
  {
    Point center( faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5 );
    //ellipse( frame, center, Size( faces[i].width*0.5, faces[i].height*0.5), 0, 0, 360, Scalar( 255, 0, 255 ), 4, 8, 0 );

    Mat faceROI = frame( faces[i] );
    return faceROI;

  }

 }

int main()
{
    Mat faces;
    face_cascade.load(face_cascade_name);
    VideoCapture cap(0);

    while(true)
    {
        cap.read(faces);
        Mat faceROI = detectAndDisplay(faces,face_cascade);
        imshow("faces", faces);
        cout << "getting size and faces" << endl;

        if(!faceROI.empty())
        {
             if((faceROI.rows * faceROI.cols) > 35000)
             { 
                  imwrite("face.jpg", faceROI);
                      break;
             }
             if(waitKey(1) == 'q')
                 break;
        }
    }
    return 0;    
}
