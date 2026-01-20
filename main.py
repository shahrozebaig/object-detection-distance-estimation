import os
from src.inference import InferencePipeline

images_path = os.getenv("IMAGES_PATH", "data/images")
videos_path = os.getenv("VIDEOS_PATH", "data/videos")

image_output_dir = "outputs/images"
video_output_dir = "outputs/videos"

os.makedirs(image_output_dir, exist_ok=True)
os.makedirs(video_output_dir, exist_ok=True)

model_path = "models/yolov8n.pt"
pipeline = InferencePipeline(model_path, focal_length=800.0)

if os.path.exists(images_path):
    images = [f for f in os.listdir(images_path) if f.lower().endswith((".jpg", ".png"))]
    for img in images:
        input_path = os.path.join(images_path, img)
        output_path = os.path.join(image_output_dir, img)
        pipeline.run_on_image(input_path, output_path)

if os.path.exists(videos_path):
    videos = [f for f in os.listdir(videos_path) if f.lower().endswith((".mp4", ".avi", ".mov"))]
    for vid in videos:
        input_path = os.path.join(videos_path, vid)
        output_path = os.path.join(video_output_dir, vid)
        pipeline.run_on_video(input_path, output_path)
