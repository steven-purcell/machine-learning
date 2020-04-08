package main

import (
	"fmt"
	"math"
)

func main() {
	var cur_x float64 = -10.00
	const precision float64 = 0.0000000000001
	var n int = 0
	const max_n int = 25000
	const rate float64 = 0.001
	// var ydiff = (2 * cur_x) + 10

	for prevStepSize := 1.00; prevStepSize > precision && n < max_n; n += 1 {
		prev_x := cur_x
		cur_x = cur_x - rate*((2*cur_x)+10)
		prevStepSize = math.Abs(cur_x - prev_x)
		if n%10 == 0 {
			fmt.Println("Iteration:", n, "\nX:", cur_x)
		}
	}
	fmt.Println("The local minimum occurs at", cur_x)
}
