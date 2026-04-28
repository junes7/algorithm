import java.util.*;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int cur[] = {}, tar[] ={}, num;
        String[] tmp; cur=date(today);
        List<Integer> list = new ArrayList<>();
        Map<String,Integer> map = new HashMap();
        for(String t:terms) {
            tmp=t.split(" ");
            map.put(tmp[0],Integer.parseInt(tmp[1])*28);
        }
        for(int i=0;i<privacies.length;i++) {
            tmp=privacies[i].split(" "); tar=date(tmp[0]);
            if((cur[0]-tar[0])*12*28+(cur[1]-tar[1])*28+(cur[2]-tar[2])>=map.get(tmp[1])) {
                list.add(i+1);
            }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
    public int[] date(String day) {
        return Arrays.stream(day.split("\\.")).mapToInt(Integer::parseInt).toArray();
    }
}