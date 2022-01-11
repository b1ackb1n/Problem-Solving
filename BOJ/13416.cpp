#include <stdio.h>
#include <algorithm>
using namespace std;

int main(){
    int t, n, a, b, c;
    scanf("%d", &t);
    for (int i=0; i<t; i++){
        scanf("%d", &n);
        int sum = 0;
        for (int j=0; j<n; j++){
            scanf("%d %d %d", &a, &b, &c);
            if (max({a,b,c})>0){
                sum += max({a,b,c});
            }
        }
        printf("%d\n", sum);
    }
    return 0;
}