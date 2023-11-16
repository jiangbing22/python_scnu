import math

def distance(*args):
    if len(args) % 2 != 0 or len(args) < 2:
        raise ValueError("Invalid number of coordinates. Please provide at least two points.")

    dimensions = len(args) // 2
    point1 = args[:dimensions]
    point2 = args[dimensions:]
    if dimensions < 1:
        raise ValueError("Minimum of 1 dimension is required to calculate distance.")

    squared_distances = [(point2[i] - point1[i])**2 for i in range(dimensions)]
    sum_of_squares = sum(squared_distances)
    distance = math.sqrt(sum_of_squares)
    spatial_distance = abs(point1[0]-point2[0])
    return distance,spatial_distance
if __name__ == "__main__":

    x_distance, spatial_distance = distance(0,0,3,4)
    print(x_distance,spatial_distance)