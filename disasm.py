def if_mask(a, b):
    c = []
    for l in a:
        r = 0
        if len(l[0]) == len(b):
            for i in range(len(b)):
                if l[0][i] == b[i]:
                    r += 1
                    if r == len(l[0]) - l[2]:
                        c.append([r, l])
    for i in c:
        if i[1][1] == 'subi':
            return [i]
        if i[1][1] == 'ldi':
            return [i]
    c = sorted(c)
    return c
def symbols(m):
    a = '-'
    b = '-'
    al = 'PbqsdKrk'
    for i in m:
        if i in al:
            a = i
    for i in m:
        if i in al and a != i:
            b = i
    s = ''
    for i in al:
        if a == i:
            s += a
        if b == i:
            s += b
    return(s)
def res_sym(mask1, mask2):
    sym = symbols(mask1)
    k = []
    s = ''
    for i in sym:
        s = ''
        if i != '-':
            for j in range(len(mask1)):
                if mask1[j] == i:
                    s += str(mask2[j])
            k.append(i + s)
    return k

def full_res(_byt ,com, a, num):
    res = ''
    if com == []:
        return _byt
    else:
        f = 1
    if f:
      for i in res_sym(com[-1][-1][0], a):
        if com[-1][-1][1] == 'jmp' or com[-1][-1][1] == 'call':
            if i[1] == 1:
                i = i.replace('1', 'a')
                i = i.replace('0', '1')
                i = i.replace('a', '0')
                i = bin(int(i, 2) + 1)[2:]
                i = i[1:] + '0'
            else:
                i = i[1:] + '0'
            return(num + ':', com[-1][-1][1], hex(int(i, 2)))
        elif 'k' in i:
            f = '+'
            if i[1] == '1':
                i = i.replace('1', 'a')
                i = i.replace('0', '1')
                i = i.replace('a', '0')
                i = bin(int(i[1:], 2) + 1)[2:]
                i = i + '0'
                f = '-'
            else:
                i = i[1:] + '0'
            if com[-1][-1][1] == 'sts':
                res += str(int(i, 2)//2)
            else:
                return(num + ':', com[-1][-1][1], f + str(int(i, 2)), ';', hex(int(num[2:], 16) + int(f + str(int(i, 2))) + 2))
        else:
            if i[0] == 'd':
                if com[-1][-1][1] == 'ldi' or com[-1][-1][1] == 'subi' or com[-1][-1][1] == 'sbci' or com[-1][-1][1] == 'cpi':
                    d = 'r' + str(int(i[1:], 2) + 16)
                else:
                    d = 'r' + str(int(i[1:], 2))
                res += d
            if i[0] == 'P':
                P = hex(int(i[1:], 2))
                res += P
            if i[0] == 'r':
                r = 'r' + str(int(i[1:], 2))
                res += r
            if i[0] == 'b':
                b = str(int(i[1:], 2))
                res += b
            if i[0] == 'q':
                q = str(int(i[1:], 2))
                if com[-1][-1][0][-4] == '0':
                    q = 'Z+' + q
                else:
                    q = 'Y+'+ q
                res += q
            if i[0] == 's':
                return com
            if i[0] == 'K':
                K = hex(int(i[1:], 2))
                res += K
            res += ' '
      return(num + ':', com[-1][-1][1], res)
_inputs = ['']
while _inputs[-1] != ':00000001FF':
    _inputs.append(input())
_hex = []
for _input in _inputs:
    num = 9
    while num < len(_input) - 2:
        _hex.append(_input[num + 2] + _input[num + 3] + _input[num] + _input[num + 1])
        num += 4
st_num = 0
s = []
m = [['1001010kkkkk110kkkkkkkkkkkkkkkkk', 'jmp', 22], ['1001010kkkkk111kkkkkkkkkkkkkkkkk', 'call', 22], ['1001001rrrrr0000kkkkkkkkkkkkkkkk', 'sts', 21], ['1001000ddddd0000kkkkkkkkkkkkkkkk', 'lds', 21], ['1010KKKKddddKKKK', 'subi', 12], ['0101KKKKddddKKKK', 'subi', 12], ['0110KKKKddddKKKK', 'sbr', 12], ['0100KKKKddddKKKK', 'sbci', 12], ['1100kkkkkkkkkkkk', 'rjmp', 12], ['1101kkkkkkkkkkkk', 'rcall', 12], ['0110KKKKddddKKKK', 'ori', 12], ['1110KKKKddddKKKK', 'ldi', 12], ['0011KKKKddddKKKK', 'cpi', 12], ['0111KKKKddddKKKK', 'cbr', 12], ['0111KKKKddddKKKK', 'andi', 12], ['10q0qq1rrrrr1qqq', 'std', 11], ['10q0qq1rrrrr0qqq', 'std', 11], ['10111PPrrrrrPPPP', 'out', 11], ['10q0qq0ddddd1qqq', 'ldd', 11], ['10q0qq0ddddd0qqq', 'ldd', 11], ['10110PPdddddPPPP', 'in', 11], ['001000dddddddddd', 'tst', 10], ['000110rdddddrrrr', 'sub', 10], ['000010rdddddrrrr', 'sbc', 10], ['000111dddddddddd', 'rol', 10], ['001010rdddddrrrr', 'or', 10], ['001011rdddddrrrr', 'mov', 10], ['000011dddddddddd', 'lsl', 10], ['001001rdddddrrrr', 'eor', 10], ['000100rdddddrrrr', 'cpse', 10], ['000001rdddddrrrr', 'cpc', 10], ['000101rdddddrrrr', 'cp', 10], ['001001dddddddddd', 'clr', 10], ['111100kkkkkkksss', 'brbs', 10], ['111101kkkkkkksss', 'brbc', 10], ['001000rdddddrrrr', 'and', 10], ['000011rdddddrrrr', 'add', 10], ['000111rdddddrrrr', 'adc', 10], ['1111111rrrrrobbb', 'sbrs', 9], ['1111110rrrrrobbb', 'sbrc', 9], ['10010111KKddKKKK', 'sbiw', 8], ['10011011PPPPPbbb', 'sbis', 8], ['10011001PPPPPbbb', 'sbic', 8], ['10011010PPPPPbbb', 'sbi', 8], ['00000001ddddrrrr', 'movw', 8], ['10011000PPPPPbbb', 'cbi', 8], ['1111101bbbbb0bbb', 'bst', 8], ['1111100bbbbb0bbb', 'bld', 8], ['10010110KKddKKKK', 'adiw', 8], ['111100kkkkkkk011', 'brvs', 7], ['111101kkkkkkk011', 'brvc', 7], ['111100kkkkkkk110', 'brts', 7], ['111101kkkkkkk110', 'brtc', 7], ['111101kkkkkkk000', 'brsh', 7], ['111101kkkkkkk010', 'brpl', 7], ['111101kkkkkkk001', 'brne', 7], ['111100kkkkkkk010', 'brmi', 7], ['111100kkkkkkk100', 'brlt', 7], ['111100kkkkkkk000', 'brlo', 7], ['111100kkkkkkk111', 'brie', 7], ['111101kkkkkkk111', 'brid', 7], ['111100kkkkkkk101', 'brhs', 7], ['111101kkkkkkk101', 'brhc', 7], ['111101kkkkkkk100', 'brge', 7], ['111100kkkkkkk001', 'breq', 7], ['111100kkkkkkk000', 'brcs', 7], ['111101kkkkkkk000', 'brcc', 7], ['1001010ddddd0010', 'swap', 5], ['1001001rrrrr1110', 'st', 5], ['1001001rrrrr1101', 'st', 5], ['1001001rrrrr1100', 'st', 5], ['1001001rrrrr1010', 'st', 5], ['1001001rrrrr1001', 'st', 5], ['1001001rrrrr0010', 'st', 5], ['1001001rrrrr0001', 'st', 5], ['1000001rrrrr1000', 'st', 5], ['1000001rrrrr0000', 'st', 5], ['1001010ddddd0111', 'ror', 5], ['1001001rrrrr1111', 'push', 5], ['1001000ddddd1111', 'pop', 5], ['1001010ddddd0001', 'neg', 5], ['1001010ddddd0110', 'lsr', 5], ['1001000ddddd0101', 'lpm', 5], ['1001000ddddd0100', 'lpm', 5], ['1001000ddddd1110', 'ld', 5], ['1001000ddddd1101', 'ld', 5], ['1001000ddddd1100', 'ld', 5], ['1001000ddddd1010', 'ld', 5], ['1001000ddddd1001', 'ld', 5], ['1001000ddddd0010', 'ld', 5], ['1001000ddddd0001', 'ld', 5], ['1000000ddddd1000', 'ld', 5], ['1000000ddddd0000', 'ld', 5], ['1001010ddddd0011', 'inc', 5], ['1001010ddddd1010', 'dec', 5], ['1001010ddddd0000', 'com', 5], ['1001010ddddd0101', 'asr', 5], ['11101111dddd1111', 'ser', 4], ['100101000sss1000', 'bset', 3], ['100101001sss1000', 'bclr', 3], ['1001010110101000', 'wdr', 0], ['1001010111101000', 'spm', 0], ['1001010110001000', 'sleep', 0], ['1001010000011000', 'sez', 0], ['1001010000111000', 'sev', 0], ['1001010001101000', 'set', 0], ['1001010001001000', 'ses', 0], ['1001010000101000', 'sen', 0], ['1001010001111000', 'sei', 0], ['1001010001011000', 'seh', 0], ['1001010000001000', 'sec', 0], ['1001010100011000', 'reti', 0], ['1001010100001000', 'ret', 0], ['0000000000000000', 'nop', 0], ['1001010111001000', 'lpm', 0], ['1001010000001000', 'ijmp', 0], ['1001010100001000', 'icall', 0], ['1001010010011000', 'clz', 0], ['1001010010111000', 'clv', 0], ['1001010011101000', 'clt', 0], ['1001010011001000', 'cls', 0], ['1001010010101000', 'cln', 0], ['1001010011111000', 'cli', 0], ['1001010011011000', 'clh', 0], ['1001010010001000', 'clc', 0]]
i = 0
if 1 == 1:
    while i != len(_hex):
        _byt = ''
        a = bin(int(_hex[i], 16))[2:]
        a = (16 - len(a)) * '0' + a
        if i < len(_hex)-1:
            k = bin(int(_hex[i + 1], 16))[2:]
            k = (16 - len(k)) * '0' + k
        if if_mask(m, a + k):
            a += k
            _byt += _hex[i][2] + _hex[i][3] + _hex[i][0] + _hex[i][1]
            i += 1
        com = if_mask(m, a)
        _byt += _hex[i][2] + _hex[i][3] + _hex[i][0] + _hex[i][1]
        if full_res(_byt, com, a, hex(st_num)):
            print(*full_res(_byt, com, a, hex(st_num)))
        i += 1
        if len(hex(int(a, 2))[2:]) % 2 == 0:
            st_num += len(hex(int(a, 2))[2:])//2
        else:
            st_num += len(hex(int(a, 2))[2:]) // 2 + 1


