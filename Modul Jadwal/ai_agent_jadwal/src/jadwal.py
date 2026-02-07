class Jadwal:
    def __init__(self):
        self.daftar_kegiatan = []

    def tambah_kegiatan(self, nama, waktu):
        kegiatan = {
            "nama": nama,
            "waktu": waktu
        }
        self.daftar_kegiatan.append(kegiatan)

    def tampilkan_jadwal(self):
        print("=== Jadwal Kegiatan ===")
        for k in self.daftar_kegiatan:
            print(f"- {k['nama']} pada {k['waktu']}")
