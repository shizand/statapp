<!--
Copyright (c) 2024 Maxim Slipenko, Eugene Lazurenko.

This file is part of Statapp
(see https://github.com/shizand/statapp).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
-->
# Руководство пользователя для программы "Statapp"

## Условные обозначения

`Взаимодействие` - так отображается интерфестные части приложения с которыми пользователь может и должен взаимодействовать. к тами относятся кнопки, пункты меню, окна приложения, страницы в моделировании и тд.

*Пример* - так отображаются комментарии или описания. Обычно используются в качестве подписей к картинкам.

***Параметр*** - так отображаются параметры, которые пользователь может получить в результате вычислений в приложении.

## Введение

"Statapp" — это программное решение для статистического анализа и регрессионного моделирования, позволяющее специалистам в области данных проводить глубокий анализ и создавать точные прогностические модели.

## Теоретические сведения

*-- В разработке --*

## Начало работы

### Генерация показателей

<hr>

### Генерация отклика

Перед тем как начать анализ, необходимо сгенерировать ***отклики***, которые будут использоваться как зависимые переменные в моделях:

1. Перейдите в меню `Генерация показателей`.
2. Выберите `Генерация отклика`.

После этого откроется окно `Генерация отклика`:

<image src="files/Генерация показателей - Генерация отклика.PNG">

*Пример пункта меню* `Генерация отклика`

3. Укажите необходимые параметры для генерации данных и нажмите кнопку `Сгенерировать`.

<image src="files/Окно - Генерация отклика.PNG" width=400>

*Пример окна* `Генерация отклика`

После этого окно должно закрыться и на `Белом листе` в `Главном окне` появится колонка со случайно сгенерированными данными отклика по заданным показателям.

<hr>

### Генерация фактора

После генерации ***откликов*** следует сгенерировать ***факторы***, которые будут служить независимыми переменными. Для генерации ***факторов*** необходимо выполнить следующие шаги:

1. Перейдите в меню `Генерация показателей`.
2. Выберите `Генерация фактора`.

После этого откроется окно `Генерация фактора`:

<image src="files/Генерация показателей - Генерация фактора.PNG">

*Пример пункта меню* `Генерация фактора`

3. Выберите нужный тип связи к ***отклику*** (прямая или обратная).
4. Укажите оставшиеся параметры для генерации данных и нажмите кнопку `Сгенерировать`.

<image src="files/Окно - Генерация фактора.PNG" width=400>

*Пример окна* `Генерация отклика`

Можно добавлять несколько факторов.

<hr>

### Удаление факторов

Так как программа `Statapp` генерирует показатели ***Факторов*** случайным образом в границах заданого ***Среднеквадратического отклонения*** то при генерации нескольких ***Факторов*** может возникнуть необходимость удаления некоторых из них. Для этого необходимо выполнить следующие шаги:

1. Выберите необходимый ***Фактор*** для удаления и кликните по `Заголовку` с обозначением `Xn` правой кнопкой мыши.
2. Нажмите на появившуюся кнопку `Удалить` для удаления выбранного ***Фактора***.

*Внимание после удаления ***Фактора*** действие уже нельзя будет отменить*

<image src="files/Окно - Удаление.PNG">

*Пример появившейся кнопки* `Удалить`

Удаленный ***Фактор*** пропадет из таблицы и более не будет учитываться в `Анализе` и `Моделировании`.

<hr>

### Анализ данных

После генерации ***отклика*** и ***факторов*** можно приступать к анализу данных.

<hr>

### Дисперсионный анализ

1. Перейдите в меню `Анализ данных`.
2. Выберите `Дисперсионный анализ`.

<image src="files/Анализ данных - Дисперсионный анализ.PNG">

*Пример пункта меню* `Дисперсионный анализ`

После этого откроется окно `Дисперсионный анализ`:

<image src="files/Окно - Дисперсионный анализ.PNG">

*Пример окна* `Дисперсионный анализ`

<hr>

### Корреляционный анализ

1. Перейдите в меню `Анализ данных`.
2. Выберите `Корреляционный анализ`.

<image src="files/Анализ данных - Корреляционный анализ.PNG">

*Пример пункта меню* `Корреляционный анализ`

После этого откроется окно `Корреляционный анализ`:

<image src="files/Окно - Корреляционный анализ.PNG">

*Пример окна* `Корреляционный анализ`

<hr>

### Моделирование

После генерации отклика и факторов можно перейти к построению регрессионных моделей.

Здесь вы можете увидеть параметры модели, её характеристики, прогноз и отклонения, а также график прогноза и отклонения.

1. Перейдите на вкладку `Моделирование`.
2. Выберите тип модели для построения: `Линейный полином`, `Квадратичный полином` или `Преобразования`.

<image src="files/Моделирование - Линейный полином.PNG">

*Пример список пунктов меню* `Моделирование`

На странице `Модель` любого окна из `Моделирование` можно увидеть данные ***Коэффициент регрессии*** и ***Коэффициент значимости*** в виде таблицы для отклика и каждого из факторов. В нижней части окна располагаются вычисленные значения для параметров: ***Остаточная дисперсия***, ***Остаточная дисперсия (масштабированная)***, ***F1 - отношение Фишера***, ***Коэффициент множественной детерминации***,

<image src="files/Окно - Полином (Линейный полином).PNG">

*Пример страницы* `Модель` *окна* `Линейный полином`

На странице `Прогноз` любого окна из `Моделирование` можно увидеть значения ***Прогноза*** и ***Отклонения*** для каждого ранее сгенерированного значения ***Отклика***.

<image src="files/Окно - Полином - Прогноз.PNG">

*Пример страницы* `Прогноз` *окна* `Линейный полином`

На странице `График` любого окна из `Моделирование` можно увидеть график ***Прогноза*** (график) и ***Отклонения*** (точки).

<image src="files/Окно - Полином - График.PNG">

*Пример страницы* `График` *окна* `Линейный полином`

При необходимости, в окне `Моделирование` - `Преобразования` для каждого фактора вы можете выбрать одно из доступных преобразований.

<image src="files/Окно - Полином (Преобразования).PNG">

*Пример окна* `Преобразования`

Для выбора преобразования для определенного фактора необходимо выполнить следующие шаги:

1. Перейдите на страницу `Модель` в окне `Преобразования`.
2. Дважды нажмите на нужную ячейку в колонке ***Преобразования***.
3. Выберите необходимое преобразование из выпадающего списка.

<image src="files/Преобразования - Выбор преобразования.PNG">

*Пример списка выбора* ***Преобразования*** *фактора в окне* `Преобразования`

*Комментарий: если значения не персчитались попробуйте снять выделение с ячейки, путем нажатия на другую ячейку*

<hr>

### Сохранение и открытие файла

Сгенерированные значения ***отклика*** и ***фактора*** из таблицы в `Главном окне` можно сохранить или зугрузить из файла ***.txt*** и ***.csv***.

### Сохранение файла

1. Перейдите в меню `Файл`.
2. Выберите `Сохранить`.

<image src="files/Файл - Сохранить.PNG">

*Пример пункта меню* `Сохранить файл`

3. Выберите путь сохранения и тип файла и нажмите кнопку `Сохранить`.

Теперь файл будет сохранен по указаному вами пути, его можно переместить куда необходимо и при необходимости загрузить обратно в приложение.

### Открытие файла

1. Перейдите в меню `Файл`.
2. Выберите `Открыть`.

<image src="files/Файл - Открыть.PNG">

*Пример пункта меню* `Открыть файл`

3. Выберите путь до открываемого файла и нажмите кнопку `Открыть`.

Приложение загрузит нужный вам файл, и при необходимости спросит нужно ли сохранять ваши текущие данные.