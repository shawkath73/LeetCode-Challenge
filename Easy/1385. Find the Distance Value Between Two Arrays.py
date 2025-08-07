class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            i = 0
            j = len(arr2)-1
            while i <= j:
                mid = i + (j-i) // 2
                if abs(num - arr2[mid]) <= d:
                    count += 1
                    break
                elif arr2[mid] < num:
                    i = mid + 1
                else:
                    j = mid - 1
        return len(arr1)-count                                       