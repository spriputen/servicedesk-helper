# Что должен делать скрипт (минимум):

# спросить через input() время регистрации и время решения в часах, например 9 и 17;
# перевести ответы в число;
# посчитать время решения как разницу;
# сравнить с лимитом SLA, который задан переменной, например 8 часов;
# через if/else вывести «SLA соблюдён» или «SLA нарушен».

# Если захочется больше: обработайте случай, когда время решения меньше времени регистрации, - это ошибка ввода.

# Пока делайте именно в часах числом. Настоящие даты через datetime появятся в неделе 18, а класс Ticket с методом is_sla_breached() - в неделе 9, туда эта логика и переедет.

print("SLA Verification")

SLA_HOURS = 8
incident_start_time = int(input("Enter the incident start time (hours): "))
incident_end_time = int(input("Enter the incident end time (hours): "))
incident_duration = incident_end_time - incident_start_time
if incident_end_time < incident_start_time:
    print("The incident end time cannot be earlier than the incident start time!")
elif incident_duration > SLA_HOURS:
    print("Duration:", incident_duration, "h.", "The SLA was breached!")
else:
    print("Duration:", incident_duration, "h.", "The SLA was not breached")