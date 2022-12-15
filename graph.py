class Graphe_m:
    """ """
    def __init__(self, n):
        self.n = n
        self.A = [[False] * n for _ in range(n)]
    def __repr__(self):
        C = ["\t".join([""]+[str(i) for i in range(self.n)])]
        for l in range(self.n):
            L = [str(l)]
            for c in range(self.n):
                if self.A[l][c]:
                    L.append("1")
                else:
                    L.append("")
            C.append("\t".join(L))
        return "\n".join(C)


g = Graphe_m(5)

print(g)