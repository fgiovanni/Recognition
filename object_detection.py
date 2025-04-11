import cv2
import numpy as np
import time
from datetime import datetime

# Carrega o modelo YOLO
print("Carregando modelo YOLO...")
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configuração da câmera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Reduzir resolução para melhor performance
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Configuração da fonte e cores
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Configuração do YOLO
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
confidence_threshold = 0.3  # Reduzido para detectar mais objetos
nms_threshold = 0.4  # Threshold para Non-Maximum Suppression

# Variáveis para FPS
fps_start_time = time.time()
fps_frame_count = 0
fps = 0

# Dicionário para rastrear objetos detectados
detected_objects = {}

print("\nIniciando detecção de objetos...")
print("Pressione ESC ou clique no X da janela para encerrar\n")

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    # Prepara a imagem para o YOLO
    blob = cv2.dnn.blobFromImage(img, 1/255, (320, 320), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    # Desenha as detecções e registra no terminal
    current_objects = set()
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[class_ids[i]]
            
            # Adiciona ao conjunto de objetos atuais
            current_objects.add(label)
            
            # Desenha retângulo
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            
            # Desenha fundo para o texto
            (text_width, text_height), _ = cv2.getTextSize(f"{label} {confidence}", font, 1, 2)
            cv2.rectangle(img, (x, y - text_height - 10), (x + text_width, y), color, -1)
            
            # Desenha texto
            cv2.putText(img, f"{label} {confidence}", (x, y - 5), font, 1, (255, 255, 255), 2)

    # Verifica novos objetos detectados
    for obj in current_objects:
        if obj not in detected_objects:
            detected_objects[obj] = True
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Novo objeto detectado: {obj}")

    # Calcula e exibe FPS
    fps_frame_count += 1
    if (time.time() - fps_start_time) >= 1.0:
        fps = fps_frame_count
        fps_frame_count = 0
        fps_start_time = time.time()
    
    cv2.putText(img, f"FPS: {fps}", (10, 30), font, 2, (0, 255, 0), 2)

    cv2.imshow("Detecção de Objetos", img)
    
    # Verifica se a janela foi fechada
    if cv2.getWindowProperty("Detecção de Objetos", cv2.WND_PROP_VISIBLE) < 1:
        break
        
    key = cv2.waitKey(1)
    if key == 27:  # ESC para sair
        break

print("\nEncerrando programa...")
cap.release()
cv2.destroyAllWindows() 