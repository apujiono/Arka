# 🤝 Cara Berkontribusi ke ARKA

Terima kasih ingin membantu ARKA tumbuh! 🌱

## 📦 Cara Tambah Plugin
1. Buat file di `plugins/nama_plugin.py`
2. Gunakan struktur:
   ```python
   def on_load(arka):
       arka.register_feature(
           name="Nama Plugin",
           description="Deskripsi",
           triggers=["kata kunci"],
           on_message=handle
       )
