import random
import os

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Papan permainan: posisi awal (0) hingga finish (100)
# Key: posisi awal, value: posisi akhir
snakes = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}

ladders = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}

def check_snake_or_ladder(position):
    """Cek apakah posisi kena ular atau tangga"""
    if position in snakes:
        print(f"🐍 Wah kena ular! Turun dari {position} ke {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"🪜 Hore dapat tangga! Naik dari {position} ke {ladders[position]}")
        return ladders[position]
    else:
        return position

def roll_dice():
    """Melempar dadu (1-6)"""
    return random.randint(1, 6)

def display_status(player_name, position):
    """Menampilkan status pemain"""
    print(f"{player_name} sekarang berada di kotak {position}")

def main():
    clear_screen()
    print("=" * 30)
    print("   SELAMAT DATANG DI ZONA ULAR")
    print("=" * 30)
    
    player_name = input("Masukkan nama pemain: ").strip()
    if not player_name:
        player_name = "Pemain"
    
    position = 0  # Mulai dari kotak 0 (sebelum kotak 1)
    
    while position < 100:
        input(f"\n{player_name}, tekan Enter untuk melempar dadu...")
        dice = roll_dice()
        print(f"🎲 Dadu menunjukkan angka {dice}")
        
        # Pindah posisi
        new_position = position + dice
        
        if new_position > 100:
            print(f"Melebihi 100 ({new_position}), harus tepat 100 untuk menang! Tetap di {position}")
            continue
        
        position = new_position
        display_status(player_name, position)
        
        # Cek apakah posisi kena efek ular/tangga
        position = check_snake_or_ladder(position)
        
        if position == 100:
            clear_screen()
            print("\n" + "=" * 30)
            print(f"🎉🎉🎉 SELAMAT! {player_name} MENANG! 🎉🎉🎉")
            print("=" * 30)
            break
        
        # Jika posisi setelah efek tetap 100, menang
        if position == 100:
            clear_screen()
            print("\n" + "=" * 30)
            print(f"🎉🎉🎉 SELAMAT! {player_name} MENANG! 🎉🎉🎉")
            print("=" * 30)
            break

if __name__ == "__main__":
    main()