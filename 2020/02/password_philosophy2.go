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

func solve(line string) bool {
	split := strings.Fields(line)
	minMax := strings.Split(split[0], "-")
	pos1, _ := strconv.Atoi(minMax[0])
	pos2, _ := strconv.Atoi(minMax[1])
	letter := split[1][0]
	password := split[2]
	return (password[pos1-1] == letter && password[pos2-1] != letter) ||
		(password[pos1-1] != letter && password[pos2-1] == letter)
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
