class Solution {
    public boolean isAnagram(String a, String b) {
        HashMap<Character,Integer> freq = new HashMap<>();

        if (a.length() != b.length()) return false;
        
        for (int i = 0; i < a.length(); i++) {
            char lowercaseA = Character.toLowerCase(a.charAt(i));
            freq.put(lowercaseA, freq.getOrDefault(a.charAt(i), 0) + 1);
            char lowercaseB = Character.toLowerCase(b.charAt(i));
            freq.put(lowercaseB, freq.getOrDefault(b.charAt(i), 0) - 1);
        }
         
        for (char c : freq.keySet()) {
            if (freq.get(c) != 0) {
                return false;
            }
        }

        return true;

    }
}