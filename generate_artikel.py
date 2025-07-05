from datetime import datetime
import random
import os

# Path folder
artikel_folder = "artikel"
os.makedirs(artikel_folder, exist_ok=True)

# Tanggal hari ini
today = datetime.now().strftime("%Y-%m-%d")
file_name = f"prediksi-hk-{today}.html"
output_path = os.path.join(artikel_folder, file_name)

# Data acak
angka_main = "-".join(str(random.randint(0, 9)) for _ in range(4))
colok_bebas = str(random.randint(0, 9))
angka_2d = "-".join([str(random.randint(10, 99)) for _ in range(3)])

# Template HTML
html_template = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Prediksi togel HK dan angka jitu terpercaya.">
  <title>Prediksi Togel HK {today}</title>
</head>
<body>
  <h1>Prediksi Togel HK {today}</h1>
  <p>Angka jitu, colok bebas, dan bocoran terpercaya dari Unditoto.</p>
  <ul>
    <li>Angka Main: {angka_main}</li>
    <li>Colok Bebas: {colok_bebas}</li>
    <li>2D Top: {angka_2d}</li>
  </ul>
  <a href="https://mez.ink/unditotosini">Kunjungi Unditoto Sekarang</a>
</body>
</html>
"""

# Simpan file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_template)
