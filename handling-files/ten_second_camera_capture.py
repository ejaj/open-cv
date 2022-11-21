import cv2

camera_capture = cv2.VideoCapture(0)
fps = 30  # An assumption
size = (int(camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video_writer = cv2.VideoWriter('videos/my_output_vid.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)

success, frame = camera_capture.read()

number_frames_remaining = 10 * fps - 1  # 10 seconds of frames

while number_frames_remaining > 0:
    if frame is not None:
        video_writer.write(frame)
    success, frame = camera_capture.read()
    number_frames_remaining -= 1
