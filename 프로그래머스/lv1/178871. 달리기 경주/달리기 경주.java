import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String tmp, rlt[] = players;
        int rank;
        Map<String, Integer> map=IntStream.range(0,players.length)
            .boxed()
            .collect(Collectors.toMap(
                i->players[i],
                i->i
            ));
        for(String st:callings) {
            rank=map.get(st);
            // 선수 위치 swap
            tmp = rlt[rank-1];
            rlt[rank-1]=rlt[rank];
            rlt[rank]=tmp;
            // key-value값 수정
            map.put(rlt[rank-1],rank-1);
            map.put(rlt[rank],rank);
        }
        return rlt;
    }
}