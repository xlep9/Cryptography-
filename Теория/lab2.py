SBOX = [
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16
]

INV_SBOX = [0] * 256

# добавим значения в обратную таблицу SBOX
for x in range(256): #x - исходный байт
    y = SBOX[x]      #y - байт после подстановки по таблице SBOX
    INV_SBOX[y] = x


def shift_rows(state):
    row1 = [state[1], state[5], state[9], state[13]]
    row1 = [row1[1], row1[2], row1[3], row1[0]]
    state[1], state[5], state[9], state[13] = row1

    row2 = [state[2], state[6], state[10], state[14]]
    row2 = [row2[2], row2[3], row2[0], row2[1]]
    state[2], state[6], state[10], state[14] = row2

    row3 = [state[3], state[7], state[11], state[15]]
    row3 = [row3[3], row3[0], row3[1], row3[2]]
    state[3], state[7], state[11], state[15] = row3


def inv_shift_rows(state):
    row1 = [state[1], state[5], state[9], state[13]]
    row1 = [row1[3], row1[0], row1[1], row1[2]]
    state[1], state[5], state[9], state[13] = row1

    row2 = [state[2], state[6], state[10], state[14]]
    row2 = [row2[2], row2[3], row2[0], row2[1]]
    state[2], state[6], state[10], state[14] = row2

    row3 = [state[3], state[7], state[11], state[15]]
    row3 = [row3[1], row3[2], row3[3], row3[0]]
    state[3], state[7], state[11], state[15] = row3


def mul_by_2(a):
    high_bit = a & 0x80    # 0x80 = 10000000
    a = (a << 1) & 0xFF   # 0xFF = 11111111
    if high_bit:
        a = a^0x1B      # 0x1B = 00011011 (x^4+x^3+x^2+1)
    return a

def mul2(x):
    return mul_by_2(x)

def mul3(x):
    return mul2(x) ^ x

def mix_one_column(col):
    a0, a1, a2, a3 = col

    return [
        mul2(a0) ^ mul3(a1) ^ a2 ^ a3,
        a0 ^ mul2(a1) ^ mul3(a2) ^ a3,
        a0 ^ a1 ^ mul2(a2) ^ mul3(a3),
        mul3(a0) ^ a1 ^ a2 ^ mul2(a3)
    ]

def mix_columns(state):
    for c in range(4):
        col = [state[4*c], state[4*c+1], state[4*c+2], state[4*c+3]]
        new_col = mix_one_column(col)

        state[4*c]   = new_col[0]
        state[4*c+1] = new_col[1]
        state[4*c+2] = new_col[2]
        state[4*c+3] = new_col[3]

def mul4(x):
    return mul2(mul2(x))

def mul8(x):
    return mul2(mul4(x))

def mul9(x):
    return mul8(x) ^ x

def mul11(x):
    return mul8(x) ^ mul2(x) ^ x 

def mul13(x):
    return mul8(x) ^ mul4(x) ^ x

def mul14(x):
    return mul8(x) ^ mul4(x) ^ mul2(x)


def inv_mix_one_column(col):
    a0, a1, a2, a3 = col
    return [
        mul14(a0) ^ mul11(a1) ^ mul13(a2) ^ mul9(a3),
        mul9(a0)  ^ mul14(a1) ^ mul11(a2) ^ mul13(a3),
        mul13(a0) ^ mul9(a1)  ^ mul14(a2) ^ mul11(a3),
        mul11(a0) ^ mul13(a1) ^ mul9(a2)  ^ mul14(a3)
    ]

def inv_mix_columns(state):
    for c in range(4):
        col = [state[4*c], state[4*c+1], state[4*c+2], state[4*c+3]]
        new_col = inv_mix_one_column(col)
        state[4*c]   = new_col[0]
        state[4*c+1] = new_col[1]
        state[4*c+2] = new_col[2]
        state[4*c+3] = new_col[3]

def add_round_key(state, key):
    for i in range(16):
        state[i] = state[i] ^ key[i]

def sub_bytes(state):
    for i in range(16):
        state[i] = SBOX[state[i]]

def inv_sub_bytes(state):
    for i in range(16):
        state[i] = INV_SBOX[state[i]]

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def rot_word(word):
    first_byte = word[0]
    return word[1:] + [first_byte]

# Заменить 4 байта слова 4 новыми байтами в таблице SBOX.
def sub_word(word):
    new_word = []
    for byte in word:
        new_word.append(SBOX[byte])
    return new_word

