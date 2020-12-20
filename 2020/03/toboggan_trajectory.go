// Toboggan Trajectory
// https://adventofcode.com/2020/day/3

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var scanner = bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	pattern := make([][]bool, 0)
	var row = 0
	for scanner.Scan() {
		var col = 0
		patternRow := make([]bool, 0)
		pattern = append(pattern, patternRow)
		for cell := range strings.Fields(scanner.Text()) {
			pattern[row].append(pattern[row], cell == '#')
			col++
		}
		row++
	}

	var count = 0
	var c = 0
	for r := 0; r < row; r++ {
		if pattern[r][c] {
			count++
		}
		c += 3
	}
	fmt.Println(count)
}
