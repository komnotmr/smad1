# smad1
## Синтаксис
\<Programm\> \<Key1\> \<Key2\> \<Filename\>

## Ключи
1. **Key1**
* ***--gen-sigm*** - Генерирует сигму
* ***--gen-points*** - Генерирует точки
1. **Key2**
* ***--error*** - Добавляет помехи в рассчёты
* ***--no-error*** - Исключает помехи из рассчётов

**Filename** - Имя файла, куда будут сохранены результаты генерации

## Примеры использования

Генерация значения сигмы в файл sigma.log

> <code>./lab1.py --gen-sigm --no-error sigma.log</code>

Генерация точек с помехами в файл points.log

> <code>./lab1.py --gen-points --error sigma.log</code>
