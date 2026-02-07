from jadwal import Jadwal
from agent import AIAgent

jadwal = Jadwal()
agent = AIAgent(jadwal)

agent.proses_input("Kuliah PBO", "08:00")
agent.proses_input("Rapat Proyek AI", "10:00")

jadwal.tampilkan_jadwal()
