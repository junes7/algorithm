import java.util.Arrays;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int rlt = n-lost.length;
        Arrays.sort(lost);
        Arrays.sort(reserve);
        // 여벌의 체육복이 있지만 도둑맞아 빌려줄 수 없는 경우
        for(int i=0;i<lost.length;i++) {
            for(int j=0;j<reserve.length;j++) {
                if(lost[i]==reserve[j]){
                    rlt+=1;
                    lost[i]=-1;
                    reserve[j]=-1;
                    break;
                }   
            }
        }
        // 여벌의 체육복 학생이 앞 또는 뒤로 빌려줄 수 있는 경우
        for(int i=0;i<lost.length;i++) {
            for(int j=0;j<reserve.length;j++) {
                if(lost[i]-1==reserve[j] || lost[i]+1==reserve[j]) {
                    rlt+=1;
                    reserve[j]=-1;
                    break;
                }
            }
        }
        return rlt;
    }
}