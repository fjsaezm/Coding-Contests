n = int(input())

for k in range(n):
    cur_level = 0
    output = ""
    line = input()
    for c in line:
        level = int(c)
        if cur_level < level:
            dif = level - cur_level
            cur_level +=dif
            for i in range(dif):
                output += "("
        if cur_level > level:
            dif = cur_level - level
            cur_level -=dif
            for i in range(dif):
                output += ")"
        output += c


    for j in range(cur_level):
        output += ")"

    print("Case #" + str(k+1) + ": " + output)
