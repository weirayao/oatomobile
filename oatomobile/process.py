from oatomobile.datasets.carla import CARLADataset

if __name__ == "__main__":
    data = CARLADataset("raw")
    for weather in ["ClearNoon", "WetNoon", "HardRainNoon", "ClearSunset"]:
        data.process("/home/wyao1/data_oatomobile_collected/raw/%s"%weather, 
                     "/data/datasets/carla/data_oatomobile_collected/processed")