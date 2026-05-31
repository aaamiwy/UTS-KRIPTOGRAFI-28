from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import time

print("=" * 60)
print("IMPLEMENTASI KRIPTOGRAFI ASIMETRIS (RSA)")
print("=" * 60)

plaintext = input("\nMasukkan plaintext yang akan dienkripsi: ")
data = plaintext.encode()

# Generate Public & Private Key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Enkripsi
start_encrypt = time.perf_counter()

ciphertext = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

end_encrypt = time.perf_counter()

# Dekripsi
start_decrypt = time.perf_counter()

decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

end_decrypt = time.perf_counter()

encrypt_time = end_encrypt - start_encrypt
decrypt_time = end_decrypt - start_decrypt

print("\n" + "=" * 60)
print("HASIL ENKRIPSI DAN DEKRIPSI")
print("=" * 60)

print(f"\nPlaintext        : {plaintext}")
print(f"Ciphertext (HEX) : {ciphertext.hex()}")
print(f"Hasil Dekripsi   : {decrypted.decode()}")

print("\nSTATISTIK")
print("-" * 60)
print(f"Waktu Enkripsi   : {encrypt_time:.8f} detik")
print(f"Waktu Dekripsi   : {decrypt_time:.8f} detik")
print(f"Ukuran Plaintext : {len(data)} byte")
print(f"Ukuran Ciphertext: {len(ciphertext)} byte")