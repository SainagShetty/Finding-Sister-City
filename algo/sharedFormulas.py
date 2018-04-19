#Implementation of Haversine Formula for distance
#Takes coordinates as input and returns distance across earth's surface in km
from skcriteria import MIN, MAX
from math import cos, asin, sqrt, pi

def distance(lat1, lng1, lat2, lng2):
    p = pi/180     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lng2 - lng1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin

# Takes a list of values and normalizes them from 0 to 14
# Used in scikit-criteria 
def normalize_weights(weights):
   max_min = [MIN if weight >= 0 else MAX for weight in weights]
   abs_weights = [abs(weight) for weight in weights]
   total = sum(abs_weights)
   normalized_weights = [float(weight) / total for weight in abs_weights]
   return (max_min, normalized_weights)