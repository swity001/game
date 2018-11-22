import random
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
print ""
 
print W+"Create By  : Swity"
print B+"Permainan Batu Gunting Kertas"
print ""
print G+"Pilihan :"
print ""
print O+"1. Batu"
print W+"2. Gunting"
print R"3. Kertas"
 
def permainan():
    kamu = int(input("Masukan pilihanmu: "))
    kom = random.choice(["Batu", "Gunting", "Kertas"])
    if kamu == 1:
        print G+"Kamu     : Batu"
        print("Komputer :", kom)
        if kom == "Batu":
            print B+"\tDraw"
        if kom == "Gunting":
            print G+"\tLu menang"
        if kom == "Kertas":
            print R+"\tLu kalah"
    if kamu == 2:
        print W+"Kamu     : Gunting"
        print("Komputer :", kom)
        if kom == "Batu":
            print R+"\tKamu kalah"
        if kom == "Gunting":
            print B+"\tDraw"
        if kom == "Kertas":
            print G+"\tLu Menang"
    if kamu == 3:
        print W+"Kamu     : Kertas"
        print("Komputer :", kom)
        if kom == "Batu":
            print G+"\tLu menang"
        if kom == "Gunting":
            print R+"\tLu kalah"
        if kom == "Kertas":
            print B+"\tDraw"
    if kamu >= 4:
        print R+"Pilihanmu salah!!!"
       
permainan()
