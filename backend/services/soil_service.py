import random

def get_soil_data(lat, lon):

    # Simulated Soil Data (API can be plugged later)

    return {
        "nitrogen": random.randint(60, 120),
        "phosphorus": random.randint(30, 80),
        "potassium": random.randint(40, 90),
        "ph": round(random.uniform(5.5, 7.5), 1)
    }
