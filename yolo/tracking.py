# tracking_webcam_usb_menu_filtered.py

import cv2
from ultralytics import YOLO
from cv2_enumerate_cameras import enumerate_cameras

def select_camera():
    cams = list(enumerate_cameras())
    if not cams:
        print("❌ Tidak ada kamera yang terdeteksi!")
        exit(1)

    print("📷 Pilih kamera yang ingin digunakan:")
    for cam in cams:
        print(f"  {cam.index}: {cam.name}")
    idx = None
    while idx is None:
        try:
            sel = int(input(f"Pilih index (0–{cams[-1].index}): "))
            if any(cam.index == sel for cam in cams):
                idx = sel
            else:
                print("🚫 Index tidak tersedia, coba lagi.")
        except:
            print("🚫 Input harus berupa angka.")
    return idx

def track_from_camera(source, model_path, tracker, imgsz, conf, device):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("❌ Tidak bisa membuka kamera.")
        exit()

    print("✅ Kamera berhasil dibuka. Tekan 'q' untuk keluar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Gagal membaca frame dari kamera.")
            break

        results = model.track(frame, conf=conf, imgsz=imgsz, tracker=tracker, device=device, persist=True, verbose=False)

        if results:
            boxes = results[0].boxes
            if boxes is not None and len(boxes) > 0:
                # Filter dengan confidence > 0.7
                boxes_filtered = [box for box in boxes if float(box.conf[0]) > 0.6]
                if boxes_filtered:
                    # Pilih yang paling tinggi confidence-nya
                    best_box = max(boxes_filtered, key=lambda b: float(b.conf[0]))
                    x1, y1, x2, y2 = map(int, best_box.xyxy[0])
                    conf_val = float(best_box.conf[0])
                    cls = int(best_box.cls[0])
                    class_name = results[0].names[cls]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{class_name} {conf_val:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Tracking Bola", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 Dihentikan oleh pengguna.")
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    cam_idx = select_camera()
    print(f"🔄 Mulai tracking dari kamera index {cam_idx}.")

    track_from_camera(
        source=cam_idx,
        model_path="runs/ball/orange_ball_v8n/weights/best.pt",
        tracker="botsort.yaml",
        imgsz=640,
        conf=0.3,
        device="cpu"
    )

if __name__ == "__main__":
    main()
