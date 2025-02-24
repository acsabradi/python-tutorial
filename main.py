remainder = 11%3
number = 11 - remainder
number /= 3
exponent = 3**2
number2 = (1 + 2) * 3
text = "Attila"
very_big_number = 28282822828
some_variable = "abcd"

# itt kiprinteljük az eredményt
print(f"The integer result is: {number}")
print(f"The remainder is: {remainder}")
print(exponent)
print(number2)
#print(some_variable2)

#variable_from_user = input("Kérlek adj meg egy egész számot: ")
#print(f"Ezt a számot adtad meg: {variable_from_user}")

# kérd be egy téglalap két oldalának hosszát, és printeld ki annak kerületét és területét

# side_a = int(input("kerlek add meg az a oldalt: "))
# side_b = int(input("kerlek add meg a b oldalt: "))
# perimeter = (side_a + side_b) * 2
# area = side_a * side_b
# print(f"perimeter: {perimeter},area: {area}")

# kamatos kamat: bekérünk 3 integert, a tőkét, a kamatot és a futamidőt
# printeld ki a futamidő végén kapott kamatos kamat összegét

# toke = int(input("kerlek add meg a toket: "))
# kamat = int(input("kerlek add meg a kamatot: "))
# futamido = int(input("kerlek add meg a futamidot: "))
#
# eredmeny = int(toke*(1+kamat/100)**futamido)
# print(f"eredmeny:{eredmeny}")

float_number = 12.9
print(f"12.9 converted to int: {int(float_number)}")

bool_variable = True

print(not 1 == 1)
print(1 == 1 and 1 == 0)
print(1 == 1 or 1 == 0)
print(True * 8)
print(False - 5)
print(True + True)
print(2 > True)
# print(1 == 2)
# print(1 != 2)
# print(1 < 10)
# print(1 <= 10)
# print(1 >= 10)

# vizsgalando_szam = int(input("add meg a vizsgalando szamot: "))
# pozitiv_szam = vizsgalando_szam >= 0
# paros_szam = (vizsgalando_szam % 2) == 0
# print(f"kapott szam pozitiv-e:{pozitiv_szam}" )
# print(f"paros_szam-e: {paros_szam}")

# A_szam = int(input("A_szam: "))
# B_szam = int(input("B_szam: "))
# vizsgalat = (A_szam % B_szam) == 0
# print (f"vizsgalat eredmenye:{vizsgalat}")

str_var = "abcdef"
print(str_var)
print(f"{str_var} ------- defgh")

# str_var += "ghijkl"
print(str_var)
print(len(str_var))
print(str_var[11])
# print(str_var[12]) -> IndexError
print(str_var[len(str_var)])