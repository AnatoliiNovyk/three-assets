import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Створюємо DataFrame із даними
data = {
    'Month': [1, 2, 3, 4, 5, 6],
    'A': [25, -10, 10, 5, 35, 13],
    'B': [0, 15, -5, 5, 20, 25],
    'C': [10, 25, -15, -5, -5, 15]
}
df = pd.DataFrame(data)
print("Таблиця даних:")
print(df)

# 2. Побудова графіків регресії
plt.figure(figsize=(15, 5))

# A vs B
plt.subplot(1, 3, 1)
sns.regplot(x='A', y='B', data=df, color='blue')
plt.title('A vs B')
plt.xlabel('Прибутковість A (%)')
plt.ylabel('Прибутковість B (%)')

# A vs C
plt.subplot(1, 3, 2)
sns.regplot(x='A', y='C', data=df, color='green')
plt.title('A vs C')
plt.xlabel('Прибутковість A (%)')
plt.ylabel('Прибутковість C (%)')

# B vs C
plt.subplot(1, 3, 3)
sns.regplot(x='B', y='C', data=df, color='red')
plt.title('B vs C')
plt.xlabel('Прибутковість B (%)')
plt.ylabel('Прибутковість C (%)')

plt.tight_layout()
plt.show()

# 3. Обчислюємо кореляцію
correlation_AB = df['A'].corr(df['B'])
correlation_AC = df['A'].corr(df['C'])
correlation_BC = df['B'].corr(df['C'])

print(f"Кореляція між A і B: {correlation_AB:.3f}")
print(f"Кореляція між A і C: {correlation_AC:.3f}")
print(f"Кореляція між B і C: {correlation_BC:.3f}")

# 4. Висновки
print("\nВисновок:")
min_corr = min(abs(correlation_AB), abs(correlation_AC), abs(correlation_BC))
if min_corr == abs(correlation_AB):
    print("Пара акцій A і B має найменшу залежність у прибутковості.")
elif min_corr == abs(correlation_AC):
    print("Пара акцій A і C має найменшу залежність у прибутковості.")
else:
    print("Пара акцій B і C має найменшу залежність у прибутковості.")
