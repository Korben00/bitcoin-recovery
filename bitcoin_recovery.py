import os as A, sys as B, time as C, pyfiglet as D, musicalbeeps as E2, math as G2, hashlib as I2, base64 as J, colorama as K
L2, M2, N2 = K.Fore, K.Style, K.Back
O, P = A.devnull, B.stdout
B.stdout = open(O, 'w')
import pygame as F
F.init()
B.stdout = P
from bitcoin import is_address
from pycoin.networks.registry import network_for_netcode


def Z(a): return [I2.sha256(A.urandom(1024)).hexdigest() for _ in range(a)]
def j(sequence, duration):
    player = E2.Player(volume=0.3, mute_output=True)
    notes = sequence.split(" ")
    for note in notes:
        player.play_note(note, duration)

def o(n): return n.decode("utf-8")
def p(q): return q.encode("utf-8")

R = network_for_netcode("BTC")
S = D.figlet_format("Bitcoin Recovery")
print("--------------------------------------------------------------------------------------------------------------------")
print(L2.YELLOW + S + M2.RESET_ALL)
print("--------------------------------------------------------------------------------------------------------------------")

print()
print('Welcome to Bitcoin Recovery!')
print('With this tool, you can recover your Bitcoin private key just from the public key.')
print()
B = input('Please enter your Bitcoin public key: ')
while True:
    if is_address(B):
        print("This is a valid address.")
        break
    else:
        print('Invalid public key, please try again.')
        B = input('Please enter your Bitcoin public key: ')

print('Please wait...')
print()
G = 8
for i in range(G, -1, -1):
    D = i // 60
    E = i % 60
    F = f"{D:02d}:{E:02d}"
    H = f"Generating your private key in progress... : "
    I = 50
    K = ((G - i) / G) * I
    L = "[" + "#" * G2.ceil(K) + "-" * (I - G2.ceil(K)) + "]"
    print(f"{H}" + L2.YELLOW + f"{L}", end="\r" + M2.RESET_ALL)
    Z(G * 100000)
    C.sleep(0.5)

for u in range(1, 6):
    M = A.urandom(16)
    N = R.keys.bip32_seed(M)
    O = N.hwif(as_private=1)
    print('Key ' + str(u) + ': ' + L2.GREEN + '{}'.format(O) + M2.RESET_ALL)
    C.sleep(1.5)

key_6_text_base64 = "S2V5IDY6"
key_6_text_decoded = J.b64decode(key_6_text_base64).decode("utf-8")
key_6_base64 = "eHBydjlzMjFaclFIMTQzS0FQUklMRk9PTERBWVBPSVNTT05EQVZSSUxBSEFIQUFQUklMRk9PTERBWVBPSVNTT05EQVZSSUxBUFJJTEZPT0xEQVlQT0lTU09OREFWUklMQVBJTEZPT0xEQVkhISE="
key_6_decoded = J.b64decode(key_6_base64).decode("utf-8")
print(key_6_text_decoded + " " + L2.GREEN + key_6_decoded + M2.RESET_ALL)
print()
input(L2.RED + "Press ENTER to safely exit this program..." + M2.RESET_ALL)
print()

v = "A3 B3 D4 B3 F4# F4# E4 A3 B3 D4 B3 E4 E4 D4 C4# B3 A3 B3 D4 B3 D4 E4 C4# A3 A3 E4 D4 A3 B3 D4 B3 F4# F4# E4 A3 B3 D4 B3 A4 C4# D4 C4# B3 A3 B3 D4 B3 D4 E4 C4# A3 A3 E4 D4"
w = "      /`·.¸\n     /¸...¸`:·\n ¸.·´  ¸   `·.¸.·´)\n: © ):´;      ¸  {\n `·.¸ `·  ¸.·´\`·¸)\n     `\\\\´´\¸.·´"
x = o(J.b64decode(p("VGhhbmsgeW91IGZvciB1c2luZyB0aGlzIGNvbXBsZXRlbHkgZmFrZSBCaXRjb2luIHByaXZhdGUga2V5IGdlbmVyYXRvciBtYWRlIGVzcGVjaWFsbHkgZm9yIEFwcmlsIEZvb2wncyBEYXkhCgpKb2luIG1lIGF0IGh0dHBzOi8va29yYmVuLmluZm8vCg==")))
print(L2.YELLOW + w + M2.RESET_ALL)
print()
print(x)
duration = 0.3
j(v, duration)
