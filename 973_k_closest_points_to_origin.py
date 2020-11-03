class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        print(f"The length of points is {len(points)}")
#         distance = {}
#         for i in range(len(points)):
#             distance[i] = points[i][0] ** 2 + points[i][1] ** 2
        
#         minVal = inf;
#         for k, v in distance.items():
#             if v <= minVal:
#                 minVal = v
        
#         print(f"minVal = {minVal}")
#         for k, v in distance.items():
#             print(k, v)
          
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
