def my_encoder(en_string: str):
    res = bytes(' '.join(format(ord(i), 'b') for i in en_string), 'ascii')    
    return res

def my_decoder(de_bytes: bytes):
    final_string = ''.join([chr(int(i, 2)) for i in de_bytes.split()])  
    return final_string

test_str = input('enter: ')

temp = my_encoder(test_str)

print(temp.decode('ascii'))

print(my_decoder(temp))