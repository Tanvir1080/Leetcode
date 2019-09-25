class Solution {
    public String toLowerCase(String str) {
        StringBuilder s = new StringBuilder();
        char c;
        for(int i = 0; i < str.length(); i++)
        {   
            
            if((int)str.charAt(i) > 64 && (int)str.charAt(i) < 91)
            {
                c = (char)(str.charAt(i) + 32);
                s.append(c);
            }
            else
            {
                s.append(str.charAt(i));
            }
            
        }
        
        return s.toString();
    }
}