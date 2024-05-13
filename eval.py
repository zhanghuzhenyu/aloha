from omni.isaac.gym.vec_env import VecEnvBase
from stable_baselines3 import PPO

env = VecEnvBase(headless=False)
from tasks.reach import ReachTask
task = ReachTask(name="Aloha", n_envs=1)
env.set_task(task, backend="torch")


# Choose the policy path to visualize
policy_path = "/home/zhang/Desktop/Vectorized-env/models/PPO/PPO_policy"


model = PPO.load(policy_path, env=env)

obs = env.reset()
while env._simulation_app.is_running():
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)

env.close()