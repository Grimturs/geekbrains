# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

first_name = input('Введите Ваше имя: ')
last_name = input('Введите Вашу фамилию: ')
age = int(input('Введите Ваш возраст: '))
weight = int(input('Введите Ваш вес: '))
diagnosis = ''

profile = [first_name, last_name + ',', str(age) + ' год,', 'вес ' + str(weight), diagnosis]


def good():
    profile[4] = "- хорошее состояние"
    print(' '.join(profile))


def bad():
    profile[4] = "- следует заняться собой"
    print(' '.join(profile))


if age <= 30:
    if 50 <= weight <= 120:
        good()
    else:
        bad()
elif 30 < age < 40:
    if weight < 50 or weight >= 120:
        bad()
    else:
        good()
elif age >= 40:
    if weight < 50 or weight >= 120:
        profile[4] = "- следует обратится к врачу!"
        print(' '.join(profile))
    else:
        good()
