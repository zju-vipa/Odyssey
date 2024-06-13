import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import os

sns.set()
sns.set_style("whitegrid")
fontsize = 48

# plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置加载的字体名
# plt.xticks(fontproperties='Times New Roman')
# plt.yticks(fontproperties='Times New Roman')

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
 
# 设置英文字体
plt.rcParams['font.sans-serif'] = ['Times New Roman']
 

# df = pd.DataFrame([[76, 9, '6h_vs_8z', '未使用 $\mathrm{sparsemax}$'],
#                    [54, 12, '6h_vs_8z', 'w/o CD Loss'],
#                    [76, 6, '6h_vs_8z', 'w/o CMI Loss'],
#                    [94, 3, '6h_vs_8z', 'Ours'],
#                    [47, 8, '3-8sz', 'w/o Sparse'],
#                    [36, 6, '3-8sz', 'w/o CD Loss'],
#                    [44, 13, '3-8sz', 'w/o CMI Loss'],
#                    [57, 6, '3-8sz', 'Ours']],
#                   columns=['mean', 'std', 'map_name', 'algo_id'])

# plt.figure(figsize=(8, 6))
# ax = sns.barplot(x='map_name', y='mean', data=df, hue='algo_id')
# plt.legend(loc='upper right', ncol=1, prop={'size': 18.5})
# plt.ylabel('Test Win Rate (%)', fontsize=fontsize, labelpad=10)
# plt.xlabel('SMAC scenario', fontsize=fontsize, labelpad=10)

# plt.xticks(fontsize=fontsize)
# plt.ylim((15, 100))
# plt.yticks([20, 40, 60, 80, 100], fontsize=fontsize)
# # sns.despine()

# num_hues = len(np.unique(df['algo_id']))
# for (hue, df_hue), dogde_dist in zip(df.groupby('algo_id', sort=False), np.linspace(-0.4, 0.4, 2 * num_hues + 1)[1::2]):
#     bars = ax.errorbar(data=df_hue, x='map_name', y='mean', yerr='std', ls='', lw=3, color='black')
#     xys = bars.lines[0].get_xydata()
#     bars.remove()
#     ax.errorbar(data=df_hue, x=xys[:, 0] + dogde_dist, y='mean', yerr='std', ls='', lw=3, color='black', capsize=6)

# plt.show()

# df = pd.DataFrame([[74, 19, '5m_vs_6m', 2],
#                    [86, 7, '5m_vs_6m', 4],
#                    [85, 5, '5m_vs_6m', 6],
#                    [83, 3, '5m_vs_6m', 8],
#                    [38, 9, '5-11MMM', 2],
#                    [47, 10, '5-11MMM', 4],
#                    [47, 7, '5-11MMM', 6],
#                    [45, 7, '5-11MMM', 8]],
#                   columns=['mean', 'std', 'map_name', 'algo_id'])
#time
# df = pd.DataFrame([[15.1, 19, '1Enderman MineMA-8B', 1],
#                    [10.9, 7, '1Enderman MineMA-8B', 2],
#                    [9.7, 5, '1Enderman MineMA-8B', 3],
#                    [17.2, 9, '1Enderman LLaMA-3-8B', 1],
#                    [9.6, 10, '1Enderman LLaMA-3-8B', 2],
#                    [9.2, 7, '1Enderman LLaMA-3-8B', 3],
#                    [4.4, 19, '3Zombies MineMA-8B', 1],
#                    [14.1, 7, '3Zombies MineMA-8B', 2],
#                    [8.2, 5, '3Zombies MineMA-8B', 3],
#                    [2.1, 9, '3Zombies LLaMA-3-8B', 1],
#                    [4.7, 10, '3Zombies LLaMA-3-8B', 2],
#                    [9.7, 7, '3Zombies LLaMA-3-8B', 3]],
#                   columns=['mean', 'std', 'map_name', 'algo_id'])

