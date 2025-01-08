# Домашнее задание к занятию " `Очереди RabbitMQ` " - `Сулименков Алексей`

---

## Задание 1. Установка RabbitMQ

Используя Vagrant или VirtualBox, создайте виртуальную машину и установите RabbitMQ. Добавьте management plug-in и зайдите в веб-интерфейс.

Итогом выполнения домашнего задания будет приложенный скриншот веб-интерфейса RabbitMQ.

### Ответ

![RabbitMQ](https://github.com/biparasite/DB-11-04HW/blob/main/RabbitMQ.png)

---

## Задание 2. Отправка и получение сообщений

Используя приложенные скрипты, проведите тестовую отправку и получение сообщения. Для отправки сообщений необходимо запустить скрипт producer.py.

В качестве решения домашнего задания приложите оба скриншота, сделанных на этапе выполнения.

### Ответ

producer.py
![producer](https://github.com/biparasite/DB-11-04HW/blob/main/producer.png)

consumer.py
![consumer](https://github.com/biparasite/DB-11-04HW/blob/main/consumer.png)

---

## Задание 3. Подготовка HA кластера

Используя Vagrant или VirtualBox, создайте вторую виртуальную машину и установите RabbitMQ. Добавьте в файл hosts название и IP-адрес каждой машины, чтобы машины могли видеть друг друга по имени.

Пример содержимого hosts файла:

```bash
$ cat /etc/hosts
192.168.0.10 rmq01
192.168.0.11 rmq02
```

После этого ваши машины могут пинговаться по имени.

Затем объедините две машины в кластер и создайте политику ha-all на все очереди.

### Ответ

В качестве решения домашнего задания приложите скриншоты из веб-интерфейса с информацией о доступных нодах в кластере и включённой политикой.

![cluster1](https://github.com/biparasite/DB-11-04HW/blob/main/Cluster1.png)

![cluster2](https://github.com/biparasite/DB-11-04HW/blob/main/Cluster2.png)

![cluster3](https://github.com/biparasite/DB-11-04HW/blob/main/Cluster3.png)

Также приложите вывод команды с двух нод:

```bash
$ rabbitmqctl cluster_status
```

<details><summary>Node rmq1</summary>

```bash
Cluster status of node rabbit@rmq1 ...
Basics

Cluster name: rabbit@rmq1

Disk Nodes

rabbit@rmq1
rabbit@rmq2

Running Nodes

rabbit@rmq1
rabbit@rmq2

Versions

rabbit@rmq1: RabbitMQ 3.10.7 on Erlang 25.0.4
rabbit@rmq2: RabbitMQ 3.10.7 on Erlang 25.0.4

Maintenance status

Node: rabbit@rmq1, status: not under maintenance
Node: rabbit@rmq2, status: not under maintenance

Alarms

(none)

Network Partitions

(none)

Listeners

Node: rabbit@rmq1, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@rmq1, interface: [::], port: 61613, protocol: stomp, purpose: STOMP
Node: rabbit@rmq1, interface: [::], port: 1883, protocol: mqtt, purpose: MQTT
Node: rabbit@rmq1, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
Node: rabbit@rmq1, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@rmq1, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
Node: rabbit@rmq2, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@rmq2, interface: [::], port: 61613, protocol: stomp, purpose: STOMP
Node: rabbit@rmq2, interface: [::], port: 1883, protocol: mqtt, purpose: MQTT
Node: rabbit@rmq2, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
Node: rabbit@rmq2, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@rmq2, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0

Feature flags

Flag: classic_mirrored_queue_version, state: enabled
Flag: drop_unroutable_metric, state: enabled
Flag: empty_basic_get_metric, state: enabled
Flag: implicit_default_bindings, state: enabled
Flag: maintenance_mode_status, state: enabled
Flag: quorum_queue, state: enabled
Flag: stream_queue, state: enabled
Flag: user_limits, state: enabled
Flag: virtual_host_metadata, state: enabled
```

</details>

<details><summary>Node rmq2</summary>

```bash
Cluster status of node rabbit@rmq2 ...
Basics

Cluster name: rabbit@rmq2

Disk Nodes

rabbit@rmq1
rabbit@rmq2

Running Nodes

rabbit@rmq1
rabbit@rmq2

Versions

rabbit@rmq1: RabbitMQ 3.10.7 on Erlang 25.0.4
rabbit@rmq2: RabbitMQ 3.10.7 on Erlang 25.0.4

Maintenance status

Node: rabbit@rmq1, status: not under maintenance
Node: rabbit@rmq2, status: not under maintenance

Alarms

(none)

Network Partitions

(none)

Listeners

Node: rabbit@rmq1, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@rmq1, interface: [::], port: 61613, protocol: stomp, purpose: STOMP
Node: rabbit@rmq1, interface: [::], port: 1883, protocol: mqtt, purpose: MQTT
Node: rabbit@rmq1, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
Node: rabbit@rmq1, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@rmq1, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
Node: rabbit@rmq2, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@rmq2, interface: [::], port: 61613, protocol: stomp, purpose: STOMP
Node: rabbit@rmq2, interface: [::], port: 1883, protocol: mqtt, purpose: MQTT
Node: rabbit@rmq2, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
Node: rabbit@rmq2, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@rmq2, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0

Feature flags

Flag: classic_mirrored_queue_version, state: enabled
Flag: drop_unroutable_metric, state: enabled
Flag: empty_basic_get_metric, state: enabled
Flag: implicit_default_bindings, state: enabled
Flag: maintenance_mode_status, state: enabled
Flag: quorum_queue, state: enabled
Flag: stream_queue, state: enabled
Flag: user_limits, state: enabled
Flag: virtual_host_metadata, state: enabled
```

</details>

Для закрепления материала снова запустите скрипт producer.py и приложите скриншот выполнения команды на каждой из нод:

```bash
$ rabbitmqadmin get queue='hello'
```

![rabbitmqadmin](https://github.com/biparasite/DB-11-04HW/blobs/main/rabbitmqadmin.png)

После чего попробуйте отключить одну из нод, желательно ту, к которой подключались из скрипта, затем поправьте параметры подключения в скрипте consumer.py на вторую ноду и запустите его.

Приложите скриншот результата работы второго скрипта.

![down_rmq1](https://github.com/biparasite/DB-11-04HW/blob/main/down_rmq1.png)

---
