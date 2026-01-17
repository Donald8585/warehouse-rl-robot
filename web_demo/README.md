---
title: Warehouse Robot RL Navigation
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.40.1
app_file: app.py
pinned: false
license: mit
---

# 🤖 Warehouse Robot Navigation | DQN + HER + Curriculum Learning

**Interactive demo comparing BFS pathfinding vs. Deep Reinforcement Learning for warehouse robot navigation**

## 🎯 Project Overview

This demo showcases a **Deep Q-Network (DQN) agent with Hindsight Experience Replay (HER)** trained using **curriculum learning** to navigate a 20×20 grid warehouse environment with obstacles.

### Key Features
- **30 comparison videos** (6 difficulty levels × 5 runs each)
- **Side-by-side visualization**: BFS optimal pathfinding (blue) vs. RL agent (green)
- **Curriculum learning**: Progressive difficulty (Easy → Medium → Hard)
- **Sparse reward challenge**: Agent learns to reach goals with only terminal rewards

## 📊 Results Summary

| Difficulty | Obstacle Density | RL Success Rate |
|------------|-----------------|----------------|
| 🟢 Tutorial | 0% | **100%** ✅ |
| 🔵 Easy | 10% | **80%** ✅ |
| 🟡 Medium | 25% | **60%** 😐 |
| 🟠 Hard | 40% | **20%** ⚠️ |
| 🔴 Expert | 55% | **0%** ❌ |
| ⚫ Nightmare | 70% | **0%** ❌ |

## 🧠 Technical Details

### Environment
- **State Space**: Agent position (x, y) + Goal position (x, y) [4D continuous]
- **Action Space**: Up, Right, Down, Left [4 discrete actions]
- **Reward**: Sparse (+0 at goal, -1 per step)
- **Episode Limit**: 200 steps
- **Grid Size**: 20×20

### Training
- **Algorithm**: DQN with Hindsight Experience Replay (HER)
- **Curriculum**: 3 stages @ 100k steps each (300k total)
  - Stage 1: Easy (10% density, distance 5-8)
  - Stage 2: Medium (25% density, distance 8-12)
  - Stage 3: Hard (40% density, distance 12-16)
- **Hyperparameters**:
  - Learning rate: 1e-3
  - Batch size: 256
  - Replay buffer: 100k transitions
  - HER strategy: Future (4 sampled goals per transition)

### Results Analysis
- ✅ **Curriculum learning effective**: 100% success on tutorial, 80% on easy
- 😐 **Generalization gap**: Performance degrades on harder difficulties
- ⚠️ **Sparse reward challenge**: Agent struggles with long-horizon credit assignment
- 💡 **Future work**: Reward shaping, prioritized replay, or hierarchical RL

## 🚀 How to Use

1. **Select difficulty level**: Tutorial → Nightmare (increasing obstacle density)
2. **Choose run number**: 1-5 (different random maps per level)
3. **Click "Load Video"**: Watch BFS (left/blue) vs RL (right/green)
4. **Compare performance**: Success rates and step counts displayed

## 🔧 Tech Stack

- **Gymnasium**: Custom environment framework
- **Stable-Baselines3**: DQN + HER implementation
- **NumPy**: State/reward processing
- **imageio**: Video generation
- **Streamlit**: Interactive web interface

## 🔗 Links

- **Portfolio**: [alfredso.com/portfolio](https://alfredso.com/portfolio)
- **GitHub**: [github.com/Donald8585/warehouse-rl-robot](https://github.com/Donald8585/warehouse-rl-robot)
- **LinkedIn**: [linkedin.com/in/alfred-so](https://www.linkedin.com/in/alfred-so/)
- **Kaggle**: [kaggle.com/sword4949](https://www.kaggle.com/sword4949)

## 📝 License

MIT License - Free to use for learning and portfolio projects

---

*Built with ❤️ by Alfred So | MSc Data Science & AI (HSUHK) | Aspiring ML Engineer*
