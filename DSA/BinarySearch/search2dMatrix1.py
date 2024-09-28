class Solution:
    def searchMatrix(self, matrix, target):

        #loop will iterate on sub list
        for i in matrix:

            #initializing left as 0 
            left=0

            #initializing right as total length of nums and subtracting one from it
            right=len(i)-1

            #loop will run until left becomes lesser or equal to right
            while left<=right:

                #initializing mid and its value will be the average of left and right
                mid=int((left+right)/2)

                #returning mid which will be the index of targeted value 
                if i[mid]==target:
                    return True
                
                #increment the left value when the value is lesser than the targeted one
                elif i[mid]<target:
                    left=mid+1

                #decreament the right value when the value is greater than the targeted one
                elif i[mid]>target:
                    right=mid-1

        #return False when targeted value is not found
        return False