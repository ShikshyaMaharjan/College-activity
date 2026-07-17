print("P\tQ\tR\tP∧Q\t(P∧Q)→R")

for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:
            pq = P and Q
            result = (not pq) or R

            print(P, "\t", Q, "\t", R, "\t", pq, "\t", result)