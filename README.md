# Statapp

![Release info](https://img.shields.io/github/v/release/shizand/statapp)
![Python version](https://img.shields.io/badge/python-3.8-blue.svg)
![Codacy grade](https://img.shields.io/codacy/grade/c4e370d74a8a4575b79afa8b9b74d130)
![License info](https://img.shields.io/github/license/shizand/statapp)

Автоматизированное программное средство по статистическому анализу и регрессионному моделированию.

## Поддерживаемые ОС и архитектуры

В теории, должно работать на любой архитектуре и ОС где запускается Python 3.8 и есть Qt.

Работоспособность проверена на x64:
-  на Windows 7, 10;
-  на ALT Linux 10.2;

## Установка

Существует два варианта statapp и statapp-onefile. Различия в том, что onefile версия поставляется одним единственным бинарным файлом. На Windows системах с включенным антивирусом это может вызывать [некоторые проблемы](https://qna.habr.com/q/988553).

### Готовые двоичные файлы

[Скачайте архив](https://github.com/shizand/statapp/releases) под вашу платформу и распакуйте в любом месте.

### Сборка из исходников

В этом проекте используется [poetry](https://python-poetry.org/).

```bash
poetry install
poetry run pyinstaller statapp.spec # или poetry run pyinstaller stat-onefile.spec
```

## Использование

<!-- TODO -->

## Чем я могу помочь проекту?

-  [Сообщить об ошибке](https://github.com/shizand/statapp/issues/new?labels=%D0%B1%D0%B0%D0%B3)

## Лицензия

[GPL-3.0 © Maxim Slipenko, Eugene Lazurenko.](https://github.com/shizand/statapp/blob/main/LICENSE)
