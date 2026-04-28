import java.util.Arrays;
class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int[] num=Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        sb.append(Arrays.stream(num).min().getAsInt());
        sb.append(" ");
        sb.append(Arrays.stream(num).max().getAsInt());
        return sb.toString();
    }
}