from cryptography.fernet import Fernet
import time

print("=" * 60)
print("IMPLEMENTASI KRIPTOGRAFI SIMETRIS (FERNET)")
print("=" * 60)

plaintext = input("\nMasukkan plaintext yang akan dienkripsi: ")
data = plaintext.encode()

# Generate Key
key = Fernet.generate_key()
cipher = Fernet(key)

# Enkripsi
start_encrypt = time.perf_counter()
ciphertext = cipher.encrypt(data)
end_encrypt = time.perf_counter()

# Dekripsi
start_decrypt = time.perf_counter()
decrypted = cipher.decrypt(ciphertext)
end_decrypt = time.perf_counter()

encrypt_time = end_encrypt - start_encrypt
decrypt_time = end_decrypt - start_decrypt

print("\n" + "=" * 60)
print("HASIL ENKRIPSI DAN DEKRIPSI")
print("=" * 60)

print(f"\nPlaintext        : {plaintext}")
print(f"Key              : {key.decode()}")
print(f"Ciphertext       : {ciphertext.decode()}")
print(f"Hasil Dekripsi   : {decrypted.decode()}")

print("\nSTATISTIK")
print("-" * 60)
print(f"Waktu Enkripsi   : {encrypt_time:.8f} detik")
print(f"Waktu Dekripsi   : {decrypt_time:.8f} detik")
print(f"Ukuran Plaintext : {len(data)} byte")
print(f"Ukuran Ciphertext: {len(ciphertext)} byte")