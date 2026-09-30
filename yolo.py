from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="roboflow_dataset/data.yaml",
    epochs=50,
    batch=16,
    imgsz=640,
    optimizer="auto"
)

model.predict(
    source="stop_sign_data_set",
    conf=0.50,
    save=True
)