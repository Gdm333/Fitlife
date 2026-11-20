# Проект FitLife - MVP версия 1.0
print('Привет, спортсмен!')  # Приветствие
user_name = input('Как я могу к тебе обращаться?')  # Имя
user_age = int(input('Сколько тебе лет?'))  # возраст
user_weight = float(input('Назови свой вес:'))  # Вес
user_height = float(input('Укажи свой рост в метрах, через точку.Пример: 1.9'))
bmi = user_weight / (user_height ** 2)  # Расчет индекса массы тела
bmi_round = round(bmi, 1)  # Округление ИМТ до десятых
water_ml = user_weight * 30  # Норма воды в день в мл
water_l = water_ml / 1000  # Перевод воды в литры
print(f"Отчет для пользователя: {user_name} ( {user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi_round}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print('')  # Пустая строка чтобы выглядело как в примере
print('Расчет окончен. Будьте здоровы!')
