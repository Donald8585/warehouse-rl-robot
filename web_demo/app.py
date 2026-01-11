import streamlit as st
import os

st.set_page_config(
    page_title="Warehouse Robot Navigation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Warehouse Robot Navigation | RL Simulation")

st.markdown("""
**Trained PPO agent navigating a 2D warehouse environment with obstacles.**

- **State**: 16-ray lidar scan + relative goal vector
- **Actions**: Forward, Left, Right, Stop
- **Goal**: Reach green target while avoiding gray obstacles
- **Agent**: Blue square
""")

# Difficulty selector
difficulty = st.selectbox(
    "🎯 Select Difficulty Level",
    ["Easy", "Medium", "Hard"],
    help="Different obstacle layouts and goal positions"
)

# Video mapping
videos = {
    "Easy": "videos/easy_rl.mp4",
    "Medium": "videos/medium_rl.mp4",
    "Hard": "videos/hard_rl.mp4"
}

# Display video
video_path = videos[difficulty]
if os.path.exists(video_path):
    st.video(video_path)
else:
    st.error(f"Video not found: {video_path}")

# Training details
st.markdown("---")
st.markdown("### 📊 Training Details")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Algorithm", "PPO")
with col2:
    st.metric("Training Steps", "500,000")
with col3:
    st.metric("Parallel Envs", "8")
with col4:
    st.metric("Episode Limit", "200")

# Links
st.markdown("---")
st.markdown("""
### 🔗 Links
- [GitHub Repository](https://github.com/Donald8585/warehouse-rl-robot)
- [Portfolio](https://alfredso.com/portfolio)
""")
