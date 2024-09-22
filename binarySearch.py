class Solution:
    def binarySearch(self, nums, target):
        self.nums=nums
        self.target=target

        #initializing left as 0 
        left=0

        #initializing right as total length of nums and subtracting one from it
        right=len(self.nums)-1

        #loop will run until left becomes lesser or equal to right
        while left<=right:

            #initializing mid and its value will be the average of left and right
            mid=int((left+right)/2)

            #returning mid which will be the index of targeted value 
            if self.nums[mid]==self.target:
                return mid
            
            #increment the left value when the value is lesser than the targeted one
            elif self.nums[mid]<self.target:
                left=mid+1

            #decreament the right value when the value is greater than the targeted one
            elif self.nums[mid]>self.target:
                right=mid-1
        
        #return -1 when targeted value is not found
        return -1