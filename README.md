# Парсер документации python и PEP

Парсер собирает данные и логирует свою работу и ошибки в командную строку и файл логов:
```
https://docs.python.org/3/
```
- список изменений в python `python main.py whats-new [аргументы]`
- список версий python и ссылки на их документацию `python main.py latest-versions [аргументы]`
- актуальная документация `python main.py download [аргументы]`

```
https://peps.python.org/
```
- сбор информации о стандартах PEP - `python main.py pep [аргументы]`

### Аргументы
   
- -h, --help
Общая информация о командах `python main.py -h`
- -c, --clear-cache
Очистка кеша перед выполнением парсинга `python main.py [вариант парсера] -c`
- -o {pretty,file}, --output {pretty,file}   
Дополнительные способы вывода данных   
pretty - данные в командной строке предстанут в виде таблицы   
file - сохраняет информацию в формате csv в папке results `python main.py [вариант парсера] -o file`

### Запуск парсера
bs4_parser_pep/src/`python main.py [вариант парсера] [аргументы]`