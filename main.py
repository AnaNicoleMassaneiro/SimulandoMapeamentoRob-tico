# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt

# Dimensões do mapa
map_width = 10
map_height = 10

# Resolução do mapa (tamanho de cada célula)
resolution = 0.1

# Inicialize o mapa com células vazias
map = np.zeros((int(map_width / resolution), int(map_height / resolution)))

# Pose inicial do robô (x, y, theta)
robot_pose = [2, 2, 0]

# Simule leituras do sensor (distâncias em metros)
sensor_readings = [(1.0, 0.5), (2.0, 0.2), (3.0, 0.8)]

# Função para atualizar o mapa com as leituras do sensor
def update_map(robot_pose, sensor_readings):
    for reading in sensor_readings:
        # Calcule a posição global da leitura do sensor com base na pose do robô
        x_sensor_global = robot_pose[0] + reading[0] * np.cos(robot_pose[2])
        y_sensor_global = robot_pose[1] + reading[0] * np.sin(robot_pose[2])

        # Converta as coordenadas globais para índices do mapa
        x_cell = int(x_sensor_global / resolution)
        y_cell = int(y_sensor_global / resolution)

        # Atualize a célula correspondente no mapa como ocupada
        map[x_cell, y_cell] = 1

# Atualize o mapa com as leituras do sensor
update_map(robot_pose, sensor_readings)

# Exiba o mapa
plt.imshow(map, origin="lower", extent=(0, map_width, 0, map_height), cmap='gray')
plt.show()
