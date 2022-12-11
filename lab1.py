
import doctest

class Cake:
    def __init__(self, weight: float, shape: str):
        """
        Создание и подготовка к работе объекта "Cake"
 
        :param weight: Вес
        :param shape: Форма
 
        Примеры:
        >>> tasty_cake = Cake(2.05,'round')  # инициализация экземпляра класса
        """
        if weight < 0:
            raise ValueError("Вес не может быть меньше 0")
        self.weigt = weight
        self.shape = shape
 
    def cut_cake(self, pieces: int) -> None:
        """
        Разрезание торта.
        :param pieces: Число кусков
 
        :raise ValueError: Если число кусков меньше 2, выдаем ошибку.
 
        Примеры:
        >>> tasty_cake = Cake(2.05,'round')
        >>> tasty_cake.cut_cake()
        """
        if pieces < 2:
            raise ValueError("Нельзя разрезать меньше чем на 2 куска")
        ...
 
    def eat_cake(self) -> None:
        """
        Съесть.
 
        Примеры:
        >>> tasty_cake = Cake(2.05,'round')
        >>> tasty_cake.eat_cake()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

class Cat:
    def __init__(self, breed: str, name: str):
        self.breed = breed
        self.name = name
        """
        Создание и подготовка к работе объекта "Кот"
        :param breed: Порода кота
        :param name: Кличка кота
        Примеры:
        >>> cat = Cat("british", "Tom")  # инициализация экземпляра класса
        """

    def pet_cat(self):
        """
        Функция которая проверяет можно ли разрезать торт
        :return: да или нет
        Примеры:
        >>> cake = cake(1, round)
        >>> cake.is_cut()
        """

    def def play_cat(self):
        """
        Функция которая проверяет можно ли съесть торт
        :return: да или нет
        Примеры:
        >>> cake = cake(1, round)
        >>> cake.is_eat()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class IceCream
    def __init__(self, taste, sort):
        self.taste = taste
        self.sort = sort
        """
        Создание и подготовка к работе объекта "Мороженное"
        :param breed: Порода кота
        :param name: Кличка кота
        Примеры:
        >>> cat = Cat("british", "Tom")  # инициализация экземпляра класса
        """

    def sell_icecream(self):
        """
        Функция которая проверяет можно ли разрезать торт
        :return: да или нет
        Примеры:
        >>> cake = cake(1, round)
        >>> cake.is_cut()
        """

    def buy_icecream(self):
        """
        Функция которая проверяет можно ли съесть торт
        :return: да или нет
        Примеры:
        >>> cake = cake(1, round)
        >>> cake.is_eat()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
