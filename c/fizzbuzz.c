#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    char str[4];
    for(i=1; i<101; i++){
       sprintf(str,"%d",i);
       printf("%s\n",i%15?i%5?i%3?str:"Fizz":"Buzz":"FizzBuzz");
    }

    return EXIT_SUCCESS;
}
