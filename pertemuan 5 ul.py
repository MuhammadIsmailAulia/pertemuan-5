# dictionaries.py

# 1. Membuat Dictionary
# Format: { kunci: nilai }
mobil = {
    "merek": "Toyota",
    "model": "GR Yaris",
    "tahun": 2023,
    "warna": "Putih"
}

print("--- Dictionary Awal ---")
print(mobil)

# 2. Mengakses Nilai
# Menggunakan bracket [] atau method .get()
print(f"\nMerek Mobil: {mobil['merek']}")
print(f"Model Mobil: {mobil.get('model')}")

# 3. Mengubah dan Menambah Data
mobil["tahun"] = 2024  # Mengubah nilai yang ada
mobil["transmisi"] = "Manual"  # Menambah pasangan baru
print(f"\nSetelah Update: {mobil}")

# 4. Menghapus Data
# pop() menghapus kunci tertentu, del juga bisa digunakan
mobil.pop("warna")
# del mobil["tahun"] 

# 5. Iterasi (Looping) melalui Dictionary
print("\n--- Iterasi Data ---")
for key, value in mobil.items():
    print(f"{key.capitalize()}: {value}")

# 6. Cek apakah Kunci ada di Dictionary
if "model" in mobil:
    print("\nKunci 'model' ditemukan dalam data.")

# 7. Dictionary di dalam List (Kasus Nyata)
database_user = [
    {"username": "budi_keren", "id": 101},
    {"username": "sari_smart", "id": 102}
]

print("\n--- Database User ---")
for user in database_user:
    print(f"ID: {user['id']} | Nama: {user['username']}")

# 8. Membersihkan Dictionary
mobil.clear()
print(f"\nStatus Dictionary Mobil: {mobil} (Kosong)")