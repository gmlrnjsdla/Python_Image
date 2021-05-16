import cv2
 
cap = cv2.VideoCapture(0)   # 0: default camera
#cap = cv2.VideoCapture("test.mp4") #동영상 파일에서 읽기

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size: {0} x {1}".format(width, height))
 
# 영상 저장을 위한 VideoWriter 인스턴스 생성
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))
  
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        writer.write(frame) #프레임 저장
        # 프레임 출력
        cv2.imshow('Camera Window', frame)
 
        # ESC를 누르면 종료
        key = cv2.waitKey(1) & 0xFF
        if (key == 27): 
            break
 
cap.release()
writer.release()
cv2.destroyAllWindows()
