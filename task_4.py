# Напиши класс EmployeeSalary. Он рассчитывает почасовую заработную плату сотрудников за неделю.
# С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
# Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
# Добавь метод класса get_hours(). 
# Если значение hours неизвестно, метод рассчитывает часы, исходя из количества выходных — rest_days. 
# Формула для этого случая такая: (7 - rest_days) * 8.
# Добавь метод класса get_email(). 
# Если значение email неизвестно, метод генерирует его так: f"{name}@email.com".
# Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
# Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.
# У тебя будет три класс-метода. Не забудь, что им всем нужно передать cls в качестве первого аргумента.
# Метод get_hours() должен вернуть cls: return cls(name, hours, rest_days, email). Метод get_email — аналогично. 
# Методу set_hourly_payment() ничего возвращать не нужно, потому что он только меняет значение переменной.


class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f'{name}@email.com'
        else:
            return cls(name, hours, rest_days, email)
        
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
        
    def salary(self):
        if self.hours is None:
            raise ValueError("Количество часов не указано")
        return self.hours * self.hourly_payment
    