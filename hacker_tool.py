import os
import sys
import time
import random
import urllib.request
import threading
import json

# Import library untuk tampilan (Pastikan sudah diinstall via pkg install figlet termcolor)
try:
    from termcolor import colored, cprint
    from figlet import figlet
except ImportError:
    cprint("Instal library: pkg install figlet termcolor", "cyan")
    sys.exit()

# --- Konfigurasi Warna & Tampilan ---
COLORS = {
    "green": "green",
    "red": "red",
    "yellow": "yellow",
    "cyan": "cyan",
    "white": "white",
    "magenta": "magenta"
}

def clear_screen():
    os.system('clear')

def print_logo():
    clear_screen()
    logo = figlet("WORM-HACKER", font="slant")
    cprint(logo, "cyan")
    cprint("=" * 50, "white")
    cprint("Target: WhatsApp Number | Platform: Termux | Mode: Dark", "yellow")
    cprint("=" * 50, "white")
    time.sleep(1.5)

def animate_typing(text, color="white", speed=0.05):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_target():
    print("\n")
    target = input(colored("[+] Masukkan Nomor WA Korban (format: 628...): ", "cyan"))
    return target

# --- Opsi Virus ---

def virus_lag(target):
    clear_screen()
    cprint(f"[*] Memulai serangan RAM & CPU pada target: {target}...", "red")
    time.sleep(2)
    cprint("[!] Menginjakan memori...", "yellow")
    for i in range(10):
        time.sleep(0.8)
        cprint(f"[#] Penggunaan RAM Target: {random.randint(85, 99)}%...", "red")
    cprint("\n[SUCCESS] HP Korban sekarang LAG berat!", "green")
    input("Tekan Enter untuk lanjut...")

def virus_bad_network(target):
    clear_screen()
    cprint(f"[*] Mengganggu paket data jaringan pada {target}...", "red")
    time.sleep(2)
    cprint("[!] Mengirim paket sampah (Junk Packets)...", "yellow")
    for i in range(8):
        time.sleep(1)
        cprint(f"[#] Ping Loss: {random.randint(40, 95)}% | Latency: {random.randint(500, 2000)}ms", "red")
    cprint("\n[SUCCESS] Jaringan HP Korban sangat jelek!", "green")
    input("Tekan Enter untuk lanjut...")

def virus_reset(target):
    clear_screen()
    cprint(f"[*] Inisialisasi perintah Factory Reset pada {target}...", "red")
    time.sleep(2)
    cprint("[!] Mengirim payload ADB: 'adb factory-reset'...", "yellow")
    time.sleep(3)
    cprint("[!] Proses reset dimulai...", "magenta")
    time.sleep(2)
    cprint("\n[SUCCESS] HP Korban sedang di-reset (Data hilang)!", "green")
    input("Tekan Enter untuk lanjut...")

def virus_custom_text(target):
    clear_screen()
    text_msg = input(colored("[-] Masukkan Text yang ingin muncul di layar korban: ", "cyan"))
    cprint(f"[*] Mengirim notifikasi pop-up ke {target}...", "red")
    time.sleep(2)
    # Simulasi pengiriman via web link (WhatsApp API sederhana)
    url = f"https://wa.me/{target}?text={text_msg}"
    cprint("[!] Membuka WhatsApp Web untuk mengirim pesan...", "yellow")
    time.sleep(1)
    # Di Termux, ini akan membuka browser jika ada, atau mencetak link
    cprint(f"\n[SUCCESS] Text terdeteksi: '{text_msg}'", "green")
    cprint(f"Link dikirim: {url}", "magenta")
    input("Tekan Enter untuk lanjut...")

def virus_ddos(target):
    clear_screen()
    cprint(f"[*] Memulai serangan DDoS (UDP Flood) ke {target}...", "red")
    cprint("[!] Menghubungkan botnet...", "yellow")
    
    def flood():
        for i in range(50):
            try:
                # Simulasi request HTTP ke WhatsApp gateway (contoh)
                urllib.request.urlopen(f"http://api.whatsapp.com/send?phone={target}", timeout=2)
            except:
                pass
            cprint(f"[#] Paket ke- {i+1} dikirim...", "cyan")
            time.sleep(0.1)

    t = threading.Thread(target=flood)
    t.start()
    t.join()
    
    cprint("\n[SUCCESS] Server WhatsApp target overload!", "green")
    input("Tekan Enter untuk lanjut...")

def virus_malware(target):
    clear_screen()
    cprint(f"[*] Menginfiltrasi Malware (Trojan Horse) ke {target}...", "red")
    time.sleep(2)
    cprint("[!] Menyuntikkan kode ke database WhatsApp...", "yellow")
    time.sleep(2)
    cprint("[!] Mengambil daftar kontak dan chat...", "magenta")
    time.sleep(2)
    cprint("\n[SUCCESS] Malware aktif! Data korban terenkripsi & terkirim ke server kita.", "green")
    input("Tekan Enter untuk lanjut...")

# --- Menu Utama ---

def main_menu(target):
    while True:
        clear_screen()
        print_logo()
        print(colored(f"Target: {target}", "cyan"))
        print(colored("=" * 30, "white"))
        print("PILIHAN VIRUS:")
        print("  [1] HP Lag (RAM Overload)")
        print("  [2] Jaringan Jelek (Ping Loss)")
        print("  [3] HP Reset (Factory Reset)")
        print("  [4] Custom Text (Pop-up di Layar)")
        print("  [5] DDoS Attack (Flood Server)")
        print("  [6] Malware (Trojan & Data Leak)")
        print("  [7] Keluar")
        print(colored("=" * 30, "white"))
        
        choice = input(colored("[?] Pilih Virus (1-7): ", "magenta"))
        
        if choice == '1':
            virus_lag(target)
        elif choice == '2':
            virus_bad_network(target)
        elif choice == '3':
            virus_reset(target)
        elif choice == '4':
            virus_custom_text(target)
        elif choice == '5':
            virus_ddos(target)
        elif choice == '6':
            virus_malware(target)
        elif choice == '7':
            cprint("Exiting WormHacker...", "yellow")
            sys.exit()
        else:
            cprint("Pilihan tidak valid!", "red")
            time.sleep(1)

# --- Jalankan Program ---
if __name__ == "__main__":
    print_logo()
    target = get_target()
    if not target:
        cprint("Nomor tidak boleh kosong!", "red")
        sys.exit()
    main_menu(target)
