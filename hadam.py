import numpy as np

def hadamard(n):
    if n == 0:
        return np.array([[1]])
    H = hadamard(n - 1)
    return np.block([[H, H], [H, -H]])

def get_H(size):
    n = 0
    while 2**n < size:
        n += 1
    return hadamard(n)

def encrypt(text, n):
    H = hadamard(n)
    size = H.shape[0]
    v = np.array([ord(c) for c in text] + [0] * (size - len(text)), dtype=float)
    encrypted = H @ v
    return H, v, encrypted

def decrypt(enc, H):
    v = (H.T / H.shape[0]) @ enc
    return ''.join(chr(int(round(x))) for x in v if int(round(x)) > 0)

print("=== Hadamard Cipher ===")

while True:
    print("\n1. Szyfruj\n2. Wyjście")
    c = input(">> ")

    if c == '1':
        text = input("Podaj słowo: ")

        print(f"\nDostępne macierze:")
        print("  n=1 →  2x2")
        print("  n=2 →  4x4")
        print("  n=3 →  8x8")
        print("  n=4 → 16x16")

        try:
            n = int(input("Wybierz n: "))
            if n < 1 or n > 4:
                print("Podaj n od 1 do 4!")
                continue
        except ValueError:
            print("Podaj liczbę!")
            continue

        size = 2**n
        if len(text) > size:
            print(f"Słowo za długie! Dla n={n} max {size} znaków.")
            continue

        H, v, enc = encrypt(text, n)

        print(f"\n--- Tekst: '{text}' ---")

        print(f"\nWektor ASCII (tekst -> liczby):")
        print([int(x) for x in v])

        print(f"\nMacierz Hadamarda ({size}x{size}):")
        print(H.astype(int))

        print(f"\nWynik szyfrowania (H x wektor):")
        print([int(x) for x in enc])

        print(f"\nOdszyfrowany tekst:")
        print(decrypt(enc, H))

    elif c == '2':
        break