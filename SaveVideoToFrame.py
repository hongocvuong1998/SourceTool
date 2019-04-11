import cv2
import numpy as np

def SaveVideoToFrame(src,dst):
	video_capture = cv2.VideoCapture(src)
	k=1
	while True:
		savefile=dst+"\\"+str(k)+".jpg"
		ret, frame = video_capture.read()
		k+=1
		print(savefile)
		if((cv2.waitKey(1) & 0xFF == ord('q')) or ret ==False):
			break
		cv2.imwrite(savefile,frame)
		cv2.imshow("frame",frame)

	video_capture.release()
	cv2.destroyAllWindows()

SaveVideoToFrame("D:\\PROJECT\\Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning\\video\\test.mp4","D:\\PROJECT\\Two_Face_Comparer\\Image")