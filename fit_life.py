# Проект FitLife - MVP версия 1.0
print('Привет, спортсмен!')  # Приветствие
while True:
    user_name = input('Как я могу к тебе обращаться?')  # Имя
    user_name = user_name.strip()
    if user_name:
        break
    print('Имя пустое, введи другое')
while True:
    user_age = int(input('Сколько тебе лет?'))  # возраст
    if 1 <= user_age <= 120:
        break
    print('Возраст не подходит, введи реальный возраст!')
while True:
    user_weight = float(input('Назови свой вес:'))  # Вес
    if 20 <= user_weight <= 200:
        break
    print('Вес не подходит, введи реальный вес!')
while True:
    user_height = float(input('Укажи свой рост в метрах. Пример: 1.9'))
    if 1 <= user_height <= 2.2:
        break
    print('Рост не подходит, введи реальный свой рост в метрах!')
bmi = user_weight / (user_height ** 2)  # Расчет индекса массы тела
bmi_round = round(bmi, 1)  # Округление ИМТ до десятых
water_ml = user_weight * 30  # Норма воды в день в мл
water_l = water_ml / 1000  # Перевод воды в литры
if user_age % 100 in (11, 12, 13, 14):
    age_word = 'лет'
elif user_age % 10 == 1:
    age_word = 'год'
elif user_age % 10 in (2, 3, 4):
    age_word = 'года'
else:
    age_word = 'лет'
print(f"Отчет для пользователя: {user_name} ({user_age} {age_word})")
print(f"Твой Индекс Массы Тела: {bmi_round}")
print(f"Рекомендуемая норма воды: {water_l} л в день")
print('')  # Пустая строка чтобы выглядело как в примере
print('Расчет окончен. Будьте здоровы!')
