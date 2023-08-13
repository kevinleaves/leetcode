class Solution {
    public boolean isPalindrome(String s) {
        // pointer at beginning and end of s
        // get chars at l, r 
        int l = 0;
        int r = s.length() - 1;
        

        while (l < r) {
            // make sure pointers are valid
            char right = s.charAt(r);
            char left = s.charAt(l);

            while (l < r && !Character.isLetterOrDigit(left)) {
                l += 1;
                left = s.charAt(l);
            }
            while (l < r && !Character.isLetterOrDigit(right)) {
                r -= 1;
                right = s.charAt(r);
            }

            if (!String.valueOf(left).toLowerCase().equals(String.valueOf(right).toLowerCase())) {
                return false;
            }

            l += 1;
            r -= 1;
        }
        return true;
        // compare
        // move pointers

    }
}