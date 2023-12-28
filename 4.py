import numpy as np
import matplotlib.pyplot as plt

#mendefinisikan variabel
a = 50
panjang = 500
waktu = 0
node = 500


dx = panjang / node
dy = panjang /node
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes = int(waktu / dt)
u = np.zeros((node, node)) + 20

#kondisi batas
u[0, :] = np.linspace(0, 100, node)
u[-1, :] = np.linspace(100, 0, node)
u[:, 0] = np.linspace(0, 100, node)
u[:, -1] = np.linspace(0, 100, node)

#visualisasi distribusi suhu awal
fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)

counter = 0
while counter < waktu:
    w = u.copy()
    #Looping setiap titik grid kecuali batas
    for i in range(1, node-1):
        for j in range(1, node-1):
            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    pcm.set_array(u)
    t_mean = np.mean(u)
    counter += dt
    print(f"t: {counter:.3f} s, Suhu rata-rata: {t_mean:.2f} Celcius")
    ax.set_title(f"Distribusi Suhu t: {counter:.3f} s, Suhu rata-rata={t_mean:.2f}")
    plt.pause(0.01)

plt.show()
