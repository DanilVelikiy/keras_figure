import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    W11 = [0.3, 0.3, 0]
    W12 = [0.4, -0.5, 1]
    weght1 = np.array([W11, W12])
    weght2 = np.array([-1, 1])

    sum_hidden = np.dot(weght1, x)
    print(f'Значения сумм на выходах скрытого слоя: {sum_hidden}')

    out_hidden = np.array([act(x) for x in sum_hidden])
    print(f'Значения на выходах нейронов скрытого слоя: {out_hidden}')

    sum_end = np.dot(weght2, out_hidden)

    y = act(sum_end)
    print(f'Выходное знаениче НС: {y}')

    return y

house = 1
rock = 0
attr = 0

res = go(house, rock, attr)

if res == 1:
    print('Ты мне нравишься')
else:
    print('Созвонимся')