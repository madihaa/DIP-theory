import math
print("Input RGB Colors:")
H = int(input("H= "))
S = int(input("S= "))
I = int(input("I= "))

if (H >= 0 and H < 120):
    R = I * (1 + ((S * math.cos(H)) / math.cos(60 - H)))
    B = I * (1 - S)
    G = 1 - (R + B)
elif (H >= 120 and H < 240):
    H = H - 120
    R = I * (1 - S)
    G = I * (1 + (S * math.cos(H)) / math.cos(60 - H))
    B = 1 - (R + G)
elif (H >= 240 and H < 360):
    H = H - 240
    G = I * (1 - S)
    B = I * (1 - ((S * math.cos(H)) / math.cos(60 - H)))
    R = 1 - (G + B)
else:
    print("Wrong inputs")

print("R = ", R)
print("G = ", G)
print("B = ", B)