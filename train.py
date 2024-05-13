
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3 import PPO
from omni.isaac.gym.vec_env import VecEnvBase

my_env = VecEnvBase(headless=False)

from tasks.reach import AlohaTask
task = AlohaTask(name="Aloha", n_envs=2)
my_env.set_task(task, backend="torch")


log_dir = "/home/zhang/Desktop/Gym-env/models/PPO"

checkpoint_callback = CheckpointCallback(save_freq=25000, save_path=log_dir, name_prefix="jetbot_policy_checkpoint1M")

total_timesteps = 375000

model = PPO("MlpPolicy", my_env, verbose=1,tensorboard_log=log_dir,)

model.learn(total_timesteps=total_timesteps, callback=checkpoint_callback)

model.save(log_dir + "/PPO_policy")

my_env.close()