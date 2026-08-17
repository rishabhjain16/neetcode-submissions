class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []
        result = []
        for p in points:
            d = p[0]**2 + p[1]**2
            distance.append([d,(p[0],p[1])])
            distance.sort()
        for i in range(k):
            result.append(distance[i][1])
        return result


        