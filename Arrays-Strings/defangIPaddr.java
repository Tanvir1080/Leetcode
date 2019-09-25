class Solution {
    public String defangIPaddr(String address) {
        int length = address.length();
        int periodCount = 1;
        StringBuilder s = new StringBuilder();
        char c;
        for(int i = 0; i < length; i++)
        {   
            c = address.charAt(i);
            if(Character.isDigit(c))
            {
                s.append(c);
            }
            else
            {
                s.append("[.]");
            }
        }
        return s.toString();
    }
}