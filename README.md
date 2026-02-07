# 🤖 AI Agent Schedule Management System (PBO Implementation)

Proyek ini adalah implementasi sistem manajemen jadwal sederhana yang menggunakan konsep **AI Agent** sebagai pengelola input. Dibangun menggunakan bahasa pemrograman Python, proyek ini memfokuskan pada penerapan prinsip **Object-Oriented Programming (OOP)** seperti Enkapsulasi, Agregasi, dan Dekomposisi.

## 📊 Rancangan Sistem (UML)
Sistem ini terdiri dari dua kelas utama yang saling berinteraksi:
- **AIAgent:** Bertindak sebagai pengolah instruksi (Controller).
- **Jadwal:** Bertindak sebagai penyimpan data kegiatan (Model).

> **Relasi:** `AIAgent` memiliki ketergantungan (Aggregation) terhadap kelas `Jadwal`.

## 🛠️ Fitur Utama
- **Encapsulation:** Penggunaan atribut privat (`__`) untuk melindungi data jadwal dari akses langsung.
- **Dynamic Logging:** AI Agent memberikan feedback visual saat memproses setiap input.
- **Data Persistence (List):** Menyimpan dan menampilkan daftar kegiatan secara terorganisir.

## 📁 Struktur File
- `jadwal.py`: Berisi kelas `Jadwal` yang mengelola list kegiatan.
- `agent.py`: Berisi kelas `AIAgent` yang mengelola logika pemrosesan input.
- `main.py`: Entry point aplikasi untuk menjalankan simulasi.

