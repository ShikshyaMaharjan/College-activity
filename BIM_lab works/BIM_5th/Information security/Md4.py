
import struct

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff

def md4(msg):
    msg = bytearray(msg, 'utf-8')
    orig_len = (8 * len(msg)) & 0xffffffffffffffff

    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0)
    msg += struct.pack('<Q', orig_len)

    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    for i in range(0, len(msg), 64):
        X = list(struct.unpack('<16I', msg[i:i+64]))
        AA, BB, CC, DD = A, B, C, D

        # Round 1 (simplified)
        for j in range(16):
            k = j
            s = [3,7,11,19][j%4]
            f = (B & C) | (~B & D)
            A = left_rotate((A + f + X[k]) & 0xffffffff, s)
            A, B, C, D = D, A, B, C

        A = (A + AA) & 0xffffffff
        B = (B + BB) & 0xffffffff
        C = (C + CC) & 0xffffffff
        D = (D + DD) & 0xffffffff

    return ''.join(f'{x:02x}' for x in struct.pack('<4I', A,B,C,D))

text = input("Enter message: ")
print("MD4:", md4(text))