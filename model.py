from ultralytics import YOLO
import os
from PIL import Image

model = YOLO("yolov8n.yaml") 

path = os.path.join(os.getcwd(), "tuberculosis.v1i.yolov8", "data.yaml")

model.train(data=path, epochs=30)

metrics = model.val()

path = model.export(format="onnx") 