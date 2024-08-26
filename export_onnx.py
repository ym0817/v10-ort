# from ultralytics import YOLO
from ultralytics import YOLOv10

# Load a model
model = YOLOv10('yolov10n.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom trained model

# Export the model
# model.export(format='onnx'
model.export(format='onnx',opset=13)