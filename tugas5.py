def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = 
    plaintex

    pla

  
""
    
   
for char in ciphertext:
        
        

   
if char.isalpha():
            
           

     
if char.islower():
                decrypted_char = 
                decrypted_char = c

                decrypted_char

                decrypted_

                decryp

                de

              

          

      

  
chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            
            els

          

     
else:
                decrypted_char = 
                decrypted_char =

                decrypted_

                decr

              

       

  
chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            plaintext += decrypted_char
        
            plaintext += decrypted_char
     

            plaintext += decrypted_ch

            plaintext += decr

            plaintext 

            pla

          

     
else:
            plaintext += char
    
            plaintext += char
    retur

            plaintext += char
   

            plaintext += ch

            plaintext

            pla

       
return plaintext

# Contoh penggunaan
ciphertext = 
ciphertext 

ciphert

ci
"Ifmmp xpsme!"
shift_value = 
shift_value 

shift_va

shif
1
decrypted_text = decrypt_caesar_cipher(ciphertext, shift_value)


decrypted_text = decrypt_caesar_cipher(ciphertext, shift_value)

decrypted_text = decrypt_caesar_cipher(ciphertext, shift_

decrypted_text = decrypt_caesar_cipher(ciphertext

decrypted_text = decrypt_caesar_cipher(ci

decrypted_text = decrypt_caesar_c

decrypted_text = decrypt_ca

decrypted_text = decr

decrypted_text 

decrypted_

decry
print(f"Ciphertext: {ciphertext}")

pri
print(f"Decrypted text: {decrypted_text}")