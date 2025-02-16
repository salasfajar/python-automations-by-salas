"""
AUTOMATED FILE BACKUP SCRIPT
Author: Salas Fajar Maulana
---
Program ini secara otomatis akan mencadangkan
folder yang ditentukan ke lokasi folder backup tujuan
dalam rentang/interval waktu tertentu.

Selain itu, program ini juga secara otomatis
menghapus backup lama yang telah melewati batas waktu
yang telah ditentukan.

Pastikan untuk menyesuaikan konfigurasi terlebih dahulu.
Konfigurasi dapat diatur melalui file config.json
"""

import os
import shutil
import time
import logging
import json
from datetime import datetime, timedelta
import schedule


#Load config file
with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

SOURCE_FOLDER = config["source_folder"]
BACKUP_FOLDER = config["backup_folder"]
BACKUP_INTERVAL = config["backup_interval"]
DELETE_OLD_BACKUPS_DAYS = config["delete_old_backups_days"]

#Setup logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(filename=os.path.join(LOG_DIR, "backup.log"),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

#Backup func
def backup_files():
    """
    Mencadangkan file 
    dari SOURCE_FOLDER ke dalam BACKUP_FOLDER
    dangan nama unik berdasarkan timestamp

    Semua proses fungsi ini akan tercatat dalam log
    """
    timestamp = datetime.now().strftime("%Y%M%D_%H%M%S")
    backup_path = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")

    try:
        if not os.path.exists(SOURCE_FOLDER):
            raise FileNotFoundError(f"Folder sumber tidak ditemukan: {SOURCE_FOLDER}")
        shutil.copytree(SOURCE_FOLDER, backup_path)
        logging.info("Backup berhasil: %s", backup_path)
        print("Backup berhasil!: %s", backup_path)
    except FileNotFoundError as e:
        logging.error("File/folder tidak ditemukan: %s", e)
        print("ERROR: File/folder tidak ditemukan %s", e)
    except PermissionError as e:
        logging.error("Permission Error: %s", e)
        print("ERROR: Tidak memiliki izin untuk mengakses file/folder %s", e)
    except OSError as e:
        logging.error("Kesalahan Sistem: %s", e)
        print("ERROR: Terjadi kesalahan pada sistem %s", e)
    except Exception as e:
        logging.error("Kesalahan tidak terduga: %s", e)
        print("ERROR: Kesalahan tidak terduga %s", e)

#Delete backup func
def delete_old_backups():
    """
    Menghapus backup file yang
    sudah melewati batas DELETE_OLD_BACKUPS_DAYS.

    Semua proses fungsi ini akan tercatat dalam log
    """
    try:
        now = datetime.now()
        for folder in os.listdir(BACKUP_FOLDER):
            folder_path = os.path.join(BACKUP_FOLDER, folder)
            if os.path.isdir(folder_path):
                folder_time = datetime.strftime(folder.split("_")[-1], "%Y%M%D_%H%M%S")
                if now - folder_time > timedelta(days=DELETE_OLD_BACKUPS_DAYS):
                    shutil.rmtree(folder_path)
                    logging.info("Backup lama telah dihapus: %s", folder_path)
                    print("Backup lama telah dihapus: %s", folder_path)
    except FileNotFoundError as e:
        logging.error("File/folder backup tidak ditemukan: %s", e)
        print("ERROR: File/folder backup tidak ditemukan %s", e)
    except PermissionError as e:
        logging.error("Permission Error: %s", e)
        print("ERROR: Tidak memiliki izin untuk menghapus file/folder %s", e)
    except OSError as e:
        logging.error("Kesalahan Sistem: %s", e)
        print("ERROR: Terjadi kesalahan pada sistem %s", e)
    except Exception as e:
        logging.error("Gagal menghapus backup: %s", e)
        print("Gagal menghapus backup: %s", e)

#Schedule automated backup
schedule.every(BACKUP_INTERVAL).minutes.do(backup_files)
schedule.every().day.at("00:00").do(delete_old_backups)

print(f"Backup otomatis dimulai setiap {BACKUP_INTERVAL} menit. Tekan Ctrl + C untuk berhenti.")
while True:
    schedule.run_pending()
    time.sleep(1)

# End-of-file (EOF)
