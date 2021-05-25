Здесь собраны файлы, необходимые для запуска нейросети:

DP_particle_analysis -  в этом файле происходит считывание информации с 11 файлов с данными (я не включал их в этот репозиторий), и моделирование распределения на детекторах, основываясь на введенных в первом блоке параметрах.
Для вычисления времени пролета используется среднее время прилета пионов для детекторов на [1, 1.7, 2.5] метрах, и если необходимо использовать другие расстояния, то нужно пересчитать времена прилета пионов.

Experiments -  главный файл с нейросетями (линейной и сверточной) которые используют информаци из файла, созданного скриптом DP_particle_analysis. Также можно задавать количество интервалов разбиения прицельного параметра и количество эпох обучения. Сверточная  нейросеть показывает себя лучше во всех запусках, поэтому стоит внимание обращать только на нее. Для оценки качества в последне блоке приводится матрица ошибок и график обучения.

fix_minus - скрипт для добавления пробела перед минусами в файлах данных

Time_analysis - анализ времени пролета частиц (использовался для определения среднего времени прилета пионов и протонов для заданных расстояний до детекторов)

В папке data я привел пример одного из сгенерированных файлов распределения на детекторе. В нем описывается разбиение детектора на 8 угловых частей, 4 радиальных и с использованием аугментации.

В файл some_results записывается информация о результатах обучения сверточной нейросети, а именно заданный размер батча, заданное число эпох и достигнутая точность. 
