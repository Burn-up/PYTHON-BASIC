secret_number = 9

while True:
    answer = int(input("Tebak angka rahasia : "))

    if answer == secret_number:
        print("Tebakan benar")
        break
    else:
        print("Jawaban salah coba lagi")
