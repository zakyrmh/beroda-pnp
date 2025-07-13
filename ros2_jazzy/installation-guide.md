# 🤖 Instalasi ROS 2 Jazzy Jalisco di Ubuntu

## 📌 Deskripsi

[ROS 2 Jazzy Jalisco](https://docs.ros.org/en/jazzy/index.html) adalah versi terbaru dari Robot Operating System 2 (ROS 2) yang dirilis pada tahun 2024. Versi ini mendukung Ubuntu 24.04 (Noble Numbat) dan membawa peningkatan performa, kompatibilitas, dan stabilitas.

---

## 🧰 Prasyarat

- Ubuntu 24.04.2 LTS (64-bit)
- Akses sudo (root)
- Koneksi internet stabil

---

## 🔧 Proses Instalasi

### 1. Set Locale
- Locale adalah kombinasi pengaturan bahasa, format tanggal/waktu, mata uang, dan encoding karakter.
- UTF‑8 adalah standar encoding yang mendukung karakter dari hampir semua bahasa dunia. ROS 2 membutuhkan ini agar bisa memproses teks (seperti nama topik, pesan, file log) dengan benar.
    ```bash
    locale  # periksa UTF-8

    sudo apt update && sudo apt install locales  # mengaktifkan paket untuk konfigurasi locale
    sudo locale-gen en_US en_US.UTF-8  # menghasilkan file dan data untuk locale en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  # menetapkan LC_ALL dan LANG ke en_US.UTF-8, agar digunakan sistem-wide
    export LANG=en_US.UTF-8  # memastikan terminal saat ini langsung pakai setting baru

    locale  # verifikasi hasil
    ```

### 2. Enable required repositories

#### a. Mengaktifkan Ubuntu Universe repository
- Universe adalah repositori resmi Ubuntu yang dikelola oleh komunitas dan berisi banyak paket sumber terbuka (open-source).
- ROS 2 membutuhkan beberapa dependensi yang hanya tersedia di Universe.
- Jika Universe tidak diaktifkan, maka apt tidak akan menemukan paket-paket tersebut, dan instalasi ROS bisa gagal karena "package not found"
    ```bash
    sudo apt install software-properties-common
    sudo add-apt-repository universe
    ```

#### b. Menambahkan repositori ROS 2 dan kunci GPG
- File .deb ini berasal dari paket ros-apt-source yang disediakan oleh tim ROS.
- Saat diinstall, ia akan secara otomatis:
  - Menambahkan sumber paket (source list) dari server ROS,
  - dan memasang kunci GPG (authentication key) untuk validasi keamanan paket.
- Setiap kali ada update baru dari ROS, repositori ini akan secara otomatis terupdate, tanpa kamu harus mengubah konfigurasi manual 
    ```bash
    sudo apt update && sudo apt install curl -y
    export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
    curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"
    sudo dpkg -i /tmp/ros2-apt-source.deb
    ```

#### c. Install development tools (optional)
- Berguna jika ingin mengembangkan atau membangun paket ROS sendiri.
    ```bash
    sudo apt update && sudo apt install ros-dev-tools
    ```

#### d. Install ROS 2
- Perbarui cache repositori apt setelah menyiapkan repositori.

    ```bash
    sudo apt update
    ```

- Instalasi Desktop (Disarankan): ROS, RViz, demo, tutorial.
    ```bash
    sudo apt install ros-jazzy-desktop
    ```

#### e. Setup environment
- Menyiapkan lingkungan (environment) agar terminal bisa mengenali dan menjalankan semua perintah, paket, pustaka, dan variabel dari instalasi ROS 2 Jazzy Jalisco.
    ```bash
    source /opt/ros/jazzy/setup.bash
    ```
- Agar otomatis setiap buka terminal, tambahkan baris ini ke file ~/.bashrc:
    ```bash
    echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
    ```

#### f. Try some examples
- Pada satu terminal, cari berkas pengaturan dan kemudian jalankan C++ talker:
    ```bash
    ros2 run demo_nodes_cpp talker
    ```
- Di sumber terminal lain, file pengaturan lalu jalankan Python listener:
    ```bash
    ros2 run demo_nodes_py listener
    ```

## REFERENSI
[ Intallation Ubuntu (deb packages) - ROS 2 Documentation: Jazzy ](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)
