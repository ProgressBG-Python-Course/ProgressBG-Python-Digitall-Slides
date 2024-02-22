# Example Python code for encoding with different schemes
text = "Здравей, свят!"

# encoding
utf8_encoded = text.encode('utf-8')
print("UTF-8 Encoded:", utf8_encoded)

# decoding
decoded_text = utf8_encoded.decode('cp1251')
print(decoded_text)

# # ASCII encoding (will raise UnicodeEncodeError for non-ASCII characters)
# try:
#     ascii_encoded = text.encode('ascii')
#     print("ASCII Encoded:", ascii_encoded)
# except UnicodeEncodeError as e:
#     print("Error:", e)