import java.util.Map;
class Solution {
    public int[] solution(String[] park, String[] routes) {
        int x=-1,y=-1,dx=0,dy=0,m,num[] = new int[2],rlt[] = new int[2];
        String[] tmp, route;boolean obs = true;
        // 방향 해시 코드
        Map<String, int[]> map = Map.of("E",new int[]{0,1},"S",new int[]{1,0},"W",new int[]{0,-1},"N",new int[]{-1,0});
        // 시작 좌표 찾기
        for(int i=0;i<park.length;i++) {
            if(park[i].contains("S")) {
                x=i;
                y=park[i].indexOf('S');
                break;
            }
        }
        System.out.println(x);System.out.println(y);
        // 수행 명령 배열 돌면서
        for(int i=0;i<routes.length;i++) {
            tmp=routes[i].split(" ");
            m=Integer.parseInt(tmp[1]);
            System.out.println(tmp[0]);
            System.out.println(m);
            num[0]=map.get(tmp[0])[0];
            num[1]=map.get(tmp[0])[1];
            dx=num[0]*m;
            dy=num[1]*m;
            System.out.println(dx);
            System.out.println(dy);
            // 범위를 벗어났을 때
            if(x+dx<0 || x+dx>park.length || y+dy<0 || y+dy>=park[0].length()) {
                obs=true;
                continue;
            }
            // 범위를 벗어나지 않았을 때
            else {
                if(tmp[0]=="S" || tmp[0]=="N") {
                    if(num[0]>0) {
                        for(int j=x;j<x+dx+num[0];j+=num[0]) {
                            if(park[j].charAt(y)=='X') {
                                obs=true;
                                break;
                            }
                        }
                    } else {
                        for(int j=x;j>x+dx+num[0];j+=num[0]) {
                            if(park[j].charAt(y)=='X') {
                                obs=true;
                                break;
                            }
                        }
                    }
                    if(!obs) {
                        x+=dx;
                    }
                } else {
                    if(num[1]>0) {
                        for(int j=y;j<y+dy+num[1];j+=num[1]) {
                            if(park[x].charAt(j)=='X') {
                                obs=true;
                                break;
                            }
                        }
                    } else {
                        for(int j=y;j>y+dy+num[1];j+=num[1]) {
                            if(park[x].charAt(j)=='X') {
                                obs=true;
                                break;
                            }
                        }
                    }
                    
                    if(!obs) {
                        y+=dy;
                    }
                }
            }
            
        }
        rlt[0]=y;
        rlt[1]=x;
        return rlt;
    }
}