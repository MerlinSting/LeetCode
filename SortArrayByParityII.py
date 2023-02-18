class Solution:
    def sortArrayByParityII(self, nums):
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and i % 2 == 0:
                temp = nums[i]
                index = self.findEven(i, nums)
                nums[i] = nums[index]
                nums[index] = temp
            elif nums[i] % 2 == 0 and i % 2 != 0:
                temp = nums[i]
                index = self.findOdd(i, nums)
                nums[i] = nums[index]
                nums[index] = temp
        return nums
    
    def findEven(self, i, nums):
        for j in range(i, len(nums)):
            if nums[j] % 2 == 0:
                return j

    def findOdd(self, i, nums):
        for j in range(i, len(nums)):
            if nums[j] % 2 != 0:
                return j

def main():
    test = Solution()
    print(test.sortArrayByParityII(nums=[4,2,5,7]))
    

if __name__ == "__main__":
    main()