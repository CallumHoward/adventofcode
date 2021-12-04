var instructions: [(String, Int)] = []
while let line = readLine() {
  let arr = line.split(separator: " ")
  instructions.append((String(arr[0]), Int(arr[1])!))
}

var horizontal = 0
var depth = 0
var aim = 0
for (dir, dist) in instructions {
  if dir == "forward" {
    horizontal += dist
    depth += aim * dist
  } else if dir == "down" {
    aim += dist
  } else if dir == "up" {
    aim -= dist
  }
}

print(horizontal * depth)
