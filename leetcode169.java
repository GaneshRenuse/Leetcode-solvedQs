class Solution {
    public int majorityElement(int[] nums) {
        int arrsize = nums.length;
        int count = 0;
        int answer = 0;

        for (int i = 0; i < arrsize; i++) {
            count = 0;
            for(int j = i + 1; j < arrsize; j++){
                if(nums[i] == nums[j]){
                    count++;
                }
            }
            if (count == arrsize/2){
                answer = nums[i];
                break;
            }
        }

        return answer;
    }
}
