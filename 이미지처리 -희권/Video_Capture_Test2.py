import cv2
 
vidcap = cv2.VideoCapture("Video/Test.mp4")   # 0: default camera
#cap = cv2.VideoCapture("test.mp4") #동영상 파일에서 읽기
count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
 
    if(int(vidcap.get(1)) % 30 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("Capture/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1
 
vidcap.release()
