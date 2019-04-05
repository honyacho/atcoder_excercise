package main

import "fmt"

func main() {
	var numStops int
	var numLines int
	fmt.Scan(&numStops)
	fmt.Scan(&numLines)

	memo := make([][]int, numStops)

	for i := 0; i < numStops; i++ {
		memo[i] = make([]int, numStops)
		for j := 0; j < numStops; j++ {
			memo[i][j] = 2147483647
		}
	}

	for i := 0; i < numLines; i++ {
		var left int
		var right int
		fmt.Scan(&left)
		fmt.Scan(&right)
		fmt.Scan(&memo[left-1][right-1])
		memo[right-1][left-1] = memo[left-1][right-1]
	}

	for i := 0; i < numStops; i++ {
		for j := 0; j < numStops; j++ {
			for k := 0; k < numStops; k++ {
				if j == k {
					memo[j][k] = 0
				} else {
					if memo[j][k] < memo[j][i]+memo[i][k] {
						memo[j][k] = memo[j][k]
					} else {
						memo[j][k] = memo[j][i] + memo[i][k]
					}
				}
			}
		}
	}

	var min int = 2147483647
	for i := 0; i < numStops; i++ {
		var max int = 0
		for j := 0; j < numStops; j++ {
			if memo[i][j] > max {
				max = memo[i][j]
			}
		}

		if max < min {
			min = max
		}
	}

	fmt.Println(min)
}
