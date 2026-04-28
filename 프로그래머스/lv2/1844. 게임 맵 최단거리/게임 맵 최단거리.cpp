#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> maps)
{
    int cnt,x=1,y=1,nx=0,ny=0,l=maps.size(),m=maps[0].size();
    vector<int> add,goal={l,m},dx,dy;
    vector<int>::iterator itr;
    queue<vector<int>> q;
    for(int i=0;i<m;i++) {
        add.push_back(0);
    }
    for(int i=0;i<maps.size();i++) {
        itr=maps[i].begin();
        maps[i].insert(itr,0);
        maps[i].push_back(0);
    }
    maps.push_back(add);
    maps[1][1]=0;
    q.push(x,y,1);
    dx={0,1,0,-1};
    dy={1,0,-1,0};
    while(!q.empty()) {
        x=get<0>(q.front());
        y=get<1>(q.front());
        cnt=get<2>(q.front());
        q.pop();
        cout<<x<<' '<<y<<' '<<cnt<<endl<<endl;
        if(x==goal[0] and y==goal[1])
            return cnt;
        // for(size_t i=0;i<dx.size()&&i<dy.size();i++) {
        //     cout<<i<<' '<<dx[i]<<' '<<dy[i]<<endl;
        //     nx=x+dx[i];
        //     ny=y+dy[i];
        //     cout<<nx<<' '<<ny<<' '<<cnt+1<<endl;
        //     if(maps[nx][ny]==1) {
        //         maps[nx][ny]=0;
        //         q.push(make_tuple(nx,ny,cnt+1));
        //     }       
        // }
    }
    return cnt;
}