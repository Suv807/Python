def switch(a):
    match a:
        case 1:
            if a > 90:
                return "A"

        case 2:
            if (a > 70) and (a < 89):
                return "B"

        case 3:
            if (a > 69) and (a < 50):
                return "C"
        case 4:
            if a > 49:
                return "fail"


c = int(input("Marks obtain by a student is"))
b = switch(c)
