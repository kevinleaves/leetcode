class Solution {
    public int[] twoSum(int[] nums, int target) {
        // create hashmap
        HashMap<Integer, Integer> seen = new HashMap<>(); 
        // iterate through nums array
        for (int i = 0; i < nums.length; i++) {
            // if target - currNum exists in hashmap, return current idx and the retreived idx
            int currNum = nums[i];
            int difference = target - nums[i];
            if (seen.containsKey(difference)) {
                return new int[]{i, seen.get(difference)};
            } else {
                // else add the current number:idx into the hashmap
                seen.put(currNum, i);
            }           
        };

    // we should return something before the iteration ends
        return new int[]{-1, -1};
    }
}