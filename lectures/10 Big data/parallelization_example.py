import pandas as pd
def get_3rd_closest_dist(pantries, geom):
    distances = pantries.distance(geom)
    third_closest = distances.sort_values().iloc[2]
    return third_closest