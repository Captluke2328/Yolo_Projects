from ultralytics import YOLO
import cv2

path = r"C:\Users\Lukas\Desktop\My_Projects\Yolo_Projects\My_Learning"
model = YOLO(path + "\yolo_model\yolov8l.pt")
cv2.waitKey(0)

