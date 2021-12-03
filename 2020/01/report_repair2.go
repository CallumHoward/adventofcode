// Report Repair
// https://adventofcode.com/2020/day/1

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve(nums map[int]bool, target int) int {
	for keyA := range nums {
		for keyB := range nums {
			if nums[target-keyA-keyB] {
				return keyA * keyB * (target - keyA - keyB)
			}
		}
	}
	return 0
}

func main() {
	const target = 2020
	var scanner = bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	var nums = make(map[int]bool)
	for scanner.Scan() {
		var num, _ = strconv.Atoi(scanner.Text())
		nums[num] = true
	}

	fmt.Println(solve(nums, target))
}
