f_path = "D:/ЧНПУ_ППФ/4 Курс/freelance/"

def data_input():
    vik = input("vik: ")
    statj = input("stat': ")
    kurs = input("kurs: ")
    fakult = input("fakultet: ")
    p1 = input("1: ")
    p2 = input("2: ")
    p3 = input("3: ")
    p4 = input("4: ")
    p5 = input("5: ")
    p6 = input("6: ")
    p7 = input("7: ")
    p8 = input("8: ")
    p9 = input("9: ")
    p10 = input("10: ")
    p11 = input("11: ")
    p12 = input("12: ")
    p13 = input("13: ")
    p14 = input("14: ")
    p15 = input("15: ")
    p16 = input("16: ")
    p17 = input("17: ")
    p18 = input("18: ")
    p19 = input("19: ")
    p20 = input("20: ")
    p21 = input("21: ")
    p22 = input("22: ")
    p23 = input("23: ")
    p24 = input("24: ")
    p25 = input("25: ")
    p26 = input("26: ")
    p27 = input("27: ")
    p28 = input("28: ")
    p29 = input("29: ")
    p30 = input("30: ")
    p31 = input("31: ")
    p32 = input("32: ")
    p33 = input("33: ")
    p34 = input("34: ")
    p35 = input("35: ")
    p36 = input("36: ")
    intim_sex = int(p1) + int(p2) + int(p3)
    osob_ident = int(p4) + int(p5) + int(p6)
    gosp_pobut = ((int(p7) + int(p8) + int(p9)) + (int(p22) + int(p23) + int(p24)))/2
    batk_vykhov = ((int(p10) + int(p11) + int(p12)) + (int(p25) + int(p26) + int(p27)))/2
    sots_aktiv = ((int(p13) + int(p14) + int(p15)) + (int(p28) + int(p29) + int(p30)))/2
    emot_psyho = ((int(p16) + int(p17) + int(p18)) + (int(p31) + int(p32) + int(p33)))/2
    zovn_pryvab = ((int(p19) + int(p20) + int(p21)) + (int(p34) + int(p35) + int(p36)))/2
    with open(f_path + "vik.txt", "a") as fv:
        fv.write(vik+ "\n")
    with open(f_path + "statj.txt", "a") as fs:
        fs.write(statj+ "\n")
    with open(f_path + "kurs.txt", "a") as fk:
        fk.write(kurs+ "\n")
    with open(f_path + "fakultet.txt", "a") as ff:
        ff.write(fakult+ "\n")
    #--------------------
    with open(f_path + "intim_sex.txt", "a") as f1:
        f1.write(str(intim_sex)+ "\n")
    with open(f_path + "osob_ident.txt", "a") as f2:
        f2.write(str(osob_ident)+ "\n")
    with open(f_path + "gosp_pobut.txt", "a") as f3:
        f3.write(str(gosp_pobut)+ "\n")
    with open(f_path + "batk_vykhov.txt", "a") as f4:
        f4.write(str(batk_vykhov)+ "\n")
    with open(f_path + "sots_aktiv.txt", "a") as f5:
        f5.write(str(sots_aktiv)+ "\n")
    with open(f_path + "emot_psyho.txt", "a") as f6:
        f6.write(str(emot_psyho)+ "\n")
    with open(f_path + "zovn_pryvab.txt", "a") as f7:
        f7.write(str(zovn_pryvab)+ "\n")

while True:
    print("Консультаційне дослідження сімейних цінностей")
    print("enter a command: ")
    ui = input(": ")

    if ui == "s":
        data_input()
    elif ui == "help":
        print("commands: 's' to start, 'help', 'end'")
    elif ui == "end":
        break
    else:
        print("unknown command")
