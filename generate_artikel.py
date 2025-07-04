import datetime
import os

# Template artikel HTML
template = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{deskripsi}">
  <title>{judul}</title>
</head>
<body>
  <h1>{judul}</h1>
  <p>{konten}</p>
  <p>Kunjungi situs <a href="https://mez.ink/unditotosini" target="_blank">Unditoto</a> untuk info lengkap prediksi togel harian.</p>
</body>
</html>"""

# Tentukan tanggal hari ini
tanggal = datetime.datetime.now().strftime("%Y-%m-%d")
judul = f"Prediksi Togel HK {tanggal}"
deskripsi = f"Prediksi togel HK hari {tanggal} terbaru dari Unditoto"
konten = f"Berikut ini adalah prediksi togel HK untuk hari {tanggal}. Angka jitu dan bocoran terpercaya hanya dari Unditoto."

# Nama file berdasarkan tanggal
filename = f"artikel/prediksi-hk-{tanggal}.html"

# Buat folder jika belum ada
os.makedirs("artikel", exist_ok=True)

# Simpan file HTML
with open(filename, "w", encoding="utf-8") as f:
    f.write(template.format(judul=judul, deskripsi=deskripsi, konten=konten))

print(f"Artikel '{filename}' berhasil dibuat.")