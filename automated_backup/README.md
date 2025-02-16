# Automated File Backup

Automated File Backup adalah skrip Python yang secara otomatis mencadangkan folder tertentu ke lokasi backup berdasarkan jadwal yang ditentukan. Skrip ini juga dapat menghapus backup lama untuk menghemat ruang penyimpanan.

## ✨ Fitur
- 📂 **Backup Otomatis**: Mencadangkan folder sumber ke folder backup secara berkala.
- 🗑 **Hapus Backup Lama**: Menghapus backup yang sudah melewati batas waktu yang ditentukan.
- 📝 **Logging**: Mencatat semua aktivitas backup dan penghapusan ke dalam file log.
- ⚙ **Konfigurasi Fleksibel**: Pengaturan dapat diubah melalui file `config.json`.

## 🛠 Persyaratan
- Python 3.x
- Modul Python:
  - `os`
  - `shutil`
  - `schedule`
  - `logging`
  - `json`
  - `time`
  - `datetime`

Jika modul `schedule` belum terinstal, kamu bisa menginstalnya dengan:
```sh
pip install schedule

🚀 Cara Menggunakan

1. Clone repository:

git clone https://github.com/salasfajar/python-automations-by-salas.git
cd python-automations-by-salas
cd automated_backup


2. Buat dan sesuaikan konfigurasi di config.json:

{
    "source_folder": "C:/Users/Username/Documents/ImportantFiles",
    "backup_folder": "D:/Backup",
    "backup_interval": 30,
    "delete_old_backups_days": 7
}

source_folder: Folder yang akan dicadangkan.

backup_folder: Lokasi tempat backup disimpan.

backup_interval: Interval backup dalam menit.

delete_old_backups_days: Hapus backup lebih lama dari jumlah hari ini.



3. Jalankan script backup.py:

python backup.py

Backup akan berjalan otomatis berdasarkan interval yang telah diatur.

Log aktivitas tersimpan di folder logs/backup.log.




🔍 Contoh Output

🔄 Backup otomatis dimulai setiap 30 menit. Tekan Ctrl+C untuk berhenti.
✅ Backup berhasil: D:/Backup/backup_20250215_153000
🗑 Backup lama dihapus: D:/Backup/backup_20250201_100000

🛡️ Error Handling

Jika terjadi error, script akan menampilkan pesan error dan mencatatnya di log:

FileNotFoundError: Jika folder sumber atau backup tidak ditemukan.

PermissionError: Jika tidak memiliki izin untuk mengakses/menghapus file.

OSError: Jika terjadi kesalahan sistem.


📜 Lisensi

Proyek ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan.

