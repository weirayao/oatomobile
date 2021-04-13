import oatomobile
import oatomobile.envs
from oatomobile.datasets.carla import CARLADataset

if __name__ == "__main__":
    dataset = CARLADataset(id = "raw")
    dataset.collect(num_episodes = 5,
                    output_dir = "/data/datasets/carla/data_oatomobile",
                    max_steps_per_episode = 1000)
