# Warehouse Robot Navigation | RL Simulation

**Interactive demo for warehouse robot navigation with reinforcement learning. Simulated 2D environment where a mobile robot learns to reach goals while avoiding obstacles using PPO algorithm.**

## 🎯 Project Overview

- **Environment**: 2D grid warehouse with random obstacles
- **State**: 16-ray lidar-like scan + relative goal vector (18 features)
- **Actions**: Forward, Left, Right, Stop
- **Algorithm**: Proximal Policy Optimization (PPO) via Stable-Baselines3
- **Goal**: Learn collision-free navigation to randomly placed goals

## 📁 Project Structure

```
warehouse-rl-robot/
├── README.md
├── requirements.txt
├── setup_project.sh          # Folder setup script
├── env/                       # Future: Gazebo worlds, robot models
├── src/
│   ├── gym_env/
│   │   └── warehouse_env.py  # Custom Gymnasium environment
│   └── rl/
│       ├── train_ppo.py      # PPO training script
│       └── eval_policy.py    # Policy evaluation + video export
├── web_demo/
│   ├── app.py                # Gradio web interface (coming soon)
│   └── videos/               # Exported episode recordings
├── docker/                    # Docker setup (optional)
├── models/                    # Saved trained models
└── tb_logs/                   # TensorBoard logs
```

## 🚀 Setup

### 1. Create folder structure (Windows Git Bash)

```bash
cd "C:/Users/logos/OneDrive/文件/GitHub"
bash setup_project.sh
```

### 2. Install dependencies

```bash
cd warehouse-rl-robot
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
```

## 🏃 Training

Train the PPO agent for 500K timesteps:

```bash
cd src
python -m rl.train_ppo
```

**Training output:**
- Model saved to: `models/ppo_warehouse.zip`
- TensorBoard logs: `tb_logs/warehouse_ppo/`

View training progress:
```bash
tensorboard --logdir=tb_logs/
```

## 📹 Evaluation & Video Export

Generate evaluation videos:

```bash
cd src
python -m rl.eval_policy
```

**Output:** MP4 videos saved to `web_demo/videos/`
- `easy_rl.mp4`
- `medium_rl.mp4`
- `hard_rl.mp4`

## 🌐 Web Demo (Coming Soon)

A Gradio web interface will be added to:
- Select difficulty level (easy/medium/hard)
- Compare RL policy vs. heuristic baseline
- View live episode playback
- Display success metrics

Deploy on HuggingFace Spaces and embed in portfolio site.

## 📊 Performance Metrics

After training, the agent typically achieves:
- **Success rate**: 70-85% (reaching goal before timeout)
- **Collision rate**: <15%
- **Average steps to goal**: 40-60 (vs. 200 max)

## 🔧 Tech Stack

- **Python 3.10+**
- **Gymnasium** - RL environment framework
- **Stable-Baselines3** - PPO implementation
- **NumPy** - State/observation processing
- **imageio** - Video export
- **TensorBoard** - Training visualization

## 🎓 Key Concepts Demonstrated

- Custom Gymnasium environment creation
- Lidar-like sensor simulation
- Discrete action space navigation
- PPO hyperparameter tuning
- Episode recording and visualization
- Reproducible ML project structure

## 🚧 Future Extensions

- [ ] Add heuristic baseline for comparison
- [ ] Integrate ROS2 + Gazebo for 3D simulation
- [ ] Implement continuous action space
- [ ] Add multi-goal navigation tasks
- [ ] Deploy Gradio web demo on HuggingFace Spaces
- [ ] Add Docker containerization

## 📝 License

MIT License - feel free to use for learning and portfolio projects

## 🔗 Links

- **Portfolio**: https://alfredso.com/portfolio
- **GitHub**: https://github.com/Donald8585/warehouse-rl-robot
- **Live Demo**: (Coming soon)

---

*Part of Alfred So's ML portfolio showcasing production-ready RL systems*
