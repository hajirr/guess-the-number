from art import logo
import random as r

print(logo)

isPlay = True
EASY = 10
HARD = 5

def level(level):
  global isPlay
  number = r.randint(0, 100)
  while level > 0:
    try:
      print(f"Kamu punya {level} kesempatan")
      tebak = int(input("Tebak nomor : "))
      if tebak == number:
        print("Ya betul")
        level = 0
      elif tebak > number:
        print("Terlalu tinggi")
      elif tebak < number:
        print("Terlalu rendah")
      level -= 1
    except:
      print("Masukan angka, Kesempatan berkurang")
      level -= 1
  play_again = input("Permainan berakhir, main lagi? y/n ")
  if play_again == "y":
    isPlay = True
  else:
    isPlay = False

def main():
  print("Selamat datang dan selamat bermain")

  while isPlay:
    nebak = input('''
        PILIH LEVEL
        1. EASY
        2. HARD
        EASY = 10 KESEMPATAN MENEBAK
        HARD = 5 KESEMPATAN MENEBAK
    ''').lower()
    try:
      if nebak == '1' or nebak == "easy":
        level(EASY)
      elif nebak == '2' or nebak == "hard":
        level(HARD)
    except:
      print("ANDA BELUM MEMASUKAN PILIHAN / PILIHAN ANDA TIDAK TERSEDIA")

main()
  