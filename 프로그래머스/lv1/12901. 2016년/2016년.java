class Solution {
    public String solution(int a, int b) {
        String rlt = "",day[]={"MON","TUE","WED","THU","FRI","SAT","SUN"};
        int days=0,month[]={31,29,31,30,31,30,31,31,30,31,30,31};
        for(int i=0;i<a-1;i++)
            days+=month[i];
        days+=b-1;
        rlt=day[(days+4)%7];
        return rlt;
    }
}