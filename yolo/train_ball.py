import os
import zipfile
from ultralytics import YOLO

def unzip_dataset(zip_path: str, extract_to: str = "datasets/ball") -> str:
    """
    Unzip Roboflow export (YOLOv8) dan kembalikan path ke data.yaml.
    """
    os.makedirs(extract_to, exist_ok=True)
    print(f"[INFO] Extracting {zip_path} → {extract_to}/")
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(extract_to)
    # Roboflow biasanya meletakkan data.yaml di root extract
    data_yaml = os.path.join(extract_to, "data.yaml")
    if not os.path.isfile(data_yaml):
        raise FileNotFoundError(f"data.yaml not found in {extract_to}")
    print(f"[INFO] Found config: {data_yaml}")
    return data_yaml

def train_ball_detector(
    data_yaml: str,
    pretrained_weights: str = "yolov8n.pt",
    epochs: int = 50,
    batch_size: int = 16,
    img_size: int = 640,
    project_dir: str = "runs/ball",
    experiment_name: str = "exp1"
):
    """
    Train YOLOv8 on dataset ball.
    """
    print(f"[INFO] Loading model {pretrained_weights}")
    model = YOLO(pretrained_weights)

    print(f"[INFO] Starting training: epochs={epochs}, batch={batch_size}, imgsz={img_size}")
    model.train(
        data    = data_yaml,
        epochs  = epochs,
        batch   = batch_size,
        imgsz   = img_size,
        project = project_dir,
        name    = experiment_name,
        exist_ok=True   # overwrite jika sama nama
    )
    print(f"[INFO] Training finished. Best weights saved to {project_dir}/{experiment_name}/weights/best.pt")

if __name__ == "__main__":
    # 1) Path ke ZIP export dari Roboflow
    ZIP_PATH = "image ball.v5i.yolov8.zip"

    # 2) Unzip dan dapatkan data.yaml
    DATA_YAML = unzip_dataset(ZIP_PATH)

    # 3) Training
    train_ball_detector(
        data_yaml      = DATA_YAML,
        pretrained_weights = "yolov8n.pt",  # bisa dicek di ultralytics hub
        epochs          = 50,
        batch_size      = 16,
        img_size        = 640,
        project_dir     = "runs/ball",
        experiment_name = "orange_ball_v8n"
    )
