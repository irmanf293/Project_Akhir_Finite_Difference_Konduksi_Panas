import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel
a = 50
panjang = 500
waktu = 1.5
node = 500

dx = panjang / node
dy = panjang / node
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes = int(waktu / dt)
u = np.zeros((node, node)) + 20

# Kondisi batas
u[0, :] = np.linspace(0, 100, node)
u[-1, :] = np.linspace(100, 0, node)
u[:, 0] = np.linspace(0, 100, node)
u[:, -1] = np.linspace(0, 100, node)

# Simpan suhu rata-rata pada setiap iterasi waktu
suhu_rata_rata = []

counter = 0
while counter < waktu:
    w = u.copy()
    # Looping setiap titik grid kecuali batas
    for i in range(1, node-1):
        for j in range(1, node-1):
            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    t_mean = np.mean(u)
    suhu_rata_rata.append(t_mean)

    counter += dt
    print(f"t: {counter:.3f} s, Suhu rata-rata: {t_mean:.2f}")

# Pastikan panjang array waktu dan suhu_rata_rata sama
panjang_minimal = min(len(np.arange(0, waktu, dt)), len(suhu_rata_rata))
waktu_array = np.arange(0, waktu, dt)[:panjang_minimal]

# Print lengths of arrays for debugging
print("Length of waktu_array:", len(waktu_array))
print("Length of suhu_rata_rata:", len(suhu_rata_rata))

# Plot hubungan suhu rata-rata terhadap waktu
plt.plot(waktu_array, suhu_rata_rata[:panjang_minimal])
plt.xlabel("Waktu (s)")
plt.ylabel("Suhu Rata-rata (Celcius)")
plt.title("Hubungan Suhu Rata-rata terhadap Waktu")
plt.show()
