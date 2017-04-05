#include <stdio.h>  

unsinged int x = 0x7f000001;
unsigned char* ptr = (unsinged char*) &x;
printf("%02x,%02x,%02x,%02x\n", ptr[0], ptr[1], ptr[2], ptr[3] );
