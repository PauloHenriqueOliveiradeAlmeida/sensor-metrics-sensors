# 🚨 Sensor Metrics Sensors

Projeto desenvolvido como atividade avaliativa para matéria de IOT, o projeto consiste em dois sensores falsos que enviam dados via MQTT para um backend

## 📚 Stack usada

![Stack](https://img.shields.io/badge/python-blue?logo=python&logoColor=white&style=for-the-badge)


## 🦾 Funcionalidades

- Gera dados randômicos com base em um range de valores
- Envia tópicos para um broker MQTT


## 🔧 Configuração do projeto
#### 📁 Ajustar variáveis

Em ambos os arquivos, caso você queira alterar a configuração padrão (usar um MQTT Broker fora do host local, por exemplo), você pode alterar as variáveis:
```python
broker = "localhost"
port = 1883
topic = "update-sensor-metrics"
```

### 🏞️ Criando um novo ambiente virtual
Execute o comando para criar um novo ambiente virtual:
```ini
python -m venv .venv

source .venv/bin/activate
```

### 📦 Instalação dos pacotes
Execute a instalação das dependências necessárias:
```ini
pip install --no-cache-dir -r requirements.txt
```

### 🚀 Executando o projeto:
Execute os dois sensores:
```ini
python temperature.py

python humidity.py
```

## 🏃 Testando
Para testar, será necessário utilizar algum backend com suporte a MQTT ou algo do gênero, ou, instalar o frontend e o backend do projeto:

Frontend: https://github.com/PauloHenriqueOliveiradeAlmeida/sensor-metrics-dashboard-web

Backend: https://github.com/PauloHenriqueOliveiradeAlmeida/sensor-metrics-dashboard-backend
