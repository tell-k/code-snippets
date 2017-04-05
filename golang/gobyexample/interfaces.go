package main

import "fmt"
import "math"

type geometry interface {
	area() float64
	perim() float64
	hello(msg string) string
}

type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}
func (r rect) hello(msg string) string {
	s := fmt.Sprintf("%s is %f.\n", msg, r.area())
	return s
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}
func (c circle) hello(msg string) string {
	s := fmt.Sprintf("%s is %f.\n", msg, c.area())
	return s
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
	fmt.Println(g.hello("msgtest"))
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	measure(r)
	measure(c)
}
