
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ret = string(word1.length() + word2.length(), ' ');
        int w1_idx = 0;
        int w2_idx = 0;
        int ret_idx = 0;
        int alternate_length = (word1.length() < word2.length()) ? word1.length() : word2.length();

        while (w1_idx < word1.length() && w2_idx < word2.length()) {
            if (ret_idx % 2 == 0) {
                ret[ret_idx] = word1[w1_idx];
                w1_idx++;
            } else {
                ret[ret_idx] = word2[w2_idx];
                w2_idx++;
            }
            ret_idx++;
        }
        for (; w1_idx < word1.length(); w1_idx++) {
            ret[ret_idx] = word1[w1_idx];
            ret_idx++;
        }
        for (; w2_idx < word2.length(); w2_idx++) {
            ret[ret_idx] = word2[w2_idx];
            ret_idx++;
        }
        return ret;
    }
};