from ultralytics import YOLO

def main():
    model = YOLO("yolov8n-pose.pt")

    model.train(
        data="data.yaml",
        epochs=120,
        batch=16,
        device=0,
        name="final_clean_120"
    )

if __name__ == "__main__":
    main()