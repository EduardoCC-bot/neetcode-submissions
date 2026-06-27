class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 1 if sum(arr[:k])/k >= threshold else 0
        t_s = threshold * k
        suma = sum(arr[:k])
        for i in range(k,len(arr)):
            suma = suma + arr[i] - arr[i-k]
            if suma >= t_s:
                cnt+=1            
            
        return cnt