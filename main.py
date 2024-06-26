import matplotlib.pyplot as plt

'''
считываем данные с ТХТ файла
'''
file_name = 'g_keep.txt'
file_data = list()
with open(file_name, 'r') as file:
    for i in file:
        if i:
            file_data.append(i.strip())

'''создаем списки для работы с данными'''
date = list()
tabys_price = list()
bt_price = list()

for item in file_data:
    date.append(item[:10])
print(date)

for item in file_data:
    tabys_price.append(float(item[13:18]) * 1000 * 1.8) # умножил на 1000 и затем на 1,8, чтобы графики были близко друг к другу
print(tabys_price)

for item in file_data:
    bt_price.append(int(item[21:].replace('.', '')))
print(bt_price)


width = 0.4
x_list = list(range(0, 5))
plt.figure()
plt.title('prices')
plt.xticks(rotation=90)
plt.xlabel('date')
plt.ylabel('price $ USD')
plt.plot(date, tabys_price, label='tabys_price', marker='o')
plt.plot(date, bt_price, label='real_bt_price', marker='^')
plt.legend()
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.subplots_adjust(left=0.06, right=0.97, top=0.95, bottom=0.13)
plt.show()
