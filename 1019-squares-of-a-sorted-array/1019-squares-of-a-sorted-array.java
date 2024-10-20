import java.util.Arrays;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = nums;
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Math.abs(nums[i]);
        }
        for (int i = 0; i < result.length; i++) {
            result[i] = (int) Math.pow(nums[i], 2);
        }
        Arrays.sort(nums);
        return result;
    }
}