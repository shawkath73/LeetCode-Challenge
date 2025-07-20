class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for w,h in dimensions:
            diagonal_sqr = w * w + h * h
            area = w * h
            if diagonal_sqr > max_diagonal:
                max_diagonal = diagonal_sqr
                max_area = area
            elif diagonal_sqr == max_diagonal:
                max_area = max(max_area,area)     
        return max_area