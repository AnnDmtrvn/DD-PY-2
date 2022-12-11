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
 
 
class Сat:
    def __init__(self, breed: str, name: str):
        """
        Создание и подготовка к работе объекта "Cat"
 
        :param breed: Порода
        :param name: Имя
 
        Примеры:
        >>> c_blue = Cat('some_breed','Blue')  # инициализация экземпляра класса
        """
        self.breed = breed
        self.name = name
 
    def pet_cat(self) -> None:
        """
        Погладить.
 
        Примеры:
        >>> c_blue = Cat('some_breed','Blue')
        >>> c_blue.pet_cat()
        """
        ...
 
    def play_cat(self, time: int) -> None:
        """
        Поиграть.
 
        :param time: Время игры
        :raise ValueError: Если величина времени меньше 0, вызываем ошибку.
 
        Примеры:
        >>> c_blue = Cat('some_breed','Blue')
        >>> c_blue.play_cat()
        """
        if time < 0:
            raise ValueError("Время игры не может быть меньше 0")
        ...
 
 
class Coat:
    def __init__(self, size: str, color: str):
        """
        Создание и подготовка к работе объекта "Coat"
 
        :param size: Размер
        :param color: Цвет
 
        Примеры:
        >>> winter_coat = Coat('XL', 'black')  # инициализация экземпляра класса
        """
        self.size = size
        self.color = color
 
    def put_on(self) -> None:
        """
        Надеть.
 
        Примеры:
        >>> winter_coat = Coat('XL', 'black')
        >>> winter_coat.put_on()
        """
        ...
 
    def open_up(self) -> None:
        """
        Расстегнуть.
 
        Примеры:
        >>> winter_coat = Coat('XL', 'black')
        >>> winter_coat.open_up()
        """
        ...
 
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
