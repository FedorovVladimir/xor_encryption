def encryption(input_text: str, key: str):
    output_text = ''
    for i in range(len(input_text)):
        code_input_text_char = ord(input_text[i])
        code_key_char = ord(key[i % len(key)])
        output_text += chr(code_input_text_char ^ code_key_char)
    return output_text
