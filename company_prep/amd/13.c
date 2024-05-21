#include <stdio.h>
#include <string.h>

enum romans { I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 };

int romanToInt(char* s) {
    int total = 0;
    for(int idx = 0; idx < strlen(s); idx++) {
        if(s[idx] == 'I') {
            total += I;
        }
        else if(s[idx] == 'V') {
            total += V;
            if ((idx > 0) && (s[idx-1]) == 'I') {
                total -= 2;
            }
        }
        else if(s[idx] == 'X') {
            total += X;
            if ((idx > 0) && (s[idx-1]) == 'I') {
                total -= 2;
            }
        }
        else if(s[idx] == 'L') {
            total += L;
            if ((idx > 0) && (s[idx-1]) == 'X') {
                total -= 20;
            }
        }
        else if(s[idx] == 'C') {
            total += C;
            if ((idx > 0) && (s[idx-1]) == 'X') {
                total -= 20;
            }
        }
        else if(s[idx] == 'D') {
            total += D;
            if ((idx > 0) && (s[idx-1]) == 'C') {
                total -= 200;
            }
        }
        else if(s[idx] == 'M') {
            total += M;
            if ((idx > 0) && (s[idx-1]) == 'C') {
                total -= 200;
            }
        }
    }
    return total;
}

int main() {
    printf("%d\n", romanToInt("III"));
    printf("%d\n", romanToInt("LVIII"));
    printf("%d\n", romanToInt("MCMXCIV"));
    printf("%d ==  (162) \n", romanToInt("CLXII"));
    printf("%d ==  (475) \n", romanToInt("CDLXXV"));
    printf("%d ==  (946) \n", romanToInt("CMXLVI"));
    printf("%d ==  (892) \n", romanToInt("DCCCXCII"));
    printf("%d ==  (884) \n", romanToInt("DCCCLXXXIV"));
    printf("%d ==  (777) \n", romanToInt("DCCLXXVII"));
    printf("%d ==  (915) \n", romanToInt("CMXV"));
    printf("%d ==  (761) \n", romanToInt("DCCLXI"));
    printf("%d ==  (689) \n", romanToInt("DCLXXXIX"));
    printf("%d ==  (94) \n", romanToInt("XCIV"));
    return 0;
}