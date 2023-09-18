"""
Абстрактный класс для любой БД
 Новая реализация БД должна реализовать 3 метода:

 1. get_vacancies (получить список вакансий из базы данных)
 2. save_vacancies (сохранить список вакансий в БД)
 3. delete_vacancies (удалить список вакансий из базы данных)

"""
from abc import ABC, abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericDB(ABC):

    @staticmethod
    @abstractmethod
    def get_vacancies() -> list[Vacancy]:
        """
        :return: Список объектов класса: "Вакансии", содержащих информацию о вакансиях.
        """
        pass

    @staticmethod
    @abstractmethod
    def save_vacancies(vacancies: list[Vacancy]) -> None:
        """
        :param vacancies: Список класса: Объекты «Вакансии», содержащие информацию о вакансиях
        """
        pass

    @staticmethod
    @abstractmethod
    def delete_vacancies() -> None:
        pass
