#!/usr/bin/env bash
set -e

# Navigate to GitHub directory
cd "C:/Users/logos/OneDrive/文件/GitHub"

# Create project directory
PROJECT_NAME="warehouse-rl-robot"
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"

# Create folder structure
mkdir -p env
mkdir -p src/gym_env
mkdir -p src/rl
mkdir -p web_demo/videos
mkdir -p docker
mkdir -p models
mkdir -p tb_logs

# Move files from root to respective folders
echo "Moving files to appropriate folders..."

# Move gym environment
if [ -f "../warehouse_env.py" ]; then
    mv ../warehouse_env.py src/gym_env/
fi

# Move RL scripts
if [ -f "../train_ppo.py" ]; then
    mv ../train_ppo.py src/rl/
fi

if [ -f "../eval_policy.py" ]; then
    mv ../eval_policy.py src/rl/
fi

# Move web demo
if [ -f "../app.py" ]; then
    mv ../app.py web_demo/
fi

# Create __init__.py files for Python packages
touch src/__init__.py
touch src/gym_env/__init__.py
touch src/rl/__init__.py

echo ""
echo "✅ Project structure created at: $(pwd)"
echo ""
echo "📁 Folder structure:"
echo "   warehouse-rl-robot/"
echo "   ├── README.md"
echo "   ├── requirements.txt"
echo "   ├── setup_project.sh"
echo "   ├── env/"
echo "   ├── src/"
echo "   │   ├── gym_env/"
echo "   │   │   └── warehouse_env.py"
echo "   │   └── rl/"
echo "   │       ├── train_ppo.py"
echo "   │       └── eval_policy.py"
echo "   ├── web_demo/"
echo "   │   ├── app.py"
echo "   │   └── videos/"
echo "   ├── docker/"
echo "   ├── models/"
echo "   └── tb_logs/"
echo ""
echo "🚀 Next steps:"
echo "   1. cd warehouse-rl-robot"
echo "   2. python -m venv .venv"
echo "   3. source .venv/Scripts/activate"
echo "   4. pip install -r requirements.txt"
echo "   5. cd src && python -m rl.train_ppo"
