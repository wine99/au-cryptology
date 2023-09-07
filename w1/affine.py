cipher = '''
KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUP
KRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKP
BCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFF
ERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERK
IVKSCPICBRKIJPKABI
'''

cipher = cipher.replace('\n', '')

# calculate the frequency of each letter
freq = {}
for c in cipher:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# sort the letters by frequency
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

def decrypt(cipher: str):
    dec = lambda x: chr(11 * (x - 4) % 26 + ord('a'))

    cipher = cipher.lower()
    # turn str to list of int
    cipher = [ord(c) - ord('a') for c in cipher]

    plain = [dec(x) for x in cipher]

    return ''.join(plain)

print(decrypt(cipher,))