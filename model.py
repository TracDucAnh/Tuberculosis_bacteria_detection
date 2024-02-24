from ultralytics import YOLO
import os
from PIL import Image
model = YOLO("yolov8n.yaml") 
path = os.path.join(os.getcwd(), "tuberculosis.v1i.yolov8", "data.yaml")
model.train(data=path, epochs=20)

metrics = model.val() 

img = os.path.join(os.getcwd(), "sample", "tuberculosis-phone-1253.jpg")

img = Image.open(img)

results = model.predict(source=img, save=True) 

path = model.export(format="onnx") 