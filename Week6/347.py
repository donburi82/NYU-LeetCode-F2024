# 347. Top K Frequent Elements
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # O(nlogn)
    freq = Counter(nums)
    freq = sorted(freq.items(), key=lambda x: -x[1])
    
    res = []
    for i in range(k):
        res.append(freq[i][0])

    return res

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # O(nlogk)
    freq = Counter(nums)
    
    heap = []
    for num, cnt in freq.items():
        heapq.heappush(heap, (cnt, num))
        if len(heap)>k:
            heapq.heappop(heap)

    return [num for cnt, num in heap]