import numpy as np 

def points_distance(list_of_points,central_point,k):
	set_of_points = []
	while len(set_of_points) < k:
		distances = []
		for i in list_of_points:
			a = central_point
			b = i
			dist = np.linalg.norm(np.array(central_point)-np.array(i))
			distances.append(dist)
		nearest_point = list_of_points[np.argmin(distances)]
		set_of_points.append(nearest_point)
		list_of_points.remove(nearest_point)
	print(set_of_points)
	return set_of_points

if __name__ == '__main__':
	list_of_points = [(0,0), (5,4), (3,1)]
	central_point = (1,2)
	k = 2
	points_distance(list_of_points, central_point, k)