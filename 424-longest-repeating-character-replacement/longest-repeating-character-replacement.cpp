class Solution {
public:
    int characterReplacement(string s, int k) {
        int l=0,r=0,res=0,cur=0;
        int arr[26]={0};
        while (r<s.size()){
            arr[s[r]-'A']++;
            cur=max(cur,arr[s[r]-'A']);
            if (((r-l+1)-cur)>k){
                arr[s[l]-'A']--;
                l++;
            }
            res=max(res,r-l+1);
            r++;
        }
        return res;
    }
};