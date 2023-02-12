if __name__ == "__main__":
    # Write your solution here
    pass

class House:
    """ Базовый класс дома. """

    def __init__(self, material: str, floor: int):
        self._material = material
        self._floor = floor

    @property
    def material(self):
        return self._material

    @property
    def floor(self):
        return self._floor

    def __str__(self):
        return f"Материал {self._material}. Этажность {self._floor}"

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self._material!r}, floor={self._floor!r})"


class ApartmentBuilding(House):
    def __init__(self, material: str, floor: int, flats: int):
        super().__init__(material, floor)
        self._flats = None
        self._flats = flats

    @property
    def flats(self):
        return self._flats

    @flats.setter
    def flats(self, new_flat) -> None:
        if isinstance(new_flat, int):
            if new_flat > 0:
                self.new_flat = new_flat
            else:
                raise ValueError(f'Invalid number of flats: {new_flat!r}')
        else:
            raise TypeError(f'Type of flats: {new_flat!r}')
        self._flats = new_flat

    def __repr__(self):
        return f"Дом: {self.material}\nЭтажей: {self.floor}\nКвартир: {self._flats}"


class DetachedHouse(House):
    def __init__(self, material: str, floors: int, room: int):
        super().__init__(material, floors)
        self._room = None
        self._room = room

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, new_room) -> None:
        if isinstance(new_room, int):
            if new_room > 0:
                self.new_room = new_room
            else:
                raise ValueError(f'Invalid number of rooms: {new_room!r}')
        else:
            raise TypeError(f'Type of rooms: {new_room!r}')
        self._room = new_room

    def __repr__(self):
        return f"Дом: {self.material}\nЭтажей: {self.floor}\nКомнат: {self._room}"
