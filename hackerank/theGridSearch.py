# the Grid Search
def gridSearch(G, P):
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])

    for i in range(R-r+1):
        for j in range(C-c+1):
            if G[i][j] == P[0][0]:
                equal = True
                for m in range(r):
                    for n in range(c):
                        if G[i+m][j+n] != P[m][n]:
                            equal = False
                            break
                    if not equal:
                        break
                if equal:
                    return "YES"
    return "NO"
