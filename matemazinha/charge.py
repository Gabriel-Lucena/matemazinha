import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constantes
k = 8.9875e9  # N m^2/C^2
mu_0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo (N/A^2)

# Definindo as cargas, suas posições e velocidades
q1 = 1e-6  # Carga da partícula 1 em Coulombs
q2 = -1e-6  # Carga da partícula 2 em Coulombs

r1 = np.array([0.0, 0.0, 0.0], dtype=np.float64)
r2 = np.array([10.0, 1.0, 1.0], dtype=np.float64)

v1 = np.array([100.0, -20.0, 0.0], dtype=np.float64)
v2 = np.array([50.0, -1110.0, 300.0], dtype=np.float64)

# Função para calcular a força e o campo magnético
def calcular_forcas_campos(r1, r2, v1, v2, q1, q2):
    r = r2 - r1
    distancia = np.linalg.norm(r)
    direcao = r / distancia
    forca_elet = k * abs(q1 * q2) / distancia**2 * direcao
    
    # Campo magnético produzido por v1 e v2
    B1 = mu_0 * q1 * np.cross(v1, r) / distancia**3
    B2 = mu_0 * q2 * np.cross(v2, -r) / distancia**3
    
    # Força magnética sobre v1 e v2
    forca_magn1 = q1 * np.cross(v1, B2)
    forca_magn2 = q2 * np.cross(v2, B1)
    
    return forca_elet, forca_magn1, forca_magn2

# Parâmetros da simulação
dt = 0.01
t_total = 10
num_frames = int(t_total / dt)

posicoes1 = []
posicoes2 = []

posicao1 = r1.copy()
posicao2 = r2.copy()

for _ in range(num_frames):
    forca_elet, forca_magn1, forca_magn2 = calcular_forcas_campos(posicao1, posicao2, v1, v2, q1, q2)
    
    acel1 = (forca_elet + forca_magn1) / q1
    acel2 = (forca_elet + forca_magn2) / q2
    
    v1 += acel1 * dt
    v2 += acel2 * dt
    
    posicao1 += v1 * dt
    posicao2 += v2 * dt
    
    posicoes1.append(posicao1.copy())
    posicoes2.append(posicao2.copy())

posicoes1 = np.array(posicoes1)
posicoes2 = np.array(posicoes2)

# Visualização das trajetórias finais
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

k = 50

ax.set_xlim(-k, k)
ax.set_ylim(-k, k)
ax.set_zlim(-k, k)
ax.set_xlabel('Posição x (m)')
ax.set_ylabel('Posição y (m)')
ax.set_zlabel('Posição z (m)')
ax.set_title('Trajetórias finais de interação entre duas cargas elétricas e campos magnéticos no espaço tridimensional')

# Plotando as trajetórias das cargas
ax.plot(posicoes1[:, 0], posicoes1[:, 1], posicoes1[:, 2], label='Carga 1', marker='o')
ax.plot(posicoes2[:, 0], posicoes2[:, 1], posicoes2[:, 2], label='Carga 2', marker='x')

ax.legend()
plt.show()
