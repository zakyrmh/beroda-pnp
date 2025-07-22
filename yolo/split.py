import os, random, shutil

# Ubah path berikut sesuai struktur-mu
SRC_IMG = 'datasets/ball/train/images'
SRC_LBL = 'datasets/ball/train/labels'

DST_TRAIN_IMG = 'datasets/ball/train/images'
DST_TRAIN_LBL = 'datasets/ball/train/labels'
DST_VAL_IMG   = 'datasets/ball/valid/images'
DST_VAL_LBL   = 'datasets/ball/valid/labels'

# Buat folder tujuan jika belum ada
for folder in [DST_TRAIN_IMG, DST_TRAIN_LBL, DST_VAL_IMG, DST_VAL_LBL]:
    os.makedirs(folder, exist_ok=True)

# Ambil list semua file gambar di SRC_IMG
files = [f for f in os.listdir(SRC_IMG) if f.lower().endswith(('.jpg', '.png'))]
random.shuffle(files)

# Split 80% train, 20% valid
split_idx   = int(0.8 * len(files))
train_files = files[:split_idx]
val_files   = files[split_idx:]

# Fungsi bantu untuk memindahkan
def move_files(filenames, src_img, src_lbl, dst_img, dst_lbl):
    for fname in filenames:
        lbl_name = os.path.splitext(fname)[0] + '.txt'
        # pastikan file label ada
        if not os.path.isfile(os.path.join(src_lbl, lbl_name)):
            print(f"[WARNING] label missing for {fname}, skipping")
            continue
        shutil.move(os.path.join(src_img, fname), os.path.join(dst_img, fname))
        shutil.move(os.path.join(src_lbl, lbl_name), os.path.join(dst_lbl, lbl_name))

# Lakukan pemindahan
move_files(train_files, SRC_IMG, SRC_LBL, DST_TRAIN_IMG, DST_TRAIN_LBL)
move_files(val_files,   SRC_IMG, SRC_LBL, DST_VAL_IMG,   DST_VAL_LBL)

print(f"Done! {len(train_files)} images → train, {len(val_files)} images → valid")
