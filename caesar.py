#!/usr/bin/python3

# This file is used to encrypt/decrypt using caesar cipher technique
# It's written in python but you can easily translate it into any language 

def main():
	text = input("Enter the text you want to encrypt/decrypt :")
	ch = int(input("Enter the choice : 1) Encrypt or 2) Decrypt :"))
	shift = int(input("Enter the shift you want :"))
	if ch == 1:
		print("Encrypting...")
		encstr = ""
		for i in text:
			if i.isupper():
				encstr += chr((ord(i) + shift-65) % 26 + 65)
			else:
				encstr += chr((ord(i) + shift-97) % 26 + 97)
		print("Encrypted text is :", encstr)

	else:
		print("Decrypting...")
		decstr = ""
		for i in text:
			if i.isupper():
				decstr += chr((ord(i) - shift-65) % 26 + 65)
			else:
				decstr += chr((ord(i) - shift-97) % 26 + 97)
		print("Decrypted text is :", decstr)

if __name__ == "__main__":
	main()