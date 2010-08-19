#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

void str_reverse (char str[], char result[]) {
    char *first = &str[0];
    char *last  = &str[strlen(str)-1];
    int  index  = 0;
    while (last >= first) {
         result[index++] = *last; 
         last--;
    }
}

wchar_t *str_reverse2(wchar_t *s) {  
    wchar_t *a, *b = s, wc;
    if (*s == 0) return s;

    while (*++b != 0);

    for (a = s; a < --b; a++) {
//        printf("swap %lc <=> %lc\n", *a, *b);
        wc = *a, *a = *b, *b = wc;
    }
    return s;
}

int main(void) {
    char str[6]  = "ab345";
    char rev[strlen(str)+1];
    str_reverse(str, rev);
    printf("str => %s\n", str);
    printf("rev => %s\n", rev);

    wchar_t str2[] = L"日本語";
    setlocale(LC_ALL, "");
    printf("str => %ls\n", str2);
    str_reverse2(str2);
    printf("rev => %ls\n", str2);
    return EXIT_SUCCESS;
}
