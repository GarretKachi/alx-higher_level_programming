#!/usr/bin/python3
# ASCII value for lowercase 'a'
start = ord('a')
# ASCII value for lowercase 'z'
end = ord('z')
# Loop through the ASCII values and print the corresponding character
for ascii_value in range(start, end + 1):
    print(chr(ascii_value), end='')
