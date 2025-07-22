# inference.py

from ultralytics import YOLO

def run_inference(
    model_path: str = "runs/ball/orange_ball_v8n/weights/best.pt",
    source: str = "datasets/ball/valid/images",  # bisa file, folder, atau video
    imgsz: int = 640,
    conf: float = 0.25,
    device: str = "cpu",  # atau "cuda:0"
    project: str = "runs/ball",
    name: str = "inference",
    save: bool = True,
    save_crop: bool = True,
    save_txt: bool = False,
    save_conf: bool = False
):
    """
    Lakukan inference menggunakan model YOLO dan simpan output analisis.
    """
    model = YOLO(model_path)
    results = model.predict(
        source=source,
        imgsz=imgsz,
        conf=conf,
        device=device,
        save=save,
        save_crop=save_crop,
        save_txt=save_txt,
        save_conf=save_conf,
        project=project,
        name=name,
        exist_ok=True
    )
    print(f"✅ Inference selesai! Output disimpan di: {project}/{name}")
    return results

def print_results(results):
    for res in results:
        for box in res.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            name = res.names[cls]
            print(f"- {name}: conf={conf:.2f}, bbox=[{x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f}]")

if __name__ == "__main__":
    res = run_inference(
        model_path="runs/ball/orange_ball_v8n/weights/best.pt",
        source="datasets/ball/valid/images",
        imgsz=640,
        conf=0.3,
        device="cpu"
    )
    print("\n📄 Hasil deteksi:")
    print_results(res)
