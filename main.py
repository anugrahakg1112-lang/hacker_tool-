import os
import sys
import time
import random
import threading
import urllib.request

# --- Konfigurasi Warna ANSI (Tanpa Library Eksternal) ---
class Color:
    R = "\033[31m"    # Merah
    G = "\033[32m"    # Hijau
    C = "\033[36m"    # Cyan
    Y = "\033[33m"    # Kuning
    M = "\033[35m"    # Magenta
    W = "\033[37m"    # Putih
    B = "\033[34m"    # Biru
    RST = "\033[0m"   # Reset

def clear():
    os.system('clear')

def logo():
    clear()
    art = f"""
{Color.C}  _____ _____   _____  _____  _____ 
 {Color.C} |  __ \_   _| |  __ \|  __ \|  __ \
 {Color.C} | |  \ || |   | |__) | |__) | |__) |
 {Color.C} | |__/ || |   |  ___/|  _  /|  _  / 
 {Color.C} |_____/ |_|   |_|    |_| \_\|_| \_\ 
 {Color.C}                                    
{Color.R}  SYSTEM: WORM-HACKER v2.0 | STATUS: ONLINE
{Color.W}"""
    print(art)
    print(f"{Color.Y}{'='*50}{Color.RST}")
    print(f"{Color.M}[+] Target: WhatsApp Number | Mode: Dark{Color.RST}")
    print(f"{Color.G}[+] Fitur: 5 Virus Aktif + Custom Text{Color.RST}")
    print(f"{Color.Y}{'='*50}{Color.RST}\n")
    time.sleep(1.2)

def typing(text, color, speed=0.03):
    for char in text:
        sys.stdout.write(f"{color}{char}{Color.RST}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_target():
    typing("Masukkan Nomor WA Korban (Contoh: 62812345678):", Color.C)
    target = input(f"{Color.M}>> {Color.RST}")
    if not target:
        typing("Error: Nomor tidak boleh kosong!", Color.R)
        sys.exit()
    return target

# --- FUNGSI VIRUS ---

def v1_lag(target):
    clear()
    typing(f"MEMULAI SERANGAN RAM OVERLOAD ke {target}...", Color.R)
    time.sleep(1)
    typing("Injecting loop... ", Color.Y)
    for i in range(10):
        time.sleep(0.5)
        val = random.randint(88, 99)
        print(f"\r{Color.M}[+] Memori HP Korban: {val}% (LAG DETECTED){Color.RST}", end="", flush=True)
    print(f"\n{Color.G}[SUCCESS] HP Korban sangat LAG!{Color.RST}")
    time.sleep(2)

def v2_network(target):
    clear()
    typing(f"MEMULAI SERANGAN JARINGAN (PING LOSS) ke {target}...", Color.R)
    time.sleep(1)
    typing("Sending Junk Packets... ", Color.Y)
    for i in range(8):
        time.sleep(0.8)
        ping = random.randint(400, 2000)
        loss = random.randint(45, 98)
        print(f"\r{Color.M}[!] Ping: {ping}ms | Loss: {loss}%{Color.RST}", end="", flush=True)
    print(f"\n{Color.G}[SUCCESS] Jaringan HP Korban terputus-putus!{Color.RST}")
    time.sleep(2)

def v3_reset(target):
    clear()
    typing(f"MEMULAI PERINTAH FACTORY RESET ke {target}...", Color.R)
    time.sleep(1.5)
    typing("Sending ADB Payload: 'adb factory-reset'...", Color.Y)
    time.sleep(2)
    typing("Clearing Data...", Color.M)
    print(f"\n{Color.G}[SUCCESS] HP Korban sedang di-RESET (Data Hilang)!{Color.RST}")
    time.sleep(2)

def v4_custom(target):
    clear()
    typing(f"MEMULAI MODE CUSTOM TEXT ke {target}...", Color.R)
    text = input(f"{Color.C}Masukkan Pesan untuk Layar Korban: {Color.RST}")
    typing("Sending Pop-up Notification...", Color.Y)
    time.sleep(1)
    url = f"https://wa.me/{target}?text={text}"
    print(f"\n{Color.M}[!] Link Aktif: {url}{Color.RST}")
    print(f"{Color.G}[SUCCESS] Pesan '{text}' siap dikirim ke layar korban!{Color.RST}")
    time.sleep(2)

def v5_ddos(target):
    clear()
    typing(f"MEMULAI SERANGAN DDoS (UDP FLOOD) ke {target}...", Color.R)
    typing("Connecting to Botnet...", Color.Y)
    
    def flood():
        for i in range(50):
            try:
                urllib.request.urlopen(f"http://api.whatsapp.com/send?phone={target}", timeout=1)
            except:
                pass
            print(f"\r{Color.C}[+] Paket DDoS ke-{i+1} dikirim...{Color.RST}", end="", flush=True)
            time.sleep(0.1)
    
    t = threading.Thread(target=flood)
    t.start()
    t.join()
    print(f"\n{Color.G}[SUCCESS] Server WhatsApp Target Overload!{Color.RST}")
    time.sleep(2)

def v6_malware(target):
    clear()
    typing(f"MEMULAI INJEKSI MALWARE (TROJAN) ke {target}...", Color.R)
    time.sleep(1)
    typing("Uploading Trojan.exe...", Color.Y)
    time.sleep(1.5)
    typing("Decrypting Chat History...", Color.M)
    time.sleep(1)
    typing("Stealing Contacts...", Color.M)
    print(f"\n{Color.G}[SUCCESS] Malware Aktif! Data Korban terkirim ke Server Kita.{Color.RST}")
    time.sleep(2)

# --- MENU UTAMA ---

def menu(target):
    while True:
        clear()
        logo()
        print(f"{Color.W}[TARGET]: {target}{Color.RST}\n")
        print(f"{Color.Y} 1. {Color.R}HP LAG (RAM Overload)   {Color.W}2. {Color.C}Jaringan Jelek (Ping Loss)   {Color.W}3. {Color.M}HP RESET (Factory Reset)")
        print(f"{Color.Y} 4. {Color.G}Custom Text (Pop-up)       {Color.W}5. {Color.B}DDoS Attack (Flood)          {Color.W}6. {Color.R}Malware (Trojan)")
        print(f"{Color.Y} 7. {Color.W}Keluar (Exit)               {Color.RST}\n")
        
        choice = input(f"{Color.M}[?] Pilih Virus (1-7): {Color.RST}")
        
        if choice == '1': v1_lag(target)
        elif choice == '2': v2_network(target)
        elif choice == '3': v3_reset(target)
        elif choice == '4': v4_custom(target)
        elif choice == '5': v5_ddos(target)
        elif choice == '6': v6_malware(target)
        elif choice == '7':
            typing("Exiting Worm Hacker...", Color.Y)
            sys.exit()
        else:
            typing("Pilihan Salah! Coba Lagi.", Color.R)
            time.sleep(1)

# --- JALANKAN ---
if __name__ == "__main__":
    try:
        logo()
        target = get_target()
        menu(target)
    except KeyboardInterrupt:
        print(f"\n{Color.R}Terminated by User{Color.RST}")
        sys.exit()
