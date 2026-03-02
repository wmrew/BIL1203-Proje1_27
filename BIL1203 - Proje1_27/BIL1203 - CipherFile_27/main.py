import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import time
import guvenlik_motoru

# Terminale pip install customtkinter cryptography yazılarak gerekli kütüphaneler yüklenmelidir

ctk.set_appearance_mode("Light")

class SifrelemeUygulamasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Grup 27 - CipherFile v1.0")
        self.geometry("550x600")
        self.resizable(False, False)
        self.configure(fg_color="#FFF8F8")

        
        ana_dizin = os.path.expanduser("~")
        alt_dizinler = ["Desktop", "BIL1203 - Proje1_27", "BIL1203 - CipherFile_27", "metin_belgeleri"]
        
        # Yolların kontrolu
        yol_od = os.path.join(ana_dizin, "OneDrive", *alt_dizinler)
        yol_std = os.path.join(ana_dizin, *alt_dizinler)

        if os.path.exists(os.path.join(ana_dizin, "OneDrive", "Desktop")):
            self.hedef_klasor = yol_od
        else:
            self.hedef_klasor = yol_std

        os.makedirs(self.hedef_klasor, exist_ok=True)

        self.secili_dosya = None
        self.arayuz_hazirla()

    def arayuz_hazirla(self):

        ctk.CTkLabel(self, text="CIPHERFILE GÜVENLİK SİSTEMİ", text_color="#E5A4B4",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=25)

        f_frame = ctk.CTkFrame(self, fg_color="transparent")
        f_frame.pack(pady=10, fill="x", padx=30)
        ctk.CTkButton(f_frame, text="Dosya Seç", fg_color="#FADADD", text_color="#4A4A4A",
                      command=self.dosya_bul).pack(side="left", padx=10)
        self.lbl_dosya = ctk.CTkLabel(f_frame, text="Henüz seçim yapılmadı", text_color="#4A4A4A")
        self.lbl_dosya.pack(side="left")

        ctk.CTkLabel(self, text="Şifreleme Algoritması Seçin:", text_color="#4A4A4A").pack(pady=(15, 5))
        self.alg_secim = ctk.CTkOptionMenu(self, values=["AES", "Sezar"], fg_color="#FADADD", 
                                           button_color="#E5A4B4", text_color="#4A4A4A")
        self.alg_secim.pack(pady=5)

        ctk.CTkLabel(self, text="Güvenlik Parolası:", text_color="#4A4A4A").pack(pady=(15, 5))
        self.ent_parola = ctk.CTkEntry(self, show="*", width=250, border_color="#FADADD")
        self.ent_parola.pack(pady=5)

        b_frame = ctk.CTkFrame(self, fg_color="transparent")
        b_frame.pack(pady=30)
        ctk.CTkButton(b_frame, text="ŞİFRELE", fg_color="#E5A4B4", command=self.sifrele_tikla).pack(side="left", padx=15)
        ctk.CTkButton(b_frame, text="ŞİFRE ÇÖZ", fg_color="#F3B0C3", command=self.coz_tikla).pack(side="left", padx=15)

        self.progress = ctk.CTkProgressBar(self, width=400, progress_color="#E5A4B4")
        self.progress.pack(pady=10)
        self.progress.set(0)

        self.lbl_yol = ctk.CTkLabel(self, text=f"Kayıt Yolu: {self.hedef_klasor}", 
                                    font=("Arial", 9), text_color="#A6A6A6", wraplength=480)
        self.lbl_yol.pack(side="bottom", pady=20)

    def dosya_bul(self):
        yol = filedialog.askopenfilename()
        if yol:
            self.secili_dosya = yol
            self.lbl_dosya.configure(text=os.path.basename(yol))

    def sifrele_tikla(self):
        parola = self.ent_parola.get()
        if not self.secili_dosya or not parola:
            messagebox.showwarning("Eksik!", "Lütfen dosya ve parola belirleyin.")
            return
        try:
            for i in range(1, 11): self.progress.set(i/10); self.update(); time.sleep(0.04)
            sonuc = guvenlik_motoru.dosyayi_sifrele(self.secili_dosya, parola, self.hedef_klasor, self.alg_secim.get())
            messagebox.showinfo("Başarılı", f"Dosya şifrelendi ve kaydedildi:\n{sonuc}")
            self.progress.set(0)
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def coz_tikla(self):
        parola = self.ent_parola.get()
        if not self.secili_dosya or not parola: return
        try:
            for i in range(1, 11): self.progress.set(i/10); self.update(); time.sleep(0.04)
            sonuc = guvenlik_motoru.dosyayi_coz(self.secili_dosya, parola, self.hedef_klasor, self.alg_secim.get())
            messagebox.showinfo("Başarılı", f"Şifre çözüldü!\nDosya konumu: {sonuc}")
            self.progress.set(0)
        except Exception:
            self.progress.set(0)
            messagebox.showerror("Hata", "Yanlış parola veya uyumsuz algoritma!")

if __name__ == "__main__":
    app = SifrelemeUygulamasi()
    app.mainloop()