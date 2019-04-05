package main

import "fmt"
import "sort"

func binSearch(from int, to int, limit int, inputs []int) int {
	half := (from + to) / 2
	if from == half {
		return inputs[from]
	}

	if inputs[half] <= limit {
		return binSearch(half, to, limit, inputs)
	} else {
		return binSearch(from, half, limit, inputs)
	}
}

func main() {
	var length int
	var limit int
	var max int = 0
	fmt.Scan(&length)
	length = length + 1
	fmt.Scan(&limit)
	inputs := make([]int, length)
	doubles := []int{}

	inputs[0] = 0
	for i := 1; i < length; i++ {
		fmt.Scan(&inputs[i])
	}
	for _, num1 := range inputs {
		for _, num2 := range inputs {
			doubles = append(doubles, num1+num2)
		}
	}
	sort.Ints(doubles)

	for _, value := range doubles {
		if value <= limit {
			if value < limit {
				value = value + binSearch(0, length*length, limit-value, doubles)
			}
			if max < value {
				max = value
			}
		}
	}
	fmt.Println(max)
}
