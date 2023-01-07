

import doctest


class House:
    def __int__(self, capacity: int, free_space: int):
        """
        Объект Дом: создание и подготовка к работе
        :param capacity: Вместительность дома
        :param free_space: Свободное место в доме
        """

        if not isinstance(capacity, int):
            raise TypeError("Вместимость должна идти в формате int")
        if capacity < 0:
            raise ValueError("Вместимость не должна быть отрицательной")
        self.capacity = capacity

        if not isinstance(free_space, int):
            raise TypeError("Свободное место должно идти в формате int")
        if free_space < 0:
            raise ValueError("Свободное место не может быть отрицательным")
        self.free_space = free_space

    def is_room_empty(self) -> bool:
        """
        Проверка, есть ли в доме люди.
        :return: Есть ли в доме люди
        """
    def invite_someone(self, person: float) -> None:
        """
        "Добавление" людей в дом.
        :param person: Вошедшие люди
        :raise ValueError: ошибка, если людей больше вместимости дома
        """

    def expel_someone(self, person_expelled: float) -> None:
        """
        Удаление людей из дома.
        :param person_expelled: количество человек, которые были уделены из дома
        :raise ValueError: ошибка, если пытаются удалить больше людей, чем есть в доме
        :return: Сколько людей удалены
        """


class City:
    def __init__(self, population, area):
        """
        Объект Город: создание и подготовка к работе
        :param population: население города
        :param area: площадь города (в квадратных километрах)
        Примеры:
        >>> moscow = City(11920000, 2511) # PEP8 здесь противоречит тому, что города пишутся с большой буквы
        """
        if not isinstance(population, int):
            raise TypeError("Population должна быть int")
        if population <= 0:
            raise ValueError("Population должна быть положительным числом")
        if not isinstance(area, (int, float)):
            raise TypeError("Area должна быть float или int!")
        if area <= 0:
            raise ValueError("Area должна быть положительным числом")

    def population_census(self):
        """
        Метод проводит перепись населения
        :return: возвращает новое число населения
        Примеры:
        >>> moscow = City(11920000, 2511)
        >>> moscow.population_census()
        """
        ...

    def city_expand(self, additional_area):
        """
        Метод увеличивает площадь города на additional_area
        :param additional_area: дополнительная площадь города
        :raise TypeError: вызывает ошибку, если тип additional_area не int и не float
        :return: возвращает новую площадь города
        Примеры:
        >>> moscow = City(11920000, 2511)
        >>> moscow.city_expand(10)
        """
        ...
class User(object):
    """
    Объект пользователь: создание и подготовка к работе
    :param username: имя пользователя, str
    :param age: возраст, int
    :param country: страна пользователя, str
    """
    def __init__(self, username: str, age: int, country: str):
        """Валидация атрибутов объекта Транспортное средство"""
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно содержать только буквы")
        if len(username) < 2:
            raise ValueError("Имя пользователя должно состоять не более 2 букв.")
        self.username = username

        if not isinstance(age, int):
            raise TypeError("Укажите возраст пользователя в целочисленном формате.")
        if age <= 0:
            raise ValueError("Возраст пользователя не может быть менее года.")
        self.age = age

        if not isinstance(country, str):
            raise TypeError("Укажите корректное название страны в формате string.")
        self.country = country

    def create_account(self) -> dict:
        """Создание аккунта пользователя"""
        pass

    def account_info(self) -> str:
        """Возвращает информацию экземпляра пользователя"""
        return f"The user is {self.username}, {self.age} y.o., from {self.country}"

    def delete_account(self):
        """Удаление существующего аккаунта"""
        pass

    @staticmethod
    def calculate_age(year: int, month: int, day: int) -> int:
        """
        Подсчет текущего возраста
        :param year: год в дате рождения, int
        :param month: месяц в дате рождения, int
        :param day: день в дате рождения, int
        """

if __name__ == "__main__":
    doctest.testmod()
