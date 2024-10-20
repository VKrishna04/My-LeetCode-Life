class Solution {
    public static int findNumbers(int[] nums) {
        int result = 0;
        for (int i : nums) {
            if (NoOfDigits(i,0)%2==0){
                result++;
            }
        }
        return result;
    }

    public static int NoOfDigits(int n, int result) {
        if (n < 10) {
            return result + 1;
        }
        return NoOfDigits(n / 10, result + 1);
    }
}