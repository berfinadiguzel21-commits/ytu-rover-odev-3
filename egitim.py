
from ultralytics import YOLO

if __name__ == '__main__':
    # 1. Modeli Yukle
    model = YOLO("yolov8n.pt")
    
    # 2. Egitimi Baslat
    results = model.train(data="data.yaml", epochs=50, imgsz=416, batch=16)