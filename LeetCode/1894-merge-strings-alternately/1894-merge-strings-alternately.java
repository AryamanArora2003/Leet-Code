class Solution {
    public String mergeAlternately(String word1, String word2) {
        String finalString = "";
        String shortString;

        if (word1.length()>0 && word2.length()>0){
            if(word1.length() >= word2.length()){
                shortString = word2;
                for(int i=0; i<word2.length();i++){
                    finalString += word1.charAt(i);
                    finalString += word2.charAt(i);
                }
                int stop = word2.length();
                while(stop < word1.length()){
                    finalString += word1.charAt(stop);
                    stop++;
                }

            }
            else{
                shortString = word1;
                for(int i=0; i<word1.length();i++){
                    finalString += word1.charAt(i);
                    finalString += word2.charAt(i);
                }
                int stop = word1.length();
                while(stop < word2.length()){
                    finalString += word2.charAt(stop);
                    stop++;
                }
            }
        
        }
        return finalString;
    }

}