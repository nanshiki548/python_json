import json, japanize_matplotlib
import matplotlib.pyplot as plt

data = json.load(open('pop.json', encoding='utf-8'))

#複数の線グラフを描画するようにデータを分割
x, totals, man, woman = [], [], [], []
for row in data:
    x.append(row['year'])
    totals.append(row['total'])
    man.append(row['man'])
    woman.append(row['woman'])

p_total = plt.plot(x, totals, label='合計(千人)')
p_woman = plt.plot(x, woman, label='女')
p_man = plt.plot(x, man, label='男')
plt.legend() #凡例を表示
plt.show()