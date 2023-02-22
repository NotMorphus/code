#!/usr/bin/bash

# This file is used to encrypt and decrypt a ROT13 cipher with input from the user
# We could have used python but its fun when its bash sometimes

echo -n "Enter the text you want to encrpyt/decrypt with ROT13 :"
read text
echo "1. Encrypt"
echo "2. Decrypt"
echo -n "Enter the choice :"
read ch
if [ $ch -eq 1 ]
then
    enc=$(echo $text | tr '[A-M][N-Z][a-m][n-z]' '[N-Z][A-M][n-z][a-m]')
    echo "The encrypted text is :"$enc
    break
else
    dec=$(echo $text | tr '[N-Z][A-M][n-z][a-m]' '[A-M][N-Z][a-m][n-z]')
    echo "The decrypted text is :"$dec
    break
fi