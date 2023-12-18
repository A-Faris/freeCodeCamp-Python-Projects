def add_time(start, duration, day = ""):
    d = ""
    days = ["monday","tuesday","wednesday","thuresday","friday","saturday","sunday"]

    m = int(str(int(start.partition(":")[2].split()[0]) + int(duration.partition(":")[2])))
    h = int(start.partition(":")[0]) + int(duration.partition(":")[0])
    if m > 59:
        m -= 60
        h += 1
    if len(str(m)) == 1:
        m = "0" + str(m)

    n = int(h/24)
    h = h%24
    E = start.split()[1]
    
    if h > 11:
        h -= 12
        if h == 0:
            h = 12
        if E == "PM":
            E = "AM"
            n += 1
        else:
            E = "PM"

    if day != "":
        day = days[(days.index(day.lower()) + n)%7]
        day = ", " + day.capitalize()

    if n == 1:
        d = " (next day)"
    elif n > 1:
        d = " (" + str(n) + " days later)"

    new_time = str(h) + ":" + str(m) + " " + E + day + d
    return new_time