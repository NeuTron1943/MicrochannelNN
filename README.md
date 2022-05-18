Здесь собраны файлы, необходимые для запуска нейросети:

DP_particle_analysis -  в этом файле происходит считывание информации с файлов с данными (не включены), и моделирование распределения на детекторах, основываясь на введенных в первом блоке параметрах.
Для вычисления времени пролета используется среднее время прилета пионов для детекторов на [1, 1.7, 2.5] метрах, и если необходимо использовать другие расстояния, то нужно пересчитать времена прилета пионов.

Experiments -   файл с нейросетями (линейной и сверточной) которые используют информацию из файла, созданного скриптом DP_particle_analysis. Также можно задавать количество интервалов разбиения прицельного параметра и количество эпох обучения. Сверточная  нейросеть показывает себя лучше во многих запусках (при большом количестве эпох обучения). Для оценки качества в последне блоке приводится матрица ошибок и график обучения.

Experiments_binary -   отдельный файл для задачи бинарной классификации, структура файла такая же как в Experiments

Experiments_regression -   главный файл для обучения нейросети для задачи регрессии, структура файла такая же как в Experiments


fix_minus - скрипт для добавления пробела перед минусами в файлах данных

Time_analysis - анализ времени пролета частиц (использовался для определения среднего времени прилета пионов и протонов для заданных расстояний до детекторов)

В папке data приведен архив с примерами сгенерированных файлов распределения на детекторе. 114 - для столкновений, смоделированных в нуле координат, 110 - столкновения с распределенными координатами.  В них описывается разбиение детектора на 8 угловых частей, 4 радиальных.

В файл some_results записывается информация о результатах обучения сверточной нейросети, а именно заданный размер батча, заданное число эпох и достигнутая точность. 
