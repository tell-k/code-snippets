package main

import "fmt"

type rect struct {
	width, height int
}

func (r *rect) area() int {
	return r.width * r.height
}

func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

type Person struct{ name string }

func (p *Person) Greet(msg string) {
	fmt.Printf("%s, I'm %s.\n", msg, p.name)
}

func (p *Person) UnchangeName(name string) {
	p.name = name
}

func main() {
	r := rect{width: 10, height: 5}
	fmt.Println("area:", r.area())
	fmt.Println("perim:", r.perim())

	rp := &r
	fmt.Println("area:", rp.area())
	fmt.Println("perim:", rp.perim())

	p := &Person{name: "taro"}
	p.UnchangeName("jiro")
	p.Greet("Hello")
}
