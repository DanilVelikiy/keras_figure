# импорт тензорфлоу с керасом
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense

# импорт других необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt

# в документации увидел интересную реализацию: перевода градусов Цельсия в градусы Фаренгейта.
c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])

# определю НС как состояющую из слоев следующих друг за другом
model = keras.Sequential()

# Добавим в эту модель слой нейронов, состоящий из одного нашего выходного нейрона, имеющий ровно один вход
# и линейную активационную функцию
model.add(Dense(units=1, input_shape=(1,), activation='linear'))
# Здесь units=1 означает один нейрон, а input_shape=(1,) – один вход. Конструктор Dense формирует полносвязный слой,
# то есть, все входы будут связаны со всеми нейронами данного слоя. В нашем простейшем случае – это связь
# и дополнительно, автоматически, для каждого нейрона добавляется смещение – bias.

# Теперь, когда структура НС определена, ее нужно скомпилировать, указав критерий качества и способ оптимизации
# алгоритма градиентного спуска. В рамках данной задачи мы выберем минимум среднего квадрата ошибки и оптимизацию
# по Adam:
# 0,1 – это шаг сходимости алгоритма обучения
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

# Для запуска обучения используется метод fit:
log = model.fit(c, f, epochs=500, verbose=False)

# Здесь передается обучающая выборка для входных и выходных значений, затем, число эпох, т.е. выборка будет пропущена
# через сеть 500 раз и на каждой итерации будут корректироваться весовые коэффициенты и вычисляться значение критерия
# качества. Последний параметр указывает не отображать в консоли текущую информацию при обучении сети.
# Мы ее выведем после, используя объект log:

plt.plot(log.history['loss'])
plt.grid(True)
plt.show()

# То есть, наш критерий качества уже на 400-й эпохе практически перестал уменьшаться.

# Хорошо, теперь было бы интересно узнать как работает сеть и какие весовые коэффициенты были найдены. Чтобы подать
# на вход произвольное значение, нужно воспользоваться методом predict:
print(model.predict([100]))

# Он возвратит выходное значение и мы его отобразим в консоли. А для отображения весовых коэффициентов,
# запишем метод get_weights:
print(model.get_weights())
