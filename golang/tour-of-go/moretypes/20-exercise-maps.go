package main

import (
	"fmt"
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	ss := strings.Fields(s)
	num := len(ss)
	ret := make(map[string]int)
	for i := 0; i < num; i++ {
		(ret[ss[i]])++
	}
	return ret
}

func main() {
	wc.Test(WordCount)
}
