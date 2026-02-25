from datetime import datetime, timedelta

# Получаем текущую дату
current_date = datetime.now()

# Вычитаем 5 дней
five_days_ago = current_date - timedelta(days=5)

print("Сегодня:", current_date.strftime("%Y-%m-%d"))
print("5 дней назад:", five_days_ago.strftime("%Y-%m-%d"))
