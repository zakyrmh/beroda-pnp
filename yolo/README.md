# RINGKASAN RISET TRACKING BOLADENGAN MODEL YOLO

Riset ini bertujuan untuk mempelajari penggunaan model YOLO untuk mendeteksi dan melacak bola berwarna oranye secara real-time menggunakan model YOLOv8 yang dilatih khusus. Riset ini mencakup seluruh pipeline mulai dari persiapan data, pelatihan, evaluasi, hingga deployment dan tracking via webcam atau kamera USB eksternal.

## 🔧 PERSIAPAN

### 1. Lingkungan Kerja
- Sistem Operasi : Windows 10/11, macOS Ventura, atau distribusi Linux (Ubuntu 20.04+).
- Python : Version 3.8+

### 2. Tools
- Visual Studio Code
- Roboflow

## 📥 LANGKAH KERJA

### 🧪 1. Persiapan Dataset
- Kumpulkan gambar bola oranye dalam berbagai kondisi.
- Anotasi bounding box menggunakan LabelImg atau Roboflow (format YOLO).

### 🪓 2. Membagi Dataset (Opsional)
- Jika hanya terdapat data train, maka sebelum melakukan pelatihan model perlu dipersiapkan data valid
- Jalankan file `split.py`

### 🚀 3. Melatih Model
- Jalankan file `train_ball.py`
- Proses ini memakan banyak waktu tergantung device.
- Output: runs/ball/orange_ball_v8n/weights/best.pt

### 🧪 4. Evaluasi Kinerja Model
- Jalankan file `evaluate_model.py`
- Menghasilkan metrik precision, recall, mAP, confusion matrix, dan grafik PR/F1.
- File hasil di runs/ball/orange_ball_v8n/val/ dan confusion_matrix.csv.

### 🎯 5. Inference Data Baru
- Jalankan file `inference.py`
- Deteksi di datasets/valid/images/.
- Output gambar ber-BBox, crop, dan label .txt di runs/ball/inference/.

### 🎥 6. Tracking Objek
- Hubungkan PC dengan kamera
- Jalankan file `tracking.py`