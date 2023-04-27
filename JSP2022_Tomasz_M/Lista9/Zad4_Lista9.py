import numpy as np
import matplotlib.pyplot as plt

height = [1.39, 1.60, 2.50, 2.87, 4.64, 5.73, 12.21,12.91,16.26,16.36]
bars = ('PHP', 'ASM', 'SQL', 'JS', 'VB','C#', 'Java', 'C++','C','Python')
y_pos = np.arange(len(height))
plt.figure(figsize=(10,5))
plt.bar(y_pos, height, color = '#c44010')
plt.xticks(y_pos, bars)
plt.xlabel('Język programowania', fontsize=12, color='#323232')
plt.ylabel('Popularność w procentach', fontsize=12, color='#323232')
plt.title('Popularność języków programowania', fontsize=16, color='#323232')
plt.show();
