from sp_network import sp_encode, sp_decode
from config import s_tables, p_tables


def text_to_list16bit(text):
    list16bit = []
    for i in text:
        list16bit.append(format(ord(i), '016b'))
    return list16bit


def list_16bit_to_hex(list_16bit):
    hex_list = []
    for i in list_16bit:
        n = int(i, 2)
        n = n.to_bytes(2, 'big').hex()
        hex_list.append(n)
    return hex_list


def hex_to_list_16bit(hex_list):
    list_16bit = []
    for i in hex_list:
        n = int(i, 16)
        n = format(n, '016b')
        list_16bit.append(n)
    return list_16bit


def list16bit_to_text(list16bit):
    text = ""
    for i in list16bit:
        text += chr(int(i, 2))
    return text


def clip_text(text):
    n = text_to_list16bit(text)
    enc_16bit = []
    for i in n:
        n = sp_encode(i, s_tables, p_tables)
        enc_16bit.append(n)
    hex_list = list_16bit_to_hex(enc_16bit)
    return " ".join(hex_list)


def plain_text(clip_list):
    clip_list = clip_list.split()
    n = hex_to_list_16bit(clip_list)
    dec_16bit = []
    for i in n:
        ln = sp_decode(i, s_tables, p_tables)
        dec_16bit.append(ln)
    res = list16bit_to_text(dec_16bit)
    return res

"""
m = text_to_list16bit("ЇїІі Привіт світе, вітаю вас!")
m1 = list16bit_to_text(m)
print(m)
print(m1)
cc = "Вісьсьсь"
print(clip_text(cc))
print(plain_text(clip_text(cc)))
"""