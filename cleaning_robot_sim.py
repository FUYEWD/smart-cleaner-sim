"""
Smart Cleaning Robot Simulation 🧹🤖
-----------------------------------
Author: Wei-Kai Chang (張為凱)
Description:
    A simple Python simulation of a cleaning robot moving in a 2D grid.
    The robot avoids obstacles, cleans tiles, and tries to maximize coverage.
    This project demonstrates basic algorithmic thinking in robotics simulation.

    Visualization uses matplotlib animation for clarity.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# === 模擬環境參數設定 ===
GRID_SIZE = 20        # 模擬地板大小 (20x20)
OBSTACLE_RATIO = 0.1  # 障礙物比例
STEPS = 300           # 模擬步數

# === 建立地圖 ===
# 0: 空地, 1: 障礙物, 2: 清潔過的地方
env = np.zeros((GRID_SIZE, GRID_SIZE))
num_obstacles = int(GRID_SIZE * GRID_SIZE * OBSTACLE_RATIO)

# 隨機放置障礙物
for _ in range(num_obstacles):
    x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    env[x, y] = 1

# === 初始位置設定 (隨機找到一個不是障礙物的位置) ===
while True:
    robot_x, robot_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    if env[robot_x, robot_y] == 0:
        break

# 定義可能的移動方向 (上, 下, 左, 右)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# === 主邏輯函式 ===
def move_robot():
    """根據簡單邏輯進行移動與避障"""
    global robot_x, robot_y
    env[robot_x, robot_y] = 2  # 標記為已清潔

    # 隨機選方向直到找到可以走的路
    for _ in range(10):  # 最多嘗試10次避免死循環
        dx, dy = random.choice(directions)
        new_x, new_y = robot_x + dx, robot_y + dy
        # 確保不出界 & 不撞障礙物
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and env[new_x, new_y] != 1:
            robot_x, robot_y = new_x, new_y
            break

# === 可視化設定 ===
fig, ax = plt.subplots()
im = ax.imshow(env, cmap='viridis', vmin=0, vmax=2)
plt.title("Smart Cleaning Robot Simulation")
plt.axis("off")

def update(frame):
    """動畫更新每一幀"""
    move_robot()
    im.set_data(env)
    return [im]

# 動畫運行
ani = animation.FuncAnimation(fig, update, frames=STEPS, interval=100, blit=True)
plt.show()

# === 結果分析 ===
cleaned = np.sum(env == 2)
coverage = cleaned / (GRID_SIZE * GRID_SIZE - num_obstacles)
print(f"Simulation finished after {STEPS} steps.")
print(f"Cleaning coverage: {coverage:.2%}")
