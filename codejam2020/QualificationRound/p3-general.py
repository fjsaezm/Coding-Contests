
n = int(input())

for i in range(n):
    n_act = int(input())
    acts = [ input().split(" ") for i in range(n_act)]
    acts = [ list(map(int,row)) for row in acts]
    copy = acts.copy()
    acts = sorted(acts,key=lambda tup : tup[0])
    # Vector to manage occupation
    free = ['C','J']
    busy = []
    output = ""
    for act in acts:
        if output == "IMPOSSIBLE":
            break
        #Check if they're still busy and free
        if len(busy) > 0:
            for a in busy:
                if a[1] <= act[0]:
                    free.append(a[0])
                    busy.remove(a)
 
        if len(free) > 0:
            # Add person to busy and when it ends
            busy.append([free[0],act[1]])
            # Add to output
            output += busy[-1][0]
            # Not free
            free.remove(free[0])
        else:
            output = "IMPOSSIBLE"
            break

    final_output = ""
    if output != "IMPOSSIBLE":
        for act in copy:
            idx = acts.index(act)
            final_output += output[idx]
    else:
        final_output = output

    print("Case #"+str(i+1)+": "+final_output)
