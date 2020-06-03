def encryption(input_text: [], key: str):
    output_text = b''
    for i in range(len(input_text)):
        code_input_text_byte = input_text[i]
        code_key_byte = ord(key[i % len(key)])
        output_text += (code_input_text_byte ^ code_key_byte).to_bytes(1, byteorder='little')
    return output_text
