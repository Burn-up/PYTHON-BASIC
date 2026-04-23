umur = int(input("Masukan umur anda : "))

# validasi umur
if umur >= 17:
    print("Anda sudah memenuhi syarat untuk membuat ktp dan sim")
elif umur < 17:
    print("Umur anda tidak mememuhi syarat untuk membuat ktp ataupun sim")
else:
    print("Input tidak valid")
