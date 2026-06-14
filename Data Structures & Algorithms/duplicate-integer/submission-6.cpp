class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> seen;
        
        for(int num : nums){
            if(seen.contains(num)){
                return true;
            }else{
                seen[num] = 0;
            }
        }
        return false;
    }
};