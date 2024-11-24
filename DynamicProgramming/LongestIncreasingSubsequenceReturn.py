def find_longest_increasing_subsequence(length, nums):
    LIS = [1] * length
    prev = [-1] * length  # To track previous indices in the LIS

    # Build the LIS array and track previous indices
    for i in range(1, length):
        for j in range(i):
            if nums[i] > nums[j] and LIS[i] < LIS[j] + 1:
                LIS[i] = LIS[j] + 1
                prev[i] = j

    # Find the index of the maximum length in LIS
    max_length = max(LIS)
    max_index = LIS.index(max_length)

    # Reconstruct the indices of the LIS
    indices = []
    while max_index != -1:
        indices.append(max_index)
        max_index = prev[max_index]

    # Reverse to get indices in the correct order
    indices.reverse()

    indices_str = " ".join(map(str, indices))
    print(max_length)
    print(indices_str)


if __name__ == "__main__":
    length = int(input().strip())
    nums = list(map(int, input().strip().split()))
    find_longest_increasing_subsequence(length, nums)
