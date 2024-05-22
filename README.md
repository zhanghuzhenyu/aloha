# MOBILE ALOHA 


## To-Use:

### option 1
1. Start Omniverse-Isaac Sim.
2. Open Aloha directory, right click on train.py and edit as python script
3. Edit config.json to setup path for assets and logs.
4. Create all the directories which are mentioned in [DIRECTORY STRUCTURE](#directory-structure) but not present after cloning (for example models)


### option 2
1. specify asset paths in `config.json`
2. run `python.sh run_demo.py` using shell script provided by Isaac Sim


## DIRECTORY STRUCTURE:

- **Agents**: Contains RL agents like TDMPC, DreamerV3 etc.
- **Assets**: Contains robot model, scene model object etc ([Download from here](https://disk.yandex.com/d/uoe_AzbQPTrsPw)).
- **Models**: Contains trained models and training logs
- **Tasks**: Contains code for creating training envrionment.
- **Utils**: Contains utility scripts (like config parser).
- **Wrappers**: Contains Gym-Env wrapper (It will contain wrapper for VecEnv which would determine no. of timesteps and other details about RL environment).

## To-Do:

- [ ] Add scene assets
- [ ] Add Manipulator Controller
- [ ] Create Manipulation Tasks
- [ ] Create Manipulation + Navigation Tasks
- [ ] Add Dockerfile
- [ ] Add Omniverse-Streaming 
