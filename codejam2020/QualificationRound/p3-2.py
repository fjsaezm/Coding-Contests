
n = int(input())

for i in range(n):
    n_act = int(input())
    acts = [ input().split(" ") for i in range(n_act)]
    acts = [ list(map(int,row)) for row in acts]
    copy = acts.copy()
    acts.sort(key = lambda x: x[0])
    
    c_busy_til = 0
    j_busy_til = 0
    output = ""
    for a in acts:
        if c_busy_til <= a[0]:
            c_busy_til = int(a[1])
            output += 'C'
        else:
            if j_busy_til <= a[0]:
                j_busy_til = int(a[1])
                output += 'J'
            else:
                output = "IMPOSSIBLE"
                break

    final_output = [ " " for i in range(n_act)]
    if output != "IMPOSSIBLE":
        for it,act in enumerate(copy):
            idx = acts.index(act)
            final_output[it] = output[idx]
            acts[idx] = [0,0]
            
        final_output = ''.join(final_output)
    else:
        final_output = output
    
    print("Case #"+str(i+1)+": "+str(final_output))
