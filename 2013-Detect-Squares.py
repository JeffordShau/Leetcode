from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.xcoords = defaultdict(set)
        self.ycoords = defaultdict(set)
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xcoords[x].add(y)
        self.ycoords[y].add(x)
        self.counts[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        counter = 0
        x, y = point

        same_horizontal = self.ycoords[y]
        same_vertical = self.xcoords[x]

        if len(same_horizontal) < len(same_vertical):

            for xcoord in same_horizontal:
                dist = abs(xcoord - x)
                if dist == 0:
                    continue

                counts_center = self.counts[(xcoord, y)]

                counts_bottom1 = self.counts[(xcoord, y - dist)]
                counts_bottom2 = self.counts[(x, y - dist)]
                counter += counts_bottom1 * counts_bottom2 * counts_center

                counts_above1 = self.counts[(xcoord, y + dist)]
                counts_above2 = self.counts[(x, y + dist)]
                counter += counts_above1 * counts_above2 * counts_center

        else:

            for ycoord in same_vertical:
                dist = abs(ycoord - y)
                if dist == 0:
                    continue

                counts_center = self.counts[(x, ycoord)]

                counts_left1 = self.counts[(x - dist, ycoord)]
                counts_left2 = self.counts[(x - dist, y)]
                counter += counts_left1 * counts_left2 * counts_center

                counts_right1 = self.counts[(x + dist, ycoord)]
                counts_right2 = self.counts[(x + dist, y)]
                counter += counts_right1 * counts_right2 * counts_center

        return counter

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)