def expand_key(key_bytes):
    # AES-128 использует ключ длиной 16 байт
    if len(key_bytes) != 16:
        raise ValueError("Key phải có đúng 16 byte")

    # Шаг 1: создаём список слов (word)
    # Каждое слово состоит из 4 байт
    words = []

    # Первые 4 слова берутся напрямую из исходного ключа
    first_word = [key_bytes[0], key_bytes[1], key_bytes[2], key_bytes[3]]
    second_word = [key_bytes[4], key_bytes[5], key_bytes[6], key_bytes[7]]
    third_word = [key_bytes[8], key_bytes[9], key_bytes[10], key_bytes[11]]
    fourth_word = [key_bytes[12], key_bytes[13], key_bytes[14], key_bytes[15]]

    words.append(first_word)   # w0
    words.append(second_word)  # w1
    words.append(third_word)   # w2
    words.append(fourth_word)  # w3

    # Шаг 2: генерируем слова от w4 до w43
    for i in range(4, 44):
        # Берём предыдущее слово
        previous_word = words[i - 1]

        # Создаём копию для обработки
        temp = [
            previous_word[0],
            previous_word[1],
            previous_word[2],
            previous_word[3]
        ]

        # Каждое 4-е слово обрабатывается особым образом
        if i % 4 == 0:
            # Циклический сдвиг влево на 1 байт
            temp = rot_word(temp)

            # Замена каждого байта через SBOX
            temp = sub_word(temp)

            # XOR первого байта с константой раунда
            rcon_value = RCON[(i // 4) - 1]
            temp[0] = temp[0] ^ rcon_value

        # Берём слово на 4 позиции назад
        word_4_before = words[i - 4]

        # Формируем новое слово через XOR по каждому байту
        new_b0 = word_4_before[0] ^ temp[0]
        new_b1 = word_4_before[1] ^ temp[1]
        new_b2 = word_4_before[2] ^ temp[2]
        new_b3 = word_4_before[3] ^ temp[3]

        new_word = [new_b0, new_b1, new_b2, new_b3]

        # Добавляем новое слово в список
        words.append(new_word)

    # Шаг 3: объединяем каждые 4 слова в один round key (16 байт)
    round_keys = []

    for r in range(11):
        round_key = []
        round_key += words[4*r]
        round_key += words[4*r + 1]
        round_key += words[4*r + 2]
        round_key += words[4*r + 3]
        round_keys.append(round_key)

    return round_keys

def encrypt_block(block, round_keys):
    # Шифрование одного блока 16 байт.
    state = list(block)

    add_round_key(state, round_keys[0])

    for rnd in range(1, 10):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, round_keys[rnd])

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, round_keys[10])

    return bytes(state)


def decrypt_block(block, round_keys):
    # Расшифровка одного блока 16 байт.
    state = list(block)

    add_round_key(state, round_keys[10])

    for rnd in range(9, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, round_keys[rnd])
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, round_keys[0])

    return bytes(state)


def encrypt_hex(plain_hex, key_hex):
    # Шифрование одного блока 16 байт в hex.
    key_bytes = bytes.fromhex(key_hex)
    plain_bytes = bytes.fromhex(plain_hex)

    if len(key_bytes) != 16 or len(plain_bytes) != 16:
        raise ValueError("Ключ и plaintext должны быть ровно 16 байт")

    round_keys = expand_key(key_bytes)
    return encrypt_block(plain_bytes, round_keys).hex()


def decrypt_hex(cipher_hex, key_hex):
    # Расшифровка одного блока 16 байт в hex.
    key_bytes = bytes.fromhex(key_hex)
    cipher_bytes = bytes.fromhex(cipher_hex)

    if len(key_bytes) != 16 or len(cipher_bytes) != 16:
        raise ValueError("Ключ и ciphertext должны быть ровно 16 байт")

    round_keys = expand_key(key_bytes)
    return decrypt_block(cipher_bytes, round_keys).hex()


print("AES-128")
print("1. Шифрование")
print("2. Расшифровка")

choice = input("Выберите: ")
key_hex = input("Введите ключ в hex (16 байт = 32 hex символа): ")

if choice == "1":
    plain_hex = input("Введите plaintext в hex: ")
    cipher_hex = encrypt_hex(plain_hex, key_hex)
    print("Ciphertext (hex):", cipher_hex)

elif choice == "2":
    cipher_hex = input("Введите ciphertext в hex: ")
    plain_hex = decrypt_hex(cipher_hex, key_hex)
    print("Plaintext (hex):", plain_hex)

else:
    print("Неверный выбор")
