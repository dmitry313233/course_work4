"""
Абстрактный класс для любого парсера
Новая реализация парсера должна реализовать 3 метода:

 1. get_vacancies (get vacancies page)
 2. parse_vacancy (get vacancy data)
 3. make_request (make request to website API)

"""
import requests

from abc import ABC, abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericParser(ABC):

    @abstractmethod
    def get_vacancies(self, pages_count: int, keywords: list[str]) -> list[Vacancy]:
        """
        :param pages_count: Количество страниц для анализа (20 вакансий на страницу)
        :param keywords: Список слов для поиска в описании вакансии

        :return: List of the class: 'Объекты «Вакансии», содержащие информацию о вакансиях.
        """

        pass

    @abstractmethod
    def parse_vacancy(self, vacancy_info: dict) -> Vacancy:
        """
        :param vacancy_info: Словарь с некоторыми полями, содержащими информацию о текущей вакансии

        :return: Объект «Вакансия» с проанализированными полями
        """
        pass

    @abstractmethod
    def make_request(self, url: str) -> requests.Response:
        """
        :param url: Url to website API

        :return: API response
        """
        pass