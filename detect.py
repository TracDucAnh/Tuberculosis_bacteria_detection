from ultralytics import YOLO
import os
from PIL import Image

path = os.path.join(os.getcwd(), "runs", "detect", "train", "weights", "best.pt")

model = YOLO(path)

sample = os.path.join(os.getcwd(), "sample")

for img in os.listdir(sample):
    if img[-4:] == ".jpg":
        img = os.path.join(sample, img)
        model.predict(source=img, save = True)