#include<stdio.h>
#include<math.h>
#include<stdbool.h>

int maxdigit(int p,int q,int r)
{
	int max=0;
	while(p>0)
	{
		max=p%10>max?p%10:max;
		p/=10;
	}
	while(q>0)
	{
		max=q%10>max?q%10:max;
		q/=10;
	}
	while(r>0)
	{
		max=r%10>max?r%10:max;
		r/=10;
	}
	return max;
}

int todecimal(int x,int n)
{
	int decimal=0;
	for(int i=0;x>0;i++)
	{
		decimal+=(x%10)*(int)pow((double)n,(double)i);
		x/=10;
	}
	return decimal;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int t=0;t<T;t++)
	{
		int p, q, r;
		bool solved=false;
		scanf("%d %d %d", &p, &q, &r);
		for(int n=maxdigit(p,q,r)+1;n<=16;n++)
			if(todecimal(p,n)*todecimal(q,n)==todecimal(r,n))
			{
				printf("%d\n", n);
				solved=true;
				break;
			}
		if(!solved)
			printf("0\n");
	}
	return 0;
}