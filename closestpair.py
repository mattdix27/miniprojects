import random
'''
Closest pair problem takes n points in space and returns the closest pair of points
'''

random_tuple_list = [(random.randrange(-1000,1000), random.randrange(-1000,1000)) for i in range(1000)]

def closest_pair(tuple_list):
    min_distance = 1000000
    closest1 = []
    for i in range(len(tuple_list)-1):
        for j in range(i+1, len(tuple_list)-i):
            if pair_distance(tuple_list[i], tuple_list[j]) < min_distance:
                closest1.clear()
                closest1.append((tuple_list[i], tuple_list[j]))
                min_distance = pair_distance(tuple_list[i], tuple_list[j])
            elif pair_distance(tuple_list[i], tuple_list[j]) == min_distance:
                closest1.append((tuple_list[i], tuple_list[j]))
    return closest1

#Find the distance between two points
def pair_distance(tuple1, tuple2):
    x = tuple1[0] - tuple2[0]
    y = tuple1[1] - tuple2[1]
    distance = (x**2 + y**2)**0.5
    
    return distance

print(closest_pair(random_tuple_list))