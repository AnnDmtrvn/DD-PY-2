class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError(f'Invalid number of pages: {pages!r}')
        else:
            raise TypeError(f'Type of pages: {pages!r}')

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nСтраниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        if isinstance(new_duration, float):
            if new_duration > 0:
                self.new_duration = new_duration
            else:
                raise ValueError(f'Invalid duration: {new_duration!r}')
        else:
            raise TypeError(f'Type of duration: {new_duration!r}')
        self._duration = new_duration

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nПродолжительность: {self.duration}"
