SOA/hw-1
Сериализация и десериализация различных форматов данных

Для запуска образа выполните следующие команды:
```
docker build . -t starboy369/serialization
docker run -it starboy369/serialization
```


Для запуска программы внутри запущенного образа выполните следующую команду:
```
python3 ./run.py           
Usage: run.py [OPTIONS]
Try 'run.py --help' for help.

Error: Invalid value for -f': is not one of 'naive', 'avro', 'json', 'pbuffer', 'mpack', 'yaml', 'xml'.

python3 ./run.py -f naive
naive - sizeof: 244; serialization time: 0.008ms deserialization time: 0.006ms
```

Программа возвращает количество байт, занимаемых переданной структурой в выбранном формате и скорость сериализации и десериализации.