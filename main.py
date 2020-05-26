import matplotlib.pyplot as plt

def Serie_Leibniz_pi(n):
    return ((-1)**n) / (2*n+1)

n_termini = []
a_n_termini = []
pi_termini = []

Somma_n = 0

for n in range(0, 30):
    a_n = Serie_Leibniz_pi(n)
    Somma_n += a_n
    pi_n = 4 * a_n

    n_termini.append(n)
    a_n_termini.append(a_n)
    pi_termini.append(pi_n)

plt.plot(n_termini, pi_termini)
plt.grid()
plt.title("Serie di Leibniz per π")
plt.xlabel("n")
plt.ylabel("π(n)")
plt.show()
