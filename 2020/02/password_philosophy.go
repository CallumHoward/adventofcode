// Password Philosophy
// https://adventofcode.com/2020/day/2

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func countLetter(inputLetter rune, input string) int {
	var count = 0
	for _, letter := range input {
		if letter == inputLetter {
			count++
		}
	}
	return count
}

func solve(line string) bool {
	split := strings.Fields(line)
	minMax := strings.Split(split[0], "-")
	min, _ := strconv.Atoi(minMax[0])
	max, _ := strconv.Atoi(minMax[1])
	letter := rune(split[1][0])
	password := split[2]

	count := countLetter(letter, password)
	return min <= count && count <= max
}

func main() {
	var scanner = bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	var count = 0
	for scanner.Scan() {
		if solve(scanner.Text()) {
			count++
		}
	}
	fmt.Println(count)
}
