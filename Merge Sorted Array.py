class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        merged = []
        i = j = 0

        # Step 1: Merge nums1 and nums2 into a new list
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Step 2: Add remaining elements
        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        # Step 3: Copy merged result back into nums1
        for k in range(m + n):
            nums1[k] = merged[k]

        return nums1

sol=Solution()
print(sol.merge([1], 1, [] , 0))
            