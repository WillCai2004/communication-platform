import gnupg
import os

gnupg_home = os.path.abspath('./gnupg_home')
gpg = gnupg.GPG(gnupghome=gnupg_home)

os.makedirs('./gnupg_home', exist_ok = True)

def generate_keys(name, email):
    input_data = gpg.gen_key_input(
        name_real = name,
        name_email = email,
        passphrase = 'your_passphrase'
    )
    key = gpg.gen_key(input_data)
    print(f"Key generation complete, fingerprint: {key.fingerprint}")
    return key.fingerprint

def encrypt_message(message, recipient_fingerprint):
    encrypt_data = gpg.encrypt(
        message,
        recipients = [recipient_fingerprint],
        always_trust = True #!!only for testing
    )
    if encrypt_data.ok:
        print("Encryption success.")
        return str(encrypt_data)
    else:
        print("encryption failed.")
        return None
    
def decrypt_message(encrypted_message, passphrase):
    decrypt_data = gpg.decrypt(encrypted_message, passphrase = passphrase)
    if decrypt_data.ok:
        print("Decryption success.")
        return str(decrypt_data)
    else:
        print("Decryption failed.")
        return None
    
# testing
if __name__ == "__main__":
    fingerprint = generate_keys("Test User","testemail@testemail.com")
    plaintext = "test messssssssssssssage"
    
    encrypted = encrypt_message(plaintext, fingerprint)
    print(f"Encrypted: \n{encrypted}")
    
    decrypted = decrypt_message(encrypted, "your_passphrase")
    print(f"Decrypted: \n{decrypted}")
    