// Report Repair
// https://adventofcode.com/2020/day/1

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	const target = 2020
	var scanner = bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	var nums = make(map[int]bool)
	for scanner.Scan() {
		var num, _ = strconv.Atoi(scanner.Text())
		nums[num] = true
	}

	for key := range nums {
		if nums[target-key] {
			fmt.Println(key * (target - key))
			break
		}
	}
}
