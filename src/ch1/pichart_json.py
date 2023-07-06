import json
import matplotlib.pyplot as plt
from japanize_matplotlib import japanize

# 日本語フォントの設定
japanize()

data = json.load(open('pi.json', encoding='utf-8'))

values = [i[0] for i in data]
labels = [i[1] for i in data]

plt.pie(values, labels=labels)
plt.show()
