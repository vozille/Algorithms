def main(nums: list):
    dp = [0] * len(nums)

    for i in range(len(nums)):
        curr_max = 0
        for j in range(i):
            if nums[i] > nums[j]:
                curr_max = max(curr_max, dp[j])
        dp[i] = curr_max + 1

    return max(dp)


if __name__ == '__main__':
    print(main([10,9,2,5,3,7,101,18]))
