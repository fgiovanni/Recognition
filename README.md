# Sistema de Detecção de Objetos em Tempo Real

## Visão Geral
Este projeto implementa um sistema de detecção de objetos em tempo real utilizando visão computacional e aprendizado de máquina. O sistema é capaz de identificar e classificar diversos objetos através da câmera do computador, exibindo os resultados em tempo real com informações detalhadas.

## Tecnologias Utilizadas

### 1. OpenCV (Open Source Computer Vision Library)
- **O que é**: Biblioteca open-source para processamento de imagens e visão computacional
- **Por que foi usado**: 
  - Fornece ferramentas robustas para captura e processamento de vídeo
  - Implementa algoritmos eficientes para manipulação de imagens
  - Possui integração nativa com o modelo YOLO

### 2. YOLO (You Only Look Once)
- **O que é**: Algoritmo de detecção de objetos baseado em redes neurais profundas
- **Por que foi usado**:
  - Alta velocidade de processamento em tempo real
  - Boa precisão na detecção de múltiplos objetos
  - Capacidade de detectar mais de 80 classes diferentes de objetos

### 3. NumPy
- **O que é**: Biblioteca para computação numérica em Python
- **Por que foi usado**:
  - Manipulação eficiente de arrays multidimensionais
  - Cálculos matemáticos otimizados
  - Suporte para operações com matrizes necessárias no processamento de imagens

## Conceitos Implementados

### 1. Detecção em Tempo Real
- Captura contínua de frames da câmera
- Processamento de cada frame para detecção de objetos
- Exibição imediata dos resultados

### 2. Otimização de Performance
- Redução da resolução da câmera (640x480)
- Redimensionamento das imagens para processamento (320x320)
- Controle de FPS para garantir fluidez

### 3. Sistema de Logging
- Registro temporal de objetos detectados
- Evita duplicação de logs para o mesmo objeto
- Formato: [HH:MM:SS] Novo objeto detectado: nome_do_objeto

### 4. Interface Visual
- Exibição de retângulos ao redor dos objetos detectados
- Etiquetas com nome do objeto e confiança da detecção
- Indicador de FPS em tempo real
- Fundo colorido para melhor legibilidade das etiquetas

## Funcionalidades Principais

1. **Detecção de Objetos**
   - Identifica múltiplos objetos simultaneamente
   - Classifica objetos em mais de 80 categorias
   - Exibe nível de confiança para cada detecção

2. **Visualização**
   - Exibição em tempo real da câmera
   - Marcadores visuais para objetos detectados
   - Informações de performance (FPS)

3. **Logging**
   - Registro de novos objetos detectados
   - Timestamp para cada detecção
   - Saída no terminal para monitoramento

4. **Controles**
   - Botão de fechar habilitado
   - Tecla ESC para encerramento
   - Interface responsiva

## Configurações Técnicas

### Thresholds
- **Confiança**: 0.3 (30% de confiança mínima para detecção)
- **NMS**: 0.4 (Non-Maximum Suppression para evitar detecções duplicadas)

### Resoluções
- Câmera: 640x480 pixels
- Processamento: 320x320 pixels
- FPS alvo: 30 frames por segundo

## Aplicações Práticas

1. **Monitoramento de Segurança**
   - Detecção de pessoas e objetos em áreas monitoradas
   - Registro de eventos em tempo real

2. **Automação Industrial**
   - Controle de qualidade
   - Detecção de objetos em linhas de produção

3. **Acessibilidade**
   - Auxílio para pessoas com deficiência visual
   - Descrição automática de ambientes

4. **Pesquisa e Desenvolvimento**
   - Prototipagem de sistemas de visão computacional
   - Testes de algoritmos de detecção

## Limitações e Considerações

1. **Performance**
   - Depende da capacidade do hardware
   - Pode ser necessário ajustar resoluções em computadores menos potentes

2. **Precisão**
   - Depende da qualidade da câmera
   - Pode variar com condições de iluminação
   - Thresholds podem precisar de ajustes para casos específicos

3. **Requisitos**
   - Python 3.11 ou superior
   - Câmera funcional
   - Espaço em disco para os arquivos do modelo YOLO

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Configuração do Ambiente

1. Clone este repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie e ative o ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate
# No Windows:
# venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Baixe os arquivos do modelo YOLO:
```bash
# Baixar arquivos necessários
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
wget https://pjreddie.com/media/files/yolov3.weights
```

## Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado

2. Execute o script:
```bash
python object_detection.py
```

3. Para sair do programa, pressione a tecla ESC

## Estrutura do Projeto

- `object_detection.py`: Script principal de detecção de objetos
- `requirements.txt`: Lista de dependências do projeto
- `coco.names`: Arquivo com as classes de objetos que podem ser detectados
- `yolov3.cfg`: Arquivo de configuração do modelo YOLO
- `yolov3.weights`: Pesos do modelo YOLO

## Notas

- O programa usa a câmera padrão do computador (índice 0)
- A detecção é feita em tempo real
- Objetos detectados são marcados com retângulos coloridos
- O nome do objeto e a confiança da detecção são exibidos na tela 