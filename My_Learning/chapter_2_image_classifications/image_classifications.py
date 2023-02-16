from ultralytics import YOLO
import cv2

path = r"C:\Users\Lukas\Desktop\My_Projects\Yolo_Projects\My_Learning"
image_path = r"C:\Users\Lukas\Desktop\My_Projects\Yolo_Projects\My_Learning\chapter_2_image_classifications\Images\3.png"

model = YOLO(path + "\yolo_model\yolov8l.pt")

results = model (image_path, show=True)
cv2.waitKey(0)
