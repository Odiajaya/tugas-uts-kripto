import base64

def encrypt_caesar(message, shift):
    encrypted_message = ""
    for char in message:
        
      
if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                encrypted_message += 
                encrypted_me
chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                encrypted_message += 
                encrypted_messag
chr((shifted - ord('A')) % 26 + ord('A'))
        
        el
else:
            encrypted_message += char
    
            encrypted_m
return encrypted_message

def base64_encode(message):
    encoded_message = base64.b64encode(message.encode()).decode()
    
    encoded_message = base64.b64encode(message.encode()).decode()
   

    encoded_message = base64.b64encode(message

    encoded_message = b
return encoded_message

# Contoh penggunaan
message = 
message 

m
"Hello, World!"
shift_amount = 
shift_amount

shift
3

encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_encode(encrypted_message)



encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_encode(encrypted_message)

pri


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_encode(encrypted_message


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_encode(encrypted_m


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_encode(encry


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = base64_


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_message = b


encrypted_message = encrypt_caesar(message, shift_amount)
encoded_messa


encrypted_message = encrypt_caesar(message, shift_amount)
encoded


encrypted_message = encrypt_caesar(message, shift_amount)
e


encrypted_message = encrypt_caesar(message, shift_am


encrypted_message = encrypt_caesar(message, s


encrypted_message = encrypt_caesar(mess


encrypted_message = encrypt_caesa


encrypted_message = encryp


encrypted_message =


encrypted_me


enc
print("Pesan Awal:", message)
print("Pesan Terenkripsi (Caesar Cipher):", encrypted_message)

pr
print("Pesan Terenkripsi (Base64):", encoded_message)