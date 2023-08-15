class Solution {
    public boolean isValid(String s) {
        /**
        populate HashMap with parenthesis pairs
        instantiate stack
        iterate through s
        if open parens, add to stack
        if close parens, check top stack to see if it's matching, if so, pop

        if stack is empty, return true, else, false
         */ 
        
        Deque<String> stack = new ArrayDeque<String>();
        Map<String, String> lookup = new HashMap<>();
        lookup.put(")", "(");
        lookup.put("}", "{");
        lookup.put("]", "[");

        for (char c : s.toCharArray()) {
            // System.out.println(c);
            
            if (lookup.containsKey(String.valueOf(c))) {
                if (stack.size() > 0 && stack.peekLast().equals(lookup.get(String.valueOf(c)))) {
                    stack.pollLast();
                } else {
                    stack.addLast(String.valueOf(c));    
                }
            } else {
                // open parens add to stack
                stack.addLast(String.valueOf(c));
            }
        }
        return stack.size() == 0;
    }
}