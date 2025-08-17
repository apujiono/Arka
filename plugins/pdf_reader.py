def on_load(arka):
    arka.register_feature(
        name="PDF Reader",
        description="Baca dan pahami dokumen PDF",
        triggers=["baca", "upload", "pelajari"],
        on_message=handle_pdf_request
    )

def handle_pdf_request(message, file=None):
    if file and file.endswith(".pdf"):
        return f"Aku sedang baca {file}... Nanti aku kasih ringkasannya."
    return "Kirim file PDF, aku akan baca."
