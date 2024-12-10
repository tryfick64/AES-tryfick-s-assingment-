if __name__ == '__main__':
    from funcs import encode_str, decode_str

    key_str = '0f1571c947d9e8590cb7add6af7f6798'
    text = "0123456789abcdeffedcba9876543210"
    print(encode_str(text, key_str))
    print(decode_str(encode_str(text, key_str), key_str))
# должно получиться ff0b844a0853bf7c6934ab4364148fb9


# в encode_str можно заменить byte_str_to_blocks на text_to_blocks но тогда надо обратно как то шифровать в ютф-8
