import matplotlib.pyplot as plt


data = {}
with open('GAT+2sides_head_tail.txt', 'r', encoding='utf-8') as f:
    data['BDRAN'] = {
        'head': [int(num) for num in f.readline().strip().split()],
        'tail': [int(num) for num in f.readline().strip().split()]
    }

with open('GAT+convauto_head_tail.txt', 'r', encoding='utf-8') as f:
    data['BDRAN+CA'] = {
        'head': [int(num) for num in f.readline().strip().split()],
        'tail': [int(num) for num in f.readline().strip().split()]
    }
print(data)

length = len(data['BDRAN']['head'])

plt.rcParams["font.sans-serif"] = [u"SimHei"]
plt.rcParams["axes.unicode_minus"] = False

width = 0.4

for i, key in enumerate(['head', 'tail']):
    plt.subplot(2, 1, i+1)
    plt.bar([x for x in range(length)], data['BDRAN'][key], width=width, label='BDRAN',color="red")
    for x, y in zip([x for x in range(length)], data['BDRAN'][key]):
        plt.text(x - width / 2, y, y)
    plt.bar([x + width for x in range(length)], data['BDRAN+CA'][key], width=width, label='BDRAN+CA',color=["green"])
    for x, y in zip([x + width for x in range(length)], data['BDRAN+CA'][key]):
        plt.text(x - width / 2, y, y)

    plt.legend()
    plt.xticks([x + width / 2 for x in range(length)], range(1, length + 1))
    plt.title(f'Performance of {key} entity prediction on WN18RR')
    plt.xlabel('Range of rank')
    plt.ylabel('Number of entities')
plt.tight_layout()
plt.show()
