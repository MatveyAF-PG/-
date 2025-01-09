# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Stair:
    def __int__(self, steps: int , material : str):
        """
        Создание и подготовка к работе обьекта "Лестница"
        :param steps: Количество ступеней
        :param material: Материал лестницы

        """
        if not isinstance(steps,(int)):
            raise TypeError ("Количество ступеней должен быть типа int")
        if steps <= 0 :
            raise ValueError("Количество ступеней должно быть положительным числом")
        self.steps = steps

        if not isinstance(material,(str)):
            raise TypeError ("Материал лестницы должен быть str")
        self.material = material
    def steps_completed (self, stepsleft : int)-> None:
        """
        Функция которая считает количество пройденных ступенек
        :param stepsleft: Остаток ступеней
        :raise ValueError: Если количество пройденных ступенек превышает количество ступенек то возвращается ошибка
        :return: Количество пройденных ступеней
        """
        if not isinstance(stepsleft,(int)):
            raise TypeError ("Остаток ступеней должен быть типа int")
        if stepsleft < 0 :
            raise ValueError ("Остаток ступеней должен быть положительным ")
        ...
    def checking_the_material (self) -> bool:
        """
        Функция которая проверяет из какого материала состоит лестница

        :return: Материал
        """
        ...

class Well:
    def __int__(self, volume : float ,liquid_volume : float):
        """
        Создание и подготовка к работе обьекта "Колодец"
        :param value: Обьем колодца
        :param liquid_volume: Обьем воды в колодце

        """
        if not isinstance(volume,(int,float)):
            raise TypeError("Обьем должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Обьем колодца должен быть положительным")
        self.volume = volume

        if not isinstance(liquid_volume,(int,float)):
            raise TypeError("Обьем воды в колодце должен быть int или float")
        if liquid_volume < 0:
            raise ValueError("Обьем жидкости не может быть отрицательным")
        self.liquid_volume = liquid_volume
    def is_empty_well(self) -> bool:
        """
        Функция которая проверяет является ли колодец пустым

        :return: Является ли колодец пустым
        """
        ...
    def remove_water_from_well(self, estimate_water: float) -> None:
        """
        Извлечение воды из колодца
        :param estimate_water: Обьем извлекаемой жидкости
        : raise ValueError: Если количество извлекаемой жидкости превышает количество воды в колодце,
        то возвращается ошибка
        :return: Обьем извлеченной жидкости

        """
        ...
class book:
    def __int__(self, pages : int , author : str):
        """
        Создание и подготовка к работе обьекта "Книга"
        :param pages: Количество страниц
        :param author: Автор
        """
        if not isinstance(pages,(int)):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages
        if not isinstance(author,(str)):
            raise TypeError("Автор должно быть str")
        self.author = author

    def read_book (self)-> None:
        """
        Функция которая прочтет книгу

        :return: Книга
        """
        ...
    def calc_pages (self) -> None:
        """
        Функция которая посчитает количество страниц
        :return: Число страниц
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass