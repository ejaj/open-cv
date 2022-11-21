import cv2

video_capture = cv2.VideoCapture('videos/input.avi')
fps = video_capture.get(cv2.CAP_PROP_FPS)
size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('videos/output.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
convert, frame = video_capture.read()
while convert:
    videoWriter.write(frame)
    success, frame = video_capture.read()
