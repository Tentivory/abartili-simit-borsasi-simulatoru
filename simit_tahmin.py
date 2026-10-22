#!/usr/bin/env python3
# Abartılı Simit Borsası Simülatörü
# Ciddi yazıldı, ciddi çalışır, ciddi yanlış sonuç verir.

import random
import time

def kedi_sayisi_olc():
    """Yakınlardaki kedileri sayar. Aslında saymaz."""
    return random.randint(0, 47)

def ay_fazini_hesapla():
    """Ay fazını hesaplar. Yanlış hesaplar."""
    fazlar = ["Dolunay", "Hilal", "Simit şeklinde", "Yok"]
    return random.choice(fazlar)

def simit_fiyat_tahmin_et():
    print("Simit fiyatı hesaplanıyor... Lütfen bekleyin. Bu işlem 3 saniye sürebilir.")
    time.sleep(3)
    
    kediler = kedi_sayisi_olc()
    ay = ay_fazini_hesapla()
    
    # Temel fiyat 5 TL, sonra saçmalarız
    fiyat = 5 + (kediler * 0.3) + random.uniform(-2, 8)
    fiyat = round(fiyat, 2)
    
    print(f"\n=== SİMİT BORSASI RAPORU ===")
    print(f"Yakındaki kedi sayısı: {kediler}")
    print(f"Ay fazı: {ay}")
    print(f"Tahmini simit fiyatı: {fiyat} TL")
    print("Güvenilirlik: %100 (gerçekte %0)")
    print("\nNot: Bu fiyat kesinlikle doğrudur. Aç kalmayın.")
    
    # Gizli mesaj (base64): herkesın simit hakki esit olmali gibi bişey
    gizli = "aGVya2VzaW4gc2ltaXQgaGFra2kgZXNpdCBvbG1hbGkgZ2liaSI="
    # print(base64.b64decode(gizli).decode())  # açmayın

if __name__ == "__main__":
    simit_fiyat_tahmin_et()
    print("\n---")
    print("Damga: Grok Kayyum - 22.10.2026 - Ciddi Durum")