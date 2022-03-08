base64_table = [
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
	"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
	"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"
]

def base64encode(data):
	data_binary = "".join(bin(ord(x)) for x in data)
	data_binary = data_binary.replace("b", "")

	data_binary_list = [data_binary[i:i+6] for i in range(0, len(data_binary), 6)]
	
	if len(data_binary_list[-1])!=6:
		zero_pad_length = 6 - len(data_binary_list[-1])
		data_binary_list[-1] = data_binary_list[-1] + "".join([str(0) for _ in range(zero_pad_length)])
	

	encoded_data = [base64_table[int(idx, 2)] for idx in data_binary_list]
	
	equal_padding_length = 4 - len(encoded_data) % 4
	if equal_padding_length:
		for _ in range(equal_padding_length):
			encoded_data.append("=")
	
	encoded_data = "".join(encoded_data)

	return encoded_data


def base64decode(data):
	data = list(data)
	if "=" in data:
		data = list(filter(("=").__ne__, data))
	
	data = [bin(base64_table.index(s)).replace("0b", "") for s in data]
	data = ["0" *(6-len(b)) + b for b in data]
	data = "".join(data)
	data = [data[i:i+8] for i in range(0, len(data), 8)]
	
	if len(data[-1])!=8:
		data = data[:-1]
	
	decoded_data = "".join([chr(int(s, 2)) for s in data])
	return decoded_data