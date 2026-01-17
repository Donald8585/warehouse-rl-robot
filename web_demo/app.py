import streamlit as st
import os

st.set_page_config(
    page_title="Warehouse Robot RL Navigation",
    page_icon="🤖",
    layout="wide"
)

difficulties = {
    "🟢 Tutorial": "tutorial",
    "🔵 Easy": "easy",
    "🟡 Medium": "medium",
    "🟠 Hard": "hard",
    "🔴 Expert": "expert",
    "⚫ Nightmare": "nightmare"
}

# ✅ UPDATED with actual training results
success_rates = {
    "tutorial": {"bfs": 100, "rl": 100},
    "easy": {"bfs": 100, "rl": 100},
    "medium": {"bfs": 100, "rl": 20},
    "hard": {"bfs": 100, "rl": 0},
    "expert": {"bfs": 100, "rl": 0},
    "nightmare": {"bfs": 100, "rl": 0},
}

# Header
st.title("🤖 Warehouse Robot Navigation | DQN + HER + Curriculum Learning")
st.markdown("**Side-by-side comparison of BFS pathfinding vs. Deep Reinforcement Learning agent**")
st.markdown("""
This demo showcases a **DQN agent with Hindsight Experience Replay (HER)** trained using **curriculum learning**
(300k steps across progressively harder environments). The agent navigates a 20×20 grid warehouse to reach goals while avoiding obstacles.
""")
st.divider()

# Main UI
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🎯 Select Environment")
    difficulty_display = st.selectbox(
        "Difficulty Level",
        options=list(difficulties.keys()),
        index=0
    )

    run = st.slider("Run Number (1-5)", 1, 5, 1)
    load_btn = st.button("▶️ Load Video", type="primary", use_container_width=True)

    st.divider()
    st.markdown("""
    ### 📚 Difficulty Levels
    - **🟢 Tutorial**: 0% obstacles, distance 3-5
    - **🔵 Easy**: 10% obstacles, distance 5-8
    - **🟡 Medium**: 25% obstacles, distance 8-12
    - **🟠 Hard**: 40% obstacles, distance 12-16
    - **🔴 Expert**: 55% obstacles, distance 14-18
    - **⚫ Nightmare**: 70% obstacles, distance 16-22

    ### 🧠 Training Details
    - **Algorithm**: DQN with HER
    - **Training**: 300k steps (3 stages)
    - **State**: Agent (x,y) + Goal position
    - **Actions**: Up, Right, Down, Left
    - **Reward**: Sparse (+0 at goal, -1 elsewhere)
    """)

with col2:
    if load_btn or 'video_loaded' not in st.session_state:
        diff_key = difficulties[difficulty_display]
        video_path = f"videos/{diff_key}_run{run:02d}_BFSvsRL.mp4"

        if os.path.exists(video_path):
            bfs_rate = success_rates[diff_key]["bfs"]
            rl_rate = success_rates[diff_key]["rl"]

            # Stats cards
            metric_col1, metric_col2 = st.columns(2)
            with metric_col1:
                st.metric("BFS Algorithm (Left)", f"{bfs_rate}%", "Optimal Path")
            with metric_col2:
                st.metric("RL Agent (Right)", f"{rl_rate}%", "Trained Agent")

            # ✅ UPDATED: LEFT=BLUE=BFS, RIGHT=GREEN=RL
            st.info("🎬 **LEFT (Blue tint):** BFS Algorithm  |  **RIGHT (Green tint):** Trained RL Agent")

            # Video player
            st.video(video_path)
            st.session_state.video_loaded = True
        else:
            st.error(f"⚠️ Video not found: {video_path}")
    else:
        st.info("👆 Select a difficulty level and click **Load Video** to begin")

st.divider()

# Results table
st.subheader("📈 Training Results Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Excellent Performance**
    - 🟢 Tutorial: **100%** ✅
    - 🔵 Easy: **100%** ✅
    """)

with col2:
    st.markdown("""
    **Challenging Levels**
    - 🟡 Medium: **20%** ⚠️
    - 🟠 Hard: **0%** ❌
    """)

with col3:
    st.markdown("""
    **Beyond Training Difficulty**
    - 🔴 Expert: **0%** ❌
    - ⚫ Nightmare: **0%** ❌
    """)

st.divider()

# Key insights
st.subheader("🔍 Key Insights")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **✅ Strengths**
    - Perfect on simpler tasks (Tutorial, Easy)
    - Learned basic navigation effectively
    - Curriculum learning helped initial stages
    """)

with col2:
    st.markdown("""
    **⚠️ Challenges**
    - Struggles with higher obstacle density
    - Difficulty generalizing to unseen complexity
    - Sparse rewards limit exploration
    """)

st.divider()

# Links
st.markdown("""
### 🔗 Project Links
[🌐 Portfolio](https://alfredso.com/portfolio) | [💻 GitHub](https://github.com/Donald8585/warehouse-rl-robot) | [💼 LinkedIn](https://linkedin.com/in/alfred-so)

---
*Built by Alfred So | MSc Data Science & AI | Hong Kong*
""")
