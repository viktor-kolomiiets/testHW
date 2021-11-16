# isso calculator

print ("isso calc")
n = int(input ("humans in group: "))
count = 0

def isso_calc(n):
    pc = int(input ("positive choise: "))
    nc = int(input ("negative choise: "))

    return (pc + nc)/(n - 1)

while True:
    ui = input (": ")
    if ui == "1":
        count = count + 1
        print ("{c}. {isso}".format(c = count, isso = isso_calc(n)))
    elif ui == "0":
        break
    else:
        print ("unknown command")
