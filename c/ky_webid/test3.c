#include <stdio.h>
#include <stdlib.h>

//変数命の規則
//
//変数名に使える文字種
//
//アルファベット
//数字
//アンダースコア
//
//上記条件を満たすが変数名に出来ないケース
//
//変数の先頭に数字
//_(アンダースコア)だけの場合
//32ビット以上の変数名
//予約語

int main()
{
    int num10        = 1000;
//    int double       = 1000; // バツ 予約語
    int input_number = 1000;
    int RETURN       = 1000;
//    int 123          = 100 , num100; //数字から始まる
    int _123         = 1000;
    printf("result => %d \n" , num10);
    return EXIT_SUCCESS;
}
