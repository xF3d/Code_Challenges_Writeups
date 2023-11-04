#include <stdio.h>

int main() {
    printf("Inserisci un numero: ");
    int n;
    scanf("%d", &n);
    
    int count = 0;
    
    for(int i = 3; i >= 1; i--) {
        int dv = n/i;
        int rs = n%i;
        
        char* x;
        
        switch(i){
            case 1:
                x = "single";
                break;
            case 2:
                x = "double";
                break;
            case 3:
                x = "triple";
                break;
            
        }
        
        while(dv > 20) {
            printf("%s %d\n", x, 20);
            n-=20 * i;
            dv-=20;
            count++;
        }
        
        if(dv > 0) {
            printf("%s %d\n", x, dv);
            n-=dv * i;
            count++;
        }
    }
    
    if(count > 3) printf("Impossible");
    
    return 0;
}