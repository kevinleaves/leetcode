class Solution {
    public void sortColors(int[] nums) {
        int numSwaps = 0;
        for (int i = 0; i < nums.length; i++) {
          for (int j = 0; j < nums.length - 1; j++) {
            if (nums[j] > nums[j + 1]) {
              // swap them
              numSwaps += 1;
              int tmp = nums[j];
              nums[j] = nums[j + 1];
              nums[j+1] = tmp;
            }
          }
        }
    }
}