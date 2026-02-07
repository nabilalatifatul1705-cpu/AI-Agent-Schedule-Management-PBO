class AIAgent:
    def __init__(self, jadwal):
        self.jadwal = jadwal

    def proses_input(self, nama, waktu):
        print("AI Agent sedang memproses input...")
        self.jadwal.tambah_kegiatan(nama, waktu)