# health
# df = pd.DataFrame([[11.5, 19, '1Enderman MineMA-8B', 1],
#                    [0, 7, '1Enderman MineMA-8B', 2],
#                    [11.1, 5, '1Enderman MineMA-8B', 3],
#                    [11.2, 9, '1Enderman LLaMA-3-8B', 1],
#                    [3.0, 10, '1Enderman LLaMA-3-8B', 2],
#                    [11.5, 7, '1Enderman LLaMA-3-8B', 3],
#                    [0, 19, '3Zombies MineMA-8B', 1],
#                    [0, 7, '3Zombies MineMA-8B', 2],
#                    [0, 5, '3Zombies MineMA-8B', 3],
#                    [0, 9, '3Zombies LLaMA-3-8B', 1],
#                    [4.8, 10, '3Zombies LLaMA-3-8B', 2],
#                    [5.5, 7, '3Zombies LLaMA-3-8B', 3]],
#                   columns=['mean', 'std', 'map_name', 'algo_id'])

# llm iter
df = pd.DataFrame([[3.6, 19, '1Enderman MineMA-8B', 1],
                   [2.6, 7, '1Enderman MineMA-8B', 2],
                   [2.3, 5, '1Enderman MineMA-8B', 3],
                   [3.1, 9, '1Enderman LLaMA-3-8B', 1],
                   [1.2, 10, '1Enderman LLaMA-3-8B', 2],
                   [7.8, 7, '1Enderman LLaMA-3-8B', 3],
                   [8, 19, '3Zombies MineMA-8B', 1],
                   [3, 7, '3Zombies MineMA-8B', 2],
                   [5, 5, '3Zombies MineMA-8B', 3],
                   [20, 9, '3Zombies LLaMA-3-8B', 1],
                   [10, 10, '3Zombies LLaMA-3-8B', 2],
                   [18, 7, '3Zombies LLaMA-3-8B', 3]],
                  columns=['mean', 'std', 'map_name', 'algo_id'])


plt.figure(figsize=(20, 12))
color = ["#e67daf", "#f5c1c8", "#20aedd", "#9acae8"]
ax = sns.lineplot(x='algo_id', y='mean', data=df, hue='map_name', style="map_name", lw=4, markers=["s"]*2, dashes=[""]*2, markersize=12, palette=color)
handles, labels = ax.get_legend_handles_labels()
# breakpoint()
ax.legend(handles=handles[:], labels=labels[:], loc='lower right', ncol=1, prop={'size': 30}, markerscale=1.5)
# for h in ax.legend_.legendHandles:
for h in ax.legend_.legend_handles:
    h.set_linewidth(2.5)

plt.ylabel('LLM Iters', fontsize=fontsize, labelpad=10)
plt.xlabel('Round', fontsize=fontsize, labelpad=10)

plt.xticks(fontsize=fontsize)
# llm iter
plt.ylim((0.5, 20.5))
plt.yticks([1, 5, 10, 15, 20], fontsize=fontsize)
# health
# plt.ylim((-0.5, 12))
# plt.yticks([0, 4, 8, 12], fontsize=fontsize)
# time
# plt.ylim((2, 18))
# plt.yticks([2, 6, 10, 14,18], fontsize=fontsize)
plt.xlim((0.5, 3.5))
plt.xticks([1, 2, 3], fontsize=fontsize)

# sns.despine()

i = 0
num_hues = len(np.unique(df['map_name']))
for (hue, df_hue), dogde_dist in zip(df.groupby('map_name', sort=False), np.linspace(0, 0, 2 * num_hues + 1)[1::2]):
    # bars = ax.errorbar(data=df_hue, x='algo_id', y='mean', yerr='std')
    # xys = bars.lines[0].get_xydata()
    # bars.remove()
    # ax.errorbar(data=df_hue, x=xys[:, 0] + dogde_dist, y='mean', yerr='std', ls='', lw=3, capsize=6, color=color[i])
    i += 1

plt.savefig('llm_iters.pdf', format='pdf', bbox_inches='tight')
