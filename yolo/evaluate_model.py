# evaluate_model.py

import numpy as np
import pandas as pd
from ultralytics import YOLO

def evaluate_model(model_path: str, data_yaml: str, batch: int = 16, imgsz: int = 640, device: str = 'cpu'):
    # Load model
    model = YOLO(model_path)

    # Jalankan validasi dengan plots
    results = model.val(
        data=data_yaml,
        batch=batch,
        imgsz=imgsz,
        device=device,
        plots=True,
        save_json=False
    )

    # Cetak metrik utama
    # metrics = results.metrics
    metrics = results.results_dict
    print("--- Metrik Validasi ---")
    print(f"Precision (mAP@0.5): {metrics['metrics/precision(B)']:.3f}")
    print(f"Recall:              {metrics['metrics/recall(B)']:.3f}")
    print(f"mAP@0.5:             {metrics['metrics/mAP50(B)']:.3f}")
    print(f"mAP@0.5–0.95:        {metrics['metrics/mAP50-95(B)']:.3f}")
    print()

    # Confusion Matrix text dan simpan CSV
    cm = results.confusion_matrix
    names = cm.names
    mat = cm.matrix
    df_cm = pd.DataFrame(mat, index=names+["background"], columns=names+["background"])
    df_cm.to_csv("confusion_matrix.csv")
    print("✅ Confusion matrix saved: confusion_matrix.csv")
    cm.print()
    print(cm.summary(normalize=True))

    print("\n✅ Evaluasi selesai. Visual outputs tersimpan di:")
    print("runs/.../val/")

if __name__ == "__main__":
    evaluate_model(
        model_path = "runs/ball/orange_ball_v8n/weights/best.pt",
        data_yaml  = "datasets/ball/data.yaml",
        batch      = 16,
        imgsz      = 640,
        device     = "cpu"
    )
