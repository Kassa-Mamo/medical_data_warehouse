import os
import torch
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

# Load the pre-trained YOLOv5 model from ultralytics (ensure you have internet access)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Define input and output directories
BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, '../images')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def detect_objects_in_image(image_path):
    try:
        logger.info(f"Processing image: {image_path}")
        results = model(image_path)
        # Extract detection details (bounding boxes, confidence, class labels)
        detections = results.pandas().xyxy[0].to_dict(orient="records")
        # Save the annotated image in the OUTPUT_DIR
        results.save(save_dir=OUTPUT_DIR)
        logger.info(f"Detections for {image_path}: {detections}")
        # Optionally, write detection details to a database or file here.
        return detections
    except Exception as e:
        logger.error(f"Error processing {image_path}: {e}")
        return []

def main():
    # Process all images in IMAGE_DIR
    for file in os.listdir(IMAGE_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(IMAGE_DIR, file)
            detect_objects_in_image(image_path)

if __name__ == "__main__":
    main()
