import pandas as pd
import random
# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем столбец 'whoAmI' в one-hot формат
one_hot_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединяем one-hot столбцы с исходным DataFrame
result = pd.concat([data, one_hot_data], axis=1)

# Выводим первые строки результата
result.head()
print(result)