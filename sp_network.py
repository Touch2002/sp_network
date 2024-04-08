def s_block(bits, s_table):
    """Приймає набір бітів та таблицю заміни, перетворює набір бітів в число, знаходить в таблиці число на
    яке треба замінити, замінене число перетворює в біти і повертає замінене число в бітах"""
    number = int(bits, 2)
    sub_number = s_table[1][number]
    sub_bits = format(sub_number, '04b')
    return sub_bits


def p_block(bit, p_table):
    s = ""
    k = 0
    m = 0
    for _ in bit:
        s += bit[(p_table[m][k]) - 1]
        if k == 3:
            m += 1
            k = 0
        else:
            k += 1
    return s


def sp_encode(bit, s_table, p_table):
    k = 0
    s_number = 0
    while k < 3:
        bit_s_transform = (s_block(bit[0:4], s_table[s_number]) +
                           s_block(bit[4:8], s_table[s_number+1]) +
                           s_block(bit[8:12], s_table[s_number+2]) +
                           s_block(bit[12:16], s_table[s_number+3]))

        bit_p_transform = p_block(bit_s_transform, p_table[k])
        s_number += 4
        k += 1
        bit = bit_p_transform
    return bit


def reverse_s_table(table):
    zipl = list(zip(table[1], table[0]))
    zipl.sort()
    revers_table = [[], []]
    for i in zipl:
        revers_table[0].append(i[0])
        revers_table[1].append(i[1])
    return revers_table


def p_decode(bit, p_table):
    revers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    k = 0
    m = 0
    for i in bit:
        revers_index = p_table[m][k] - 1
        revers[revers_index] = i
        if k == 3:
            m += 1
            k = 0
        else:
            k += 1

    revers_bit = ""
    for i in revers:
        revers_bit += i
    return revers_bit


def sp_decode(bit, s_table, p_table):
    k = -1
    s_number = -1
    while k > -4:
        bit = p_decode(bit, p_table[k])
        bit_s_transform = (s_block(bit[0:4], reverse_s_table(s_table[s_number-3])) +
                           s_block(bit[4:8], reverse_s_table(s_table[s_number-2])) +
                           s_block(bit[8:12], reverse_s_table(s_table[s_number-1])) +
                           s_block(bit[12:16], reverse_s_table(s_table[s_number])))
        s_number -= 4
        k -= 1
        bit = bit_s_transform
    return bit
