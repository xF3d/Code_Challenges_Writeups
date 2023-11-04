#include <stdio.h>

void work(int d, int* n, char* s) {
    const int max = 20*d;
    while(*n!=0) {
        int rem = *n < max ? *n : max;
        *n -= rem;
        printf("%s %d\n", s, rem/d);
    }
}

int main() {
    printf("Inserisci un numero: ");
    int n;
    scanf("%d", &n);
    
    if(n <= 60) {
        work(1, &n, "single");
        return 0;
    }
    
    if(n > 160 || n%3==0) {
        if(n%3!=0) printf("Impossible\n");
        else work(3, &n, "triple");
        return 0;
    }

    if(n==61) {
        printf("triple 20\n");
        printf("single 1\n");
        return 0;
    }
    
    n-=60;
    printf("triple 20\n");
    int d3 = n/3 > 20 ? 20 : n/3;
    n-=d3*3;

    if(n!=0 && n%2==1) {
        d3--;
        n+=3;
    }
    
    if(n > 40) {
        printf("Impossible");
        return 0;
    }
    
    int d2 = n/2;
    n-=d2*2;
    
    if(d3!=0) printf("triple %d\n", d3);
    if(d2!=0) printf("double %d\n", d2);
    
    return 0;
}