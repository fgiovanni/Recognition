#!/bin/bash

# Criar ambiente virtual com Python 3.11
echo "Criando ambiente virtual com Python 3.11..."
/usr/local/opt/python@3.11/bin/python3.11 -m venv venv

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Baixar arquivos do YOLO
echo "Baixando arquivos do modelo YOLO..."
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
wget https://pjreddie.com/media/files/yolov3.weights

echo "Configuração concluída! Para executar o programa, use:"
echo "source venv/bin/activate"
echo "python object_detection.py" 