class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int j = 0, result = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                j = 0;
                continue;
            }
            j++;
            result = Math.max(j, result);
        }
        return result;
    }
}