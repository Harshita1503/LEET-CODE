'''You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True

        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        for x3,y3 in coordinates[2:]:
            if(y3-y1)*(x2-x1)-(x3-x1)*(y2-y1)!=0:
                return False
        return True    
