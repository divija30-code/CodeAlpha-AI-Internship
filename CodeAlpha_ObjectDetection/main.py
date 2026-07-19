import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    # Draw bounding boxes, labels, and tracking IDs
    annotated_frame = results[0].plot()

    cv2.imshow("Real-Time Object Detection & Tracking", annotated_frame)

    # Press ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
