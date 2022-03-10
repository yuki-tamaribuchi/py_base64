from base64.base64 import base64encode, base64decode

if __name__ == "__main__":
	data = b"ABCDEFG"

	print("data: ", data)

	encoded_data = base64encode(data)

	print("encoded_data:", encoded_data)

	decoded_data = base64decode(encoded_data)

	print("decoded_data: ", decoded_data)