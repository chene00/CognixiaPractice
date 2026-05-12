class Main:

    @staticmethod
    def main():
        numbers = [10, 23, 52, 6, 1, 3, 4, 102]
        print(f"largest number: {Main.findLargest(numbers)}")

    @staticmethod
    def findLargest(nums):
        largest = 0
        for i in nums:
            if i > largest:
                largest = i
        return largest

if __name__ == "__main__":
    Main.main()
