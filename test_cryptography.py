from cryptography.fernet import Fernet

# Generate a key (Do this once and store it securely)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> bytes:
    """Encrypt a message using Fernet encryption."""
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    """Decrypt a Fernet-encrypted message."""
    return cipher.decrypt(encrypted_message).decode()

# Example Usage
if __name__ == "__main__":
    original_message = "Hello, this is a secret message!"
    encrypted_msg = encrypt_message(original_message)
    decrypted_msg = decrypt_message(encrypted_msg)

    print(f"Original: {original_message}")
    print(f"Encrypted: {encrypted_msg}")
    print(f"Decrypted: {decrypted_msg}")
