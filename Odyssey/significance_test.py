import numpy as np
from scipy.stats import ttest_ind_from_stats

data = {
    "Table S1": {
        "Zombie": {"Round 1": {"mean": 12.7, "std": 2.8, "nobs": 3}, "Round 2": {"mean": 9.1, "std": 2.1, "nobs": 3}, "Round 3": {"mean": 3.4, "std": 1.8, "nobs": 3}},
        "Spider": {"Round 1": {"mean": 12.7, "std": 2.5, "nobs": 3}, "Round 2": {"mean": 9.2, "std": 1.3, "nobs": 3}, "Round 3": {"mean": 7.3, "std": 1.9, "nobs": 3}},
        "Skeleton": {"Round 1": {"mean": 13.6, "std": 0.5, "nobs": 3}, "Round 2": {"mean": 9.5, "std": 4.7, "nobs": 3}, "Round 3": {"mean": 2.5, "std": 1.5, "nobs": 3}},
        "Enderman": {"Round 1": {"mean": 14.7, "std": 3.4, "nobs": 3}, "Round 2": {"mean": 7.9, "std": 1.1, "nobs": 3}, "Round 3": {"mean": 4.5, "std": 0.3, "nobs": 3}},
    },
    "Table S2": {
        "DEPS with GPT4-o": {
            "# Distinct Items Obtained": {"mean": 13.0, "std": 1.4, "nobs": 3},
            "Distance Traveled": {"mean": 1108.4, "std": 711.7, "nobs": 3},
            "# Items Crafted": {"mean": 25.0, "std": 7.9, "nobs": 3},
            "# R&A Unlocked": {"mean": 42.0, "std": 7.5, "nobs": 3}
        },
        "Voyager with GPT-3.5-Turbo": {
            "# Distinct Items Obtained": {"mean": 3.3, "std": 2.0, "nobs": 3},
            "Distance Traveled": {"mean": 2625.0, "std": 1284.9, "nobs": 3},
            "# Items Crafted": {"mean": 30.0, "std": 27.3, "nobs": 3},
            "# R&A Unlocked": {"mean": 17.3, "std": 9.7, "nobs": 3}
        },
        "Voyager with GPT-4o-mini": {
            "# Distinct Items Obtained": {"mean": 17.7, "std": 2.5, "nobs": 3},
            "Distance Traveled": {"mean": 1616.7, "std": 898.2, "nobs": 3},
            "# Items Crafted": {"mean": 71.7, "std": 23.5, "nobs": 3},
            "# R&A Unlocked": {"mean": 75.7, "std": 14.4, "nobs": 3}
        },
        "ReAct with GPT-4o-mini": {
            "# Distinct Items Obtained": {"mean": 10.0, "std": 5.1, "nobs": 3},
            "Distance Traveled": {"mean": 758.8, "std": 323.0, "nobs": 3},
            "# Items Crafted": {"mean": 171.3, "std": 23.5, "nobs": 3},
            "# R&A Unlocked": {"mean": 78.0, "std": 34.0, "nobs": 3}
        },
        "AutoGPT with GPT-4o-mini": {
            "# Distinct Items Obtained": {"mean": 15.3, "std": 5.7, "nobs": 3},
            "Distance Traveled": {"mean": 2324.2, "std": 304.1, "nobs": 3},
            "# Items Crafted": {"mean": 142.7, "std": 129.7, "nobs": 3},
            "# R&A Unlocked": {"mean": 128.7, "std": 12.5, "nobs": 3}
        },
        "Odyssey with LLaMA3-8B": {
            "# Distinct Items Obtained": {"mean": 23.3, "std": 5.6, "nobs": 3},
            "Distance Traveled": {"mean": 1287.3, "std": 229.2, "nobs": 3},
            "# Items Crafted": {"mean": 126.0, "std": 60.1, "nobs": 3},
            "# R&A Unlocked": {"mean": 145.3, "std": 35.1, "nobs": 3}
        },
        "Odyssey with MineMA3-8B w/o Planner": {
            "# Distinct Items Obtained": {"mean": 5.7, "std": 5.3, "nobs": 3},
            "Distance Traveled": {"mean": 105.0, "std": 53.9, "nobs": 3},
            "# Items Crafted": {"mean": 18.7, "std": 18.0, "nobs": 3},
            "# R&A Unlocked": {"mean": 49.0, "std": 45.7, "nobs": 3}
        },
        "Odyssey with MineMA3-8B w/o Skill Library": {
            "# Distinct Items Obtained": {"mean": 3.7, "std": 0.9, "nobs": 3},
            "Distance Traveled": {"mean": 732.9, "std": 234.4, "nobs": 3},
            "# Items Crafted": {"mean": 38.0, "std": 20.0, "nobs": 3},
            "# R&A Unlocked": {"mean": 31.7, "std": 2.4, "nobs": 3}
        },
        "Odyssey with MineMA3-8B": {
            "# Distinct Items Obtained": {"mean": 36.7, "std": 2.0, "nobs": 3},
            "Distance Traveled": {"mean": 2524.7, "std": 703.4, "nobs": 3},
            "# Items Crafted": {"mean": 378.7, "std": 156.8, "nobs": 3},
            "# R&A Unlocked": {"mean": 180.0, "std": 8.3, "nobs": 3}
        },
    },
    "Table 3": {
        "1 zombie": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 3/3, "Health": {"mean": 20.0, "std": 0.0, "nobs": 3}, "Time (min)": {"mean": 9.9, "std": 6.0, "nobs": 3}, "# LLM Iters": {"mean": 67.3, "std": 41.7, "nobs": 3}},
            "LLaMA-3-8B": {"Success Rate": 4/8, "Health": {"mean": 20.0, "std": 0.0, "nobs": 4}, "Time (min)": {"mean": 8.3, "std": 4.2, "nobs": 4}, "# LLM Iters": {"mean": 6.1, "std": 4.1, "nobs": 4}},
            "MineMA-8B": {"Success Rate": 8/8, "Health": {"mean": 19.4, "std": 2.3, "nobs": 8}, "Time (min)": {"mean": 8.8, "std": 5.4, "nobs": 8}, "# LLM Iters": {"mean": 10.0, "std": 5.8, "nobs": 8}}
        },
        "1 spider": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 3/3, "Health": {"mean": 10.8, "std": 8.0, "nobs": 3}, "Time (min)": {"mean": 9.4, "std": 8.8, "nobs": 3}, "# LLM Iters": {"mean": 19.0, "std": 1.4, "nobs": 3}},
            "LLaMA-3-8B": {"Success Rate": 4/8, "Health": {"mean": 19.4, "std": 1.0, "nobs": 4}, "Time (min)": {"mean": 12.1, "std": 3.8, "nobs": 4}, "# LLM Iters": {"mean": 8.4, "std": 3.5, "nobs": 4}},
            "MineMA-8B": {"Success Rate": 8/8, "Health": {"mean": 19.3, "std": 1.6, "nobs": 8}, "Time (min)": {"mean": 8.3, "std": 6.7, "nobs": 8}, "# LLM Iters": {"mean": 15.2, "std": 6.0, "nobs": 8}}
        },
        "1 skeleton": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 16.5, "std": 0.0, "nobs": 2}, "Time (min)": {"mean": 7.4, "std": 2.9, "nobs": 2}, "# LLM Iters": {"mean": 46.0, "std": 32.0, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 4/8, "Health": {"mean": 17.6, "std": 2.7, "nobs": 4}, "Time (min)": {"mean": 8.1, "std": 3.5, "nobs": 4}, "# LLM Iters": {"mean": 8.9, "std": 3.7, "nobs": 4}},
            "MineMA-8B": {"Success Rate": 8/8, "Health": {"mean": 13.6, "std": 5.9, "nobs": 8}, "Time (min)": {"mean": 8.6, "std": 7.3, "nobs": 8}, "# LLM Iters": {"mean": 12.1, "std": 7.0, "nobs": 8}}
        },
        "1 zombified piglin": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 3/3, "Health": {"mean": 19.0, "std": 1.4, "nobs": 3}, "Time (min)": {"mean": 14.5, "std": 4.7, "nobs": 3}, "# LLM Iters": {"mean": 50.3, "std": 26.2, "nobs": 3}},
            "LLaMA-3-8B": {"Success Rate": 4/8, "Health": {"mean": 19.9, "std": 0.4, "nobs": 4}, "Time (min)": {"mean": 9.2, "std": 3.9, "nobs": 4}, "# LLM Iters": {"mean": 10.0, "std": 4.2, "nobs": 4}},
            "MineMA-8B": {"Success Rate": 8/8, "Health": {"mean": 18.7, "std": 1.9, "nobs": 8}, "Time (min)": {"mean": 8.5, "std": 6.1, "nobs": 8}, "# LLM Iters": {"mean": 11.7, "std": 6.2, "nobs": 8}}
        },
        "1 enderman": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 11.0, "std": 9.0, "nobs": 2}, "Time (min)": {"mean": 22.8, "std": 1.7, "nobs": 2}, "# LLM Iters": {"mean": 28.0, "std": 4.0, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 2/8, "Health": {"mean": 15.1, "std": 7.3, "nobs": 2}, "Time (min)": {"mean": 13.0, "std": 3.0, "nobs": 2}, "# LLM Iters": {"mean": 6.8, "std": 1.9, "nobs": 2}},
            "MineMA-8B": {"Success Rate": 4/8, "Health": {"mean": 19.8, "std": 0.5, "nobs": 4}, "Time (min)": {"mean": 10.4, "std": 6.3, "nobs": 4}, "# LLM Iters": {"mean": 12.5, "std": 5.4, "nobs": 4}}
        },
        "1 zombie, 1 spider": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 1/3, "Health": {"mean": 17.5, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 5.9, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 21.0, "std": 0.0, "nobs": 1}},
            "LLaMA-3-8B": {"Success Rate": 1/8, "Health": {"mean": 20.0, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 8.5, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 6.0, "std": 0.0, "nobs": 1}},
            "MineMA-8B": {"Success Rate": 5/8, "Health": {"mean": 16.4, "std": 4.1, "nobs": 5}, "Time (min)": {"mean": 10.6, "std": 6.7, "nobs": 5}, "# LLM Iters": {"mean": 12.0, "std": 4.9, "nobs": 5}}
        },
        "1 zombie, 1 skeleton": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 19.0, "std": 1.0, "nobs": 2}, "Time (min)": {"mean": 15.0, "std": 8.6, "nobs": 2}, "# LLM Iters": {"mean": 40.5, "std": 20.5, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 1/8, "Health": {"mean": 0.2, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 13.5, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 9.0, "std": 0.0, "nobs": 1}},
            "MineMA-8B": {"Success Rate": 3/8, "Health": {"mean": 12.8, "std": 2.8, "nobs": 3}, "Time (min)": {"mean": 14.0, "std": 1.9, "nobs": 3}, "# LLM Iters": {"mean": 10.3, "std": 2.8, "nobs": 3}}
        },
        "3 zombies": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 7.8, "std": 4.2, "nobs": 2}, "Time (min)": {"mean": 8.2, "std": 0.4, "nobs": 2}, "# LLM Iters": {"mean": 61.0, "std": 29.0, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 1/8, "Health": {"mean": 3.7, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 14.3, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 8.0, "std": 0.0, "nobs": 1}},
            "MineMA-8B": {"Success Rate": 1/8, "Health": {"mean": 5.2, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 11.1, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 14.0, "std": 0.0, "nobs": 1}}
        },
        "1 zombie villager": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 20.0, "std": 0.0, "nobs": 2}, "Time (min)": {"mean": 12.6, "std": 2.0, "nobs": 2}, "# LLM Iters": {"mean": 50.0, "std": 3.0, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 7/8, "Health": {"mean": 19.6, "std": 1.1, "nobs": 7}, "Time (min)": {"mean": 12.7, "std": 5.3, "nobs": 7}, "# LLM Iters": {"mean": 11.0, "std": 5.3, "nobs": 7}},
            "MineMA-8B": {"Success Rate": 8/8, "Health": {"mean": 20.0, "std": 0.0, "nobs": 8}, "Time (min)": {"mean": 9.0, "std": 3.6, "nobs": 8}, "# LLM Iters": {"mean": 12.8, "std": 6.1, "nobs": 8}}
        },
        "1 cave spider": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 2/3, "Health": {"mean": 16.5, "std": 3.5, "nobs": 2}, "Time (min)": {"mean": 10.0, "std": 1.8, "nobs": 2}, "# LLM Iters": {"mean": 79.2, "std": 29.0, "nobs": 2}},
            "LLaMA-3-8B": {"Success Rate": 6/8, "Health": {"mean": 19.5, "std": 1.2, "nobs": 6}, "Time (min)": {"mean": 12.0, "std": 6.3, "nobs": 6}, "# LLM Iters": {"mean": 19.5, "std": 1.2, "nobs": 6}},
            "MineMA-8B": {"Success Rate": 7/8, "Health": {"mean": 20.0, "std": 0.0, "nobs": 7}, "Time (min)": {"mean": 3.6, "std": 2.6, "nobs": 7}, "# LLM Iters": {"mean": 8.6, "std": 8.8, "nobs": 7}}
        },
        "1 wither skeleton": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 1/3, "Health": {"mean": 20.0, "std": 0.0, "nobs": 1}, "Time (min)": {"mean": 20.9, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 100.0, "std": 0.0, "nobs": 1}},
            "LLaMA-3-8B": {"Success Rate": 6/8, "Health": {"mean": 13.2, "std": 6.0, "nobs": 6}, "Time (min)": {"mean": 11.7, "std": 3.7, "nobs": 6}, "# LLM Iters": {"mean": 12.3, "std": 2.7, "nobs": 6}},
            "MineMA-8B": {"Success Rate": 7/8, "Health": {"mean": 17.3, "std": 3.7, "nobs": 7}, "Time (min)": {"mean": 11.0, "std": 6.8, "nobs": 7}, "# LLM Iters": {"mean": 12.6, "std": 6.9, "nobs": 7}}
        },
        "Cook Meat": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 0/3, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "LLaMA-3-8B": {"Success Rate": 1/8, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": 20.3, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 19.0, "std": 0.0, "nobs": 1}},
            "MineMA-8B": {"Success Rate": 2/8, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": 21.4, "std": 1.2, "nobs": 2}, "# LLM Iters": {"mean": 30.0, "std": 10.0, "nobs": 2}}
        },
        "Animal Husbandry": {
            "Voyager with GPT-4-o-mini": {"Success Rate": 1/3, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": 19.0, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 12.0, "std": 0.0, "nobs": 1}},
            "LLaMA-3-8B": {"Success Rate": 2/8, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": 15.3, "std": 7.6, "nobs": 2}, "# LLM Iters": {"mean": 31.0, "std": 4.0, "nobs": 2}},
            "MineMA-8B": {"Success Rate": 3/8, "Health": {"mean": np.nan, "std": np.nan, "nobs": 0}, "Time (min)": {"mean": 16.8, "std": 7.8, "nobs": 3}, "# LLM Iters": {"mean": 26.7, "std": 16.2, "nobs": 3}},
        }
    },
    "Table 4": {
        "Collect Seeds": {
            "Baichuan2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 1.8, "std": 1.4, "nobs": 2}, "# LLM Iters": {"mean": 3.0, "std": 2.8, "nobs": 2}},
            "Qwen2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 3.8, "std": 1.5, "nobs": 2}, "# LLM Iters": {"mean": 4.5, "std": 0.7, "nobs": 2}},
            "Qwen2-72B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 0.9, "std": 0.3, "nobs": 4}, "# LLM Iters": {"mean": 1.8, "std": 1.0, "nobs": 4}},
            "MineMA-8B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 1.3, "std": 1.4, "nobs": 5}, "# LLM Iters": {"mean": 1.4, "std": 0.9, "nobs": 5}},
            "MineMA-70B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 1.4, "std": 1.6, "nobs": 5}, "# LLM Iters": {"mean": 1.0, "std": 0.0, "nobs": 5}},
        },
        "Hoe Farmland": {
            "Baichuan2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 15.7, "std": 16.2, "nobs": 2}, "# LLM Iters": {"mean": 19.5, "std": 10.6, "nobs": 2}},
            "Qwen2-72B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 8.0, "std": 5.4, "nobs": 4}, "# LLM Iters": {"mean": 16.0, "std": 6.6, "nobs": 4}},
            "MineMA-8B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 17.2, "std": 14.7, "nobs": 2}, "# LLM Iters": {"mean": 26.5, "std": 9.2, "nobs": 2}},
            "MineMA-70B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 10.2, "std": 6.7, "nobs": 4}, "# LLM Iters": {"mean": 11.8, "std": 2.6, "nobs": 4}},
        },
        "Shear Sheep": {
            "Baichuan2-7B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 26.0, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 30.0, "std": 0.0, "nobs": 1}},
            "Qwen2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 11.0, "std": 2.8, "nobs": 2}, "# LLM Iters": {"mean": 10.8, "std": 1.5, "nobs": 2}},
            "Qwen2-72B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 6.3, "std": 0.3, "nobs": 2}, "# LLM Iters": {"mean": 10.0, "std": 4.2, "nobs": 2}},
            "MineMA-8B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 15.7, "std": 10.9, "nobs": 2}, "# LLM Iters": {"mean": 13.0, "std": 9.9, "nobs": 2}},
            "MineMA-70B": {"Success Rate": {"mean": 3/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 6.9, "std": 7.8, "nobs": 3}, "# LLM Iters": {"mean": 11.0, "std": 7.5, "nobs": 3}},
        },
        "Milk Cow": {
            "Baichuan2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-7B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 26.1, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 30.0, "std": 0.0, "nobs": 1}},
            "Qwen2-72B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 7.0, "std": 5.0, "nobs": 2}, "# LLM Iters": {"mean": 9.5, "std": 9.2, "nobs": 2}},
            "MineMA-8B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 7.2, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 7.0, "std": 0.0, "nobs": 1}},
            "MineMA-70B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 8.6, "std": 10.0, "nobs": 2}, "# LLM Iters": {"mean": 10.0, "std": 11.3, "nobs": 2}},
        },
        "Cook Meat": {
            "Baichuan2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-72B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 8.2, "std": 5.8, "nobs": 2}, "# LLM Iters": {"mean": 9.5, "std": 2.1, "nobs": 2}},
            "MineMA-8B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 25.6, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 38.0, "std": 0.0, "nobs": 1}},
            "MineMA-70B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 20.2, "std": 8.5, "nobs": 2}, "# LLM Iters": {"mean": 24.0, "std": 2.8, "nobs": 2}},
        },
        "Obtain Leather": {
            "Baichuan2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-7B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 14.9, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 16.0, "std": 0.0, "nobs": 1}},
            "Qwen2-72B": {"Success Rate": {"mean": 3/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 4.2, "std": 4.0, "nobs": 3}, "# LLM Iters": {"mean": 6.0, "std": 5.6, "nobs": 3}},
            "MineMA-8B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 15.0, "std": 8.7, "nobs": 4}, "# LLM Iters": {"mean": 17.8, "std": 15.2, "nobs": 4}},
            "MineMA-70B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 7.4, "std": 7.8, "nobs": 5}, "# LLM Iters": {"mean": 8.8, "std": 8.6, "nobs": 5}},
        },
        "Make Sugar": {
            "Baichuan2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 16.2, "std": 15.6, "nobs": 2}, "# LLM Iters": {"mean": 22.0, "std": 18.4, "nobs": 2}},
            "Qwen2-7B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 15.4, "std": 7.0, "nobs": 2}, "# LLM Iters": {"mean": 15.5, "std": 9.2, "nobs": 2}},
            "Qwen2-72B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 18.0, "std": 9.4, "nobs": 4}, "# LLM Iters": {"mean": 19.5, "std": 14.2, "nobs": 4}},
            "MineMA-8B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 4.3, "std": 1.9, "nobs": 5}, "# LLM Iters": {"mean": 7.0, "std": 1.9, "nobs": 5}},
            "MineMA-70B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 4.3, "std": 4.4, "nobs": 5}, "# LLM Iters": {"mean": 7.8, "std": 4.0, "nobs": 5}},
        },
        "Collect Water": {
            "Baichuan2-7B": {"Success Rate": {"mean": 0/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": np.nan, "std": np.nan, "nobs": 0}, "# LLM Iters": {"mean": np.nan, "std": np.nan, "nobs": 0}},
            "Qwen2-7B": {"Success Rate": {"mean": 1/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 10.0, "std": 0.0, "nobs": 1}, "# LLM Iters": {"mean": 10.0, "std": 0.0, "nobs": 1}},
            "Qwen2-72B": {"Success Rate": {"mean": 2/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 17.4, "std": 15.8, "nobs": 2}, "# LLM Iters": {"mean": 33.5, "std": 43.1, "nobs": 2}},
            "MineMA-8B": {"Success Rate": {"mean": 4/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 10.4, "std": 3.0, "nobs": 4}, "# LLM Iters": {"mean": 8.8, "std": 5.5, "nobs": 4}},
            "MineMA-70B": {"Success Rate": {"mean": 5/5, "std": 0, "nobs": 5}, "Time (min)": {"mean": 9.3, "std": 4.8, "nobs": 5}, "# LLM Iters": {"mean": 9.4, "std": 3.7, "nobs": 5}},
        },
    }
}

def ttest_from_stats(mean1, std1, mean2, std2, nobs1, nobs2):
    if nobs1 <= 1 and nobs2 <= 1:
        return np.nan
    t_stat, p_val = ttest_ind_from_stats(mean1=mean1, std1=std1, nobs1=nobs1,
                                         mean2=mean2, std2=std2, nobs2=nobs2)
    return p_val


def analyze_comparison(data, metrics, task_name):
    for metric in metrics:
        best_model = None
        second_best_model = None
        best_mean = None
        second_best_mean = None
        
        if (metric == "Time (min)") or (metric == "# LLM Iters"):
            best_mean = np.inf
            second_best_mean = np.inf
            for model, values in data.items():
                mean = values[metric]["mean"]
                if mean < best_mean:
                    second_best_mean = best_mean
                    second_best_model = best_model
                    best_mean = mean
                    best_model = model
                elif mean < second_best_mean:
                    second_best_mean = mean
                    second_best_model = model
        else:
            best_mean = -np.inf
            second_best_mean = -np.inf
            for model, values in data.items():
                mean = values[metric]["mean"]
                if mean > best_mean:
                    second_best_mean = best_mean
                    second_best_model = best_model
                    best_mean = mean
                    best_model = model
                elif mean > second_best_mean:
                    second_best_mean = mean
                    second_best_model = model

        if best_model and second_best_model:
            mean1, std1, nobs1 = data[best_model][metric]["mean"], data[best_model][metric]["std"], data[best_model][metric]["nobs"]
            mean2, std2, nobs2 = data[second_best_model][metric]["mean"], data[second_best_model][metric]["std"], data[second_best_model][metric]["nobs"]
            
            if not np.isnan(mean1) and not np.isnan(mean2):


                p_val = ttest_from_stats(mean1, std1, mean2, std2, nobs1, nobs2)
                if np.isnan(p_val):
                    print(f"{task_name} {metric} (comparing {best_model} with {second_best_model}): insufficient data")
                elif p_val < 0.05:
                    print(f"{task_name} {metric} (comparing {best_model} with {second_best_model}): p_val={p_val:.5f} implies statistical significance")
                else:
                    print(f"{task_name} {metric} (comparing {best_model} with {second_best_model}): p_val={p_val:.5f}")
        else:
            print(f"{task_name} {metric}: Insufficient data")


def analyze_comparison_with_ours(data, metrics, best_model, task_name):
    for metric in metrics:
        is_best = True
        best_mean = data[best_model][metric]["mean"]
        second_best_model = None
        second_best_mean = np.inf if ((metric == "Time (min)") or (metric == "# LLM Iters")) else -np.inf
        
        if (metric == "Time (min)") or (metric == "# LLM Iters"):
            for model, values in data.items():
                if model != best_model and values[metric]["mean"] < best_mean:
                    is_best = False
                    break
                if model != best_model and values[metric]["mean"] < second_best_mean:
                    second_best_mean = values[metric]["mean"]
                    second_best_model = model
        else:
            for model, values in data.items():
                if model != best_model and values[metric]["mean"] > best_mean:
                    is_best = False
                    break
                if model != best_model and values[metric]["mean"] > second_best_mean:
                    second_best_mean = values[metric]["mean"]
                    second_best_model = model

        if is_best and second_best_model:
            mean1, std1, nobs1 = data[best_model][metric]["mean"], data[best_model][metric]["std"], data[best_model][metric]["nobs"]
            mean2, std2, nobs2 = data[second_best_model][metric]["mean"], data[second_best_model][metric]["std"], data[second_best_model][metric]["nobs"]
            
            if not np.isnan(mean1) and not np.isnan(mean2):
                p_val = ttest_from_stats(mean1, std1, mean2, std2, nobs1, nobs2)
                if p_val < 0.05:
                    print(f"{task_name} {metric} (comparing {best_model} with {second_best_model}): p_val={p_val:.5f} implies statistical significance")
                else:
                    print(f"{task_name} {metric} (comparing {best_model} with {second_best_model}): p_val={p_val:.5f} implies no statistical significance")
        else:
            print(f"{task_name} {metric}: {best_model} is not the best model, no p-value calculation")

def analyze_table_r1(data_r1):
    for task, rounds in data_r1.items():
        comparisons = [
            ("Round 2 vs Round 1", "Round 1", "Round 2"),
            ("Round 3 vs Round 2", "Round 2", "Round 3"),
            ("Round 3 vs Round 1", "Round 1", "Round 3")
        ]
        
        for comparison, round1, round2 in comparisons:
            p_val = ttest_from_stats(
                rounds[round1]["mean"], rounds[round1]["std"],
                rounds[round2]["mean"], rounds[round2]["std"],
                rounds[round1]["nobs"], rounds[round2]["nobs"]
            )
            if p_val < 0.05:
                print(f"{task} {comparison}: p_val={p_val:.5f} implies statistical significance")
            else:
                print(f"{task} {comparison}: p_val={p_val:.5f} implies no statistical significance")

def analyze_table_r2(data_r2):
    metrics = ["# Distinct Items Obtained", "Distance Traveled", "# Items Crafted", "# R&A Unlocked"]
    best_model = "Odyssey with MineMA3-8B"
    analyze_comparison_with_ours(data_r2, metrics, best_model, "explore")

def analyze_table_r3(data_r3):
    metrics = ["Health", "Time (min)", "# LLM Iters"]
    
    for task_name, task_data in data_r3.items():
        analyze_comparison(task_data, metrics, task_name)

def analyze_table_r4(data_r4):
    metrics = ["Time (min)", "# LLM Iters"]
    
    for task_name, task_data in data_r4.items():
        analyze_comparison(task_data, metrics, task_name)

def main():
    analyze_table_r1(data["Table S1"])
    analyze_table_r2(data["Table S2"])
    analyze_table_r3(data["Table 3"])
    analyze_table_r4(data["Table 4"])

if __name__ == "__main__":
    main()
