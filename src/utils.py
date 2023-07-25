import logging

from requests import RequestException

from constants import EXPECTED_STATUS
from exceptions import ParserFindTagException


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None, status=None):
    try:
        if status:
            searched_tag = soup.find(text=status)
        else:
            searched_tag = soup.find(tag, attrs=(attrs or {}))
        if searched_tag is None:
            raise Exception
    except Exception:
        if status:
            error_msg = f'Тэг, имеющий текст "{status}" не найден'
        else:
            error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    else:
        return searched_tag


def check_index(index):
    if index in EXPECTED_STATUS:
        return True
    else:
        raise KeyError('Такого статуса нет в словаре')
