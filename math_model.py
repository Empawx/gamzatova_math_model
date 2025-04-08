import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления показателей модели M/M/1
def mm1_model(lambda_rate, mu_rate):
    if lambda_rate >= mu_rate:
        raise ValueError("Интенсивность прихода λ должна быть меньше интенсивности обслуживания μ.")
    
    # Расчет показателей
    L = lambda_rate / (mu_rate - lambda_rate)  # Среднее количество клиентов в системе
    W = 1 / (mu_rate - lambda_rate)  # Среднее время ожидания в системе
    L_q = (lambda_rate ** 2) / (mu_rate * (mu_rate - lambda_rate))  # Среднее количество клиентов в очереди
    W_q = lambda_rate / (mu_rate * (mu_rate - lambda_rate))  # Среднее время ожидания в очереди
    
    return L, W, L_q, W_q

# Параметры модели
lambda_rate_values = np.linspace(0.1, 0.9, 100)  # Интенсивность прихода (λ)
mu_rate = 1.0  # Интенсивность обслуживания (μ)

# Массивы для хранения результатов
L_values = []
W_values = []
L_q_values = []
W_q_values = []

# Рассчитываем показатели для различных значений λ
for lambda_rate in lambda_rate_values:
    L, W, L_q, W_q = mm1_model(lambda_rate, mu_rate)
    L_values.append(L)
    W_values.append(W)
    L_q_values.append(L_q)
    W_q_values.append(W_q)

# Построение графиков
plt.figure(figsize=(12, 8))

# Среднее количество клиентов в системе (L)
plt.subplot(2, 2, 1)
plt.plot(lambda_rate_values, L_values, label="L (Среднее количество в системе)")
plt.xlabel('Интенсивность прихода (λ)')
plt.ylabel('Среднее количество клиентов (L)')
plt.title('L(λ) — Среднее количество клиентов в системе')
plt.grid(True)

# Среднее время ожидания в системе (W)
plt.subplot(2, 2, 2)
plt.plot(lambda_rate_values, W_values, label="W (Среднее время ожидания в системе)", color='orange')
plt.xlabel('Интенсивность прихода (λ)')
plt.ylabel('Среднее время ожидания (W)')
plt.title('W(λ) — Среднее время ожидания в системе')
plt.grid(True)

# Среднее количество клиентов в очереди (L_q)
plt.subplot(2, 2, 3)
plt.plot(lambda_rate_values, L_q_values, label="L_q (Среднее количество в очереди)", color='green')
plt.xlabel('Интенсивность прихода (λ)')
plt.ylabel('Среднее количество в очереди (L_q)')
plt.title('L_q(λ) — Среднее количество клиентов в очереди')
plt.grid(True)

# Среднее время ожидания в очереди (W_q)
plt.subplot(2, 2, 4)
plt.plot(lambda_rate_values, W_q_values, label="W_q (Среднее время ожидания в очереди)", color='red')
plt.xlabel('Интенсивность прихода (λ)')
plt.ylabel('Среднее время ожидания в очереди (W_q)')
plt.title('W_q(λ) — Среднее время ожидания в очереди')
plt.grid(True)

# Показать все графики
plt.tight_layout()
plt.show()