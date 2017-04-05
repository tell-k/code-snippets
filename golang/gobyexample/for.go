package main

import "fmt"
import "strings"

func main() {
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + i
	}

	fmt.Println(strings.Repeat("-", 10))
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	fmt.Println(strings.Repeat("-", 10))
	for {
		fmt.Println("loop")
		break
	}

	fmt.Println(strings.Repeat("-", 10))
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}

}
