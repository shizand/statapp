# Statapp

![Release info](https://img.shields.io/github/v/release/shizand/statapp)
![Python version](https://img.shields.io/badge/python-3.8-blue.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c4e370d74a8a4575b79afa8b9b74d130)](https://app.codacy.com/gh/shizand/statapp/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
![License info](https://img.shields.io/github/license/shizand/statapp)

Автоматизированное программное средство по статистическому анализу и регрессионному моделированию. Является идейным продолжателем программы STAT.exe (Produced by Reutov V.N., Donetsk University, 1990).

Разработано двумя студентами ФГБОУ ВО «ДонНТУ» для своего университета.

## Поддерживаемые ОС и архитектуры

В теории, должно работать на любой архитектуре и ОС, где запускается Python 3.8 и есть Qt 5.

Работоспособность проверена на x64:

* на Windows 7, 10;
* на ALT Linux 10.2.

## Установка

Программа распространяется с помощью [PyInstaller](https://pyinstaller.org/en/stable/). 

Существует две версиии: **statapp** и **statapp-onefile**. 

Различия в том, что onefile версия поставляется одним единственным бинарным файлом. На Windows системах с включенным антивирусом это может вызывать [некоторые проблемы](https://qna.habr.com/q/988553).

### Готовые двоичные файлы

[Скачайте архив](https://github.com/shizand/statapp/releases) под вашу платформу и распакуйте в любом месте.

### Сборка из исходников

В этом проекте используется [poetry](https://python-poetry.org/).

```bash
poetry install
pyinstaller statapp.spec # или pyinstaller statapp.spec -- --one-file
```

## Использование

<!-- TODO -->

## Чем я могу помочь проекту?

* [Сообщить об ошибке](https://github.com/shizand/statapp/issues/new?labels=%D0%B1%D0%B0%D0%B3)

## Исходный код

Исходный код доступен на [GitHub](https://github.com/shizand/statapp).
Также есть зеркала:

* [GitFic](https://gitflic.ru/project/shizand/statapp);
* [Gitea сервер](https://git.slipenko.com/shizand/statapp).

## Лицензия

[GPL-3.0 © Maxim Slipenko, Eugene Lazurenko.](https://github.com/shizand/statapp/blob/main/LICENSE)
