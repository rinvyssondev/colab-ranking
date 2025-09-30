import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dadosutf.csv", encoding="utf-8", sep=";")
df.columns = df.columns.str.strip()

df["POSICAO22"] = pd.to_numeric(df["POSICAO22"], errors="coerce")
df["POSICAO25"] = pd.to_numeric(df["POSICAO25"], errors="coerce")

total_estados = df.shape[0]

df["RANK22"] = total_estados + 1 - df["POSICAO22"]
df["RANK25"] = total_estados + 1 - df["POSICAO25"]

df_sorted = df.sort_values("POSICAO25")
estados = df_sorted["ESTADOS"]
rank22 = df_sorted["RANK22"]
rank25 = df_sorted["RANK25"]

colors22 = ['#ff0000' if estado == "Alagoas" else '#3d3d3d' for estado in estados]
colors25 = ['#0000BB' if estado == "Alagoas" else '#a3a3a3' for estado in estados]

bar_height = 0.40
spacing = 0.08

y = np.arange(len(estados)) * 1.5 
y22 = y - bar_height/2 - spacing/2   
y25 = y + bar_height/2 + spacing/2  

plt.figure(figsize=(12, 14))  
bars22 = plt.barh(y22, rank22, height=bar_height, color=colors22, label="2022")
bars25 = plt.barh(y25, rank25, height=bar_height, color=colors25, label="2025")

plt.gca().invert_yaxis()

plt.yticks(y, estados)

plt.xticks(range(1, total_estados+1), [f"{i}º" for i in range(total_estados, 0, -1)])

plt.xlabel("Posição")
plt.title("Ranking dos Estados")
plt.legend()
plt.tight_layout()
plt.show()
