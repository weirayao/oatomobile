from oatomobile.datasets.carla import CARLADataset

if __name__ == "__main__":
    data = CARLADataset("raw")
    data.process("/data/datasets/carla/data_oatomobile_collected/raw", 
                 "/data/datasets/carla/data_oatomobile_collected/processed")