class Solution:
    def maxScore(self, nums1, nums2, k):#in class solution we defined maxscore 
        #whose prams are self, mums1, nums2, k
        total = res = 0  #totla is set to result and it is set to 0
        heap = []# we created a empty heap list 
        
        pairs = zip(nums1, nums2) #we defined pair, Zip make nums1 and nums2 as set
        # for ex like nums1 =[1,2,3] and nums2 = [4,5,6] so what zip will do it 
        # it will make them as set of tuples like [1,4]
                                                # [2,5] and etc
        
        sorted_pairs = sorted(pairs, key=lambda x: -x[1]) #sorted_pair will sort the pair
        #by key and key defined as lambda x: -x[1], where - means reverse order, desending order
        #[1] means second number of the set and if there was 0 it would mean first set
        
        for pair in sorted_pairs: #for loop
            num1, num2 = pair  
            heappush(heap, num1)#will add number to the heap to be added
            total += num1 #num1 will added to the total
            if len(heap) > k: #if lenght of heap is bigger than k
                total -= heappop(heap)# then heappop will remove the smallest number from the heap of the total
            if len(heap) == k:
                res = max(res, total * num2) # it will compare result and ans value and then set it to res (result)
        
        return res