class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #initializing the inputs
        self.n=nums
        self.t=target

        #initializing empty list
        l=[]

        #iterating on length of nums
        for i in range(len(self.n)):

            #iterating from value of i + 1 till length of nums
            for j in range(i+1,len(self.n)):

                #checking which two numbers sum is equal to target
                if self.n[i]+self.n[j]==self.t:

                    #appending in empty list value of i,j 
                    l.append(i)
                    l.append(j)
        
        #returning list
        return l