# 🤖 Warehouse Robot Navigation | DQN + HER + Curriculum Learning

[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/Donald8585/warehouse-robot-navigation)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/Donald8585/warehouse-rl-robot)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org/)
[![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-DQN-orange)](https://stable-baselines3.readthedocs.io/)

Deep Reinforcement Learning agent using **DQN with Hindsight Experience Replay (HER)** trained through **curriculum learning** across 6 difficulty levels. Side-by-side video comparison demonstrates BFS optimal pathfinding vs. trained RL agent performance.

<p align="center">
  <img src="https://img.shields.io/badge/Success%20Rate-100%25%20Easy-brightgreen" alt="Easy Success"/>
  <img src="https://img.shields.io/badge/Success%20Rate-20%25%20Medium-yellow" alt="Medium Success"/>
  <img src="https://img.shields.io/badge/Training-300K%20Steps-blue" alt="Training Steps"/>
</p>

---

## 🎯 Key Features

- ✅ **Curriculum Learning**: 300k training steps across 3 progressive stages (Easy → Medium → Hard)
- ✅ **DQN with Hindsight Experience Replay**: Efficient learning in sparse reward environments
- ✅ **6 Difficulty Levels**: 0-70% obstacle density, variable goal distances (3-22 grid units)
- ✅ **Real-time Video Comparison**: BFS optimal path (LEFT/BLUE) vs. RL agent (RIGHT/GREEN)
- ✅ **Path Validation System**: BFS pre-check ensures all maps are solvable
- ✅ **Interactive Streamlit UI**: 30 comparison videos (5 runs × 6 difficulties)
- ✅ **Deployed on HuggingFace Spaces**: Free CPU-tier hosting with zero operational cost

---

## 📊 Performance Results

| Difficulty | Obstacle Density | Distance | RL Success Rate | BFS Success Rate |
|-----------|------------------|----------|-----------------|------------------|
| 🟢 Tutorial | 0% | 3-5 | **100%** ✅ | 100% |
| 🔵 Easy | 10% | 5-8 | **100%** ✅ | 100% |
| 🟡 Medium | 25% | 8-12 | **20%** ⚠️ | 100% |
| 🟠 Hard | 40% | 12-16 | **0%** ❌ | 100% |
| 🔴 Expert | 55% | 14-18 | **0%** ❌ | 100% |
| ⚫ Nightmare | 70% | 16-22 | **0%** ❌ | 100% |

**Key Insights:**
- ✅ **Perfect performance on simpler tasks** - Agent mastered Tutorial and Easy levels
- ⚠️ **Limited generalization** - Struggles with higher obstacle density (40%+)
- 📉 **Sparse rewards challenge** - Only 1/5 Medium runs succeeded
- 🎯 **BFS baseline demonstrates optimal performance** across all difficulties

---

## 🛠️ Tech Stack

**Reinforcement Learning:**
- Stable Baselines3 (DQN + HER implementation)
- Gymnasium (custom grid environment)
- NumPy (grid-based simulation)

**Training Infrastructure:**
- Kaggle T4 GPU (~1 hour training time)
- 300k total timesteps (100k per stage)
- Episode limit: 200 steps

**Deployment:**
- Streamlit (interactive web UI)
- ImageIO (video generation)
- HuggingFace Spaces (free CPU hosting)

---

## 📁 Project Structure

```
warehouse-rl-robot/
├── rl-warehouse.ipynb          # 🎓 Main Kaggle notebook (training + evaluation)
├── web_demo/
│   ├── app.py                  # Streamlit web interface
│   └── videos/                 # 30 comparison videos (5 runs × 6 levels)
│       ├── tutorial_run01_BFSvsRL.mp4
│       ├── easy_run01_BFSvsRL.mp4
│       └── ...
├── requirements.txt
└── README.md
```

**Workflow:**
1. **Train on Kaggle** → `rl-warehouse.ipynb` (DQN+HER curriculum learning)
2. **Generate videos** → Output 30 comparison videos
3. **Deploy to HF Spaces** → `web_demo/` folder with Streamlit UI

---

## 🚀 Quick Start

### 1. View Live Demo

👉 **[Try it now on HuggingFace Spaces](https://huggingface.co/spaces/Donald8585/warehouse-robot-navigation)** 👈

### 2. Train Your Own Agent (Kaggle)

**Open the notebook:**
```
rl-warehouse.ipynb
```

**What it does:**
- 🏗️ Defines custom Gymnasium environment (20×20 grid)
- 🧠 Trains DQN+HER agent with curriculum learning
- 📹 Generates side-by-side BFS vs RL comparison videos
- 💾 Outputs 30 videos for web demo

**Training time:** ~1 hour on Kaggle T4 GPU (free tier)

### 3. Run Web Demo Locally

```bash
cd web_demo
streamlit run app.py
```

Select difficulty level and run number to watch BFS vs RL comparisons!

---

## 🎮 Environment Details

### State Space (4 features)
- Agent position: `(x, y)` coordinates
- Goal position: `(goal_x, goal_y)` coordinates
- Grid size: 20×20 cells

### Action Space (Discrete: 4 actions)
- `0`: Move Up
- `1`: Move Right
- `2`: Move Down
- `3`: Move Left

### Reward Structure
- **Goal reached**: `+0` (sparse reward)
- **All other steps**: `-1` (time penalty)
- Episode terminates at goal or after 200 steps

### Difficulty Configuration

```python
DIFFICULTIES = {
    "tutorial": {"obstacle_pct": 0.0, "min_dist": 3, "max_dist": 5},
    "easy": {"obstacle_pct": 0.10, "min_dist": 5, "max_dist": 8},
    "medium": {"obstacle_pct": 0.25, "min_dist": 8, "max_dist": 12},
    "hard": {"obstacle_pct": 0.40, "min_dist": 12, "max_dist": 16},
    "expert": {"obstacle_pct": 0.55, "min_dist": 14, "max_dist": 18},
    "nightmare": {"obstacle_pct": 0.70, "min_dist": 16, "max_dist": 22}
}
```

**Safety Zones:** 7×7 clearance around start and goal positions to ensure navigability.

---

## 💡 Technical Highlights

### 1. Hindsight Experience Replay (HER)
```python
model = DQN(
    "MlpPolicy",
    env,
    replay_buffer_class=HerReplayBuffer,
    replay_buffer_kwargs=dict(
        n_sampled_goal=4,
        goal_selection_strategy="future"
    )
)
```
HER enables learning from failed episodes by treating achieved states as alternative goals.

### 2. Curriculum Learning
Progressive training across difficulty levels prevents catastrophic forgetting:
- **Stage 1**: Master easy navigation (0-10% obstacles) - 100k steps
- **Stage 2**: Handle moderate complexity (25% obstacles) - 100k steps
- **Stage 3**: Attempt high difficulty (40% obstacles) - 100k steps

### 3. Path Validation
```python
def is_solvable(grid, start, goal):
    return bfs_path_exists(grid, start, goal)
```
BFS pre-validation ensures all generated maps have valid solutions.

### 4. Side-by-Side Comparison
- **LEFT (Blue tint)**: BFS optimal algorithm
- **RIGHT (Green tint)**: Trained RL agent
- Synchronized obstacle maps for fair evaluation

---

## 🔬 Challenges & Insights

### ✅ What Worked
- Curriculum learning enabled 100% success on Tutorial/Easy levels
- HER significantly improved sample efficiency with sparse rewards
- Path validation prevented impossible maze configurations
- Side-by-side visualization clearly demonstrates algorithm differences

### ⚠️ Limitations
- **Poor generalization to unseen complexity** - Agent fails on 40%+ obstacle density
- **Sample inefficiency at higher difficulties** - 300k steps insufficient for Hard+ levels
- **Sparse reward challenge** - Agent struggles to explore effectively in complex mazes

### 🔮 Future Improvements
- [ ] Implement reward shaping (distance to goal, collision penalties)
- [ ] Extend curriculum learning to 500k+ steps
- [ ] Add exploration bonuses (curiosity-driven learning)
- [ ] Test alternative algorithms (PPO, SAC, Rainbow DQN)
- [ ] Implement continuous action space for smoother navigation

---

## 🎓 Key Concepts Demonstrated

- ✅ Deep Reinforcement Learning (DQN)
- ✅ Hindsight Experience Replay (HER)
- ✅ Curriculum Learning
- ✅ Custom Gymnasium Environment
- ✅ Sparse Reward Environments
- ✅ Algorithm Comparison (RL vs Classical)
- ✅ Video Visualization
- ✅ Production Deployment (HuggingFace Spaces)
- ✅ Honest Performance Reporting

---

## 🌐 Live Demo

**Try it yourself:** [https://huggingface.co/spaces/Donald8585/warehouse-robot-navigation](https://huggingface.co/spaces/Donald8585/warehouse-robot-navigation)

**Features:**
- Select difficulty level (Tutorial → Nightmare)
- Choose run number (1-5 different random seeds)
- Watch side-by-side BFS vs RL comparison
- View real-time success metrics

**Embed in your site:**
```html
<iframe 
    src="https://donald8585-warehouse-robot-navigation.hf.space" 
    width="100%" 
    height="800"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>
```

---

## 📝 Citation

If you use this project in your research or work, please cite:

```bibtex
@software{so2026warehouse,
  author = {So, Chit Wai Alfred},
  title = {Warehouse Robot Navigation with DQN+HER+Curriculum Learning},
  year = {2026},
  url = {https://github.com/Donald8585/warehouse-rl-robot}
}
```

---

## 📜 License

MIT License - feel free to use for learning and portfolio projects.

---

## 🔗 Connect

**Portfolio:** [https://alfredso.com/portfolio](https://alfredso.com/portfolio)  
**GitHub:** [https://github.com/Donald8585](https://github.com/Donald8585)  
**LinkedIn:** [https://linkedin.com/in/alfred-so](https://linkedin.com/in/alfred-so)  
**Kaggle:** [https://www.kaggle.com/sword4949](https://www.kaggle.com/sword4949)

---

<p align="center">
  <i>Part of Alfred So's ML portfolio showcasing production-ready RL systems</i><br>
  <i>MSc Data Science & AI | Hong Kong</i>
</p>

<p align="center">
  Made with ❤️ and 🤖 by <a href="https://github.com/Donald8585">Alfred So</a>
</p>
