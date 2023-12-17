import tkinter as tk
from tkinter import font
import time

start_time = 0


def start_test():
    global start_time
    start_time = time.time()
    text_entry.delete(1.0, tk.END)
    result_label.config(text="")

    # Kullanıcı metni yazmayı bitirdiğinde Enter tuşuna basar ve 'end_test' fonksiyonu çalışır
    text_entry.bind("<Return>", end_test)


def end_test(event):
    end_time = time.time()
    elapsed_time = end_time - start_time
    typed_text = text_entry.get(1.0, tk.END).strip()

    # Dakikadaki yazılan kelime sayısını hesapla ve göster (WPM)
    word_count = len(typed_text.split())
    wpm = round((word_count / elapsed_time) * 60)
    result_label.config(text=f"Yazma hızınız: {wpm} kelime/dakika")


# Ana pencereyi oluştur
root = tk.Tk()
custom_font = font.Font(family="Helvetica", size=14)

root.title('Yazma Hızı Testi')

# Test metni
test_metni = ("Bir gün bir çocuk annesine sordu: 'Gerçek nedir?' Annesi cevap verdi: "
              "'Gerçek, güneşin doğuşudur, yağmurun yağmasıdır.' Çocuk düşündü ve dedi ki: "
              "'Peki, rüyalarımızda gördüklerimiz gerçek mi?'")

# Metni görüntüle
text_label = tk.Label(root, text=test_metni, wraplength=400, font=custom_font)
text_label.pack()

# Kullanıcının metin yazacağı kutucuk
text_entry = tk.Text(root, height=8, width=50)
text_entry.pack()

# Testi başlat
start_button = tk.Button(root, text="Testi Başlat", command=start_test)
start_button.pack(pady=10)

# Sonucu gösterecek label (başlangıçta görünmez)
result_label = tk.Label(root, text="", font=custom_font)
result_label.pack()

root.mainloop()
