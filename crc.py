
def xor(a, b): 

 	result = [] 
 	for i in range(1, len(b)): 

		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 
 
def mod2div(dividend, divisor): 

 	cur = len(divisor) 
  	tmp = dividend[0 : cur] 

	while cur < len(dividend): 
		if tmp[0] == '1': 
 			tmp = xor(divisor, tmp) + dividend[cur] 
		else: 
			tmp = xor('0'*cur, tmp) + dividend[cur] 
		cur += 1

 	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 

	else: 
		tmp = xor('0'*cur, tmp) 

	ch = tmp 
	return ch 

def decodeData(data, key): 

	l_key = len(key) 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 
	return remainder 

def encodeData(data, key): 

	l_key = len(key) 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 
	codeword = data + remainder 
	return codeword	 
