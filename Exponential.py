import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych
x = np.linspace(0, 10, 100)
y = np.exp(x)

# Regresja liniowa
slope, intercept = np.polyfit(x, y, 1)

# Predykcja
y_pred = slope * x + intercept

# Obliczenie R²
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot

print(f"Równanie regresji: y = {slope:.2f}x + {intercept:.2f}")
print(f"Współczynnik determinacji R²: {r2:.3f}")

# Wykres
plt.scatter(x, y, label='Dane rzeczywiste')
plt.plot(x, y_pred, color='red', label='Linia regresji')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresja liniowa funkcji wykładniczej')
plt.legend()
plt.grid(True)
plt.show()

