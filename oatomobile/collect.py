import oatomobile
import oatomobile.envs
from oatomobile.datasets.carla import CARLADataset

if __name__ == "__main__":
    dataset = CARLADataset(id = "raw")
    dataset.collect(num_episodes = 1,
                    output_dir = "/home/wyao1/data_oatomobile_collected/raw",
                    max_steps_per_episode = 2000,
                    debug = False)
