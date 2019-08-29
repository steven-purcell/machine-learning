package main

import (
	"fmt"
	"math"
)

func main() {
	var cur_x float64 = -10.00
	// ydiff := 2*cur_x + 10
	var precision float64 = 0.00000001
	// var prevStepSize float64 = 1.00
	var n int = 0
	var max_n int = 25000
	var rate float64 = 0.001
	// var prev_x float64 = 0.00

	for prevStepSize := 1.00; prevStepSize > precision && n < max_n; n += 1 {
		prev_x := cur_x
		cur_x = cur_x - rate*(2*cur_x+10)
		prevStepSize = math.Abs(cur_x - prev_x)
		fmt.Println("Iteration:", n, "\nX:", cur_x)
	}
	fmt.Println("The local minimum occurs at", cur_x)
}
