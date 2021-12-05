func oneIsMost(input: [Int]) -> Bool {
  let sum = input.reduce(0) { $0 + $1 }
  return sum > input.count / 2
}

var lines: [[Int]] = []
while let line = readLine() {
  lines.append(Array(line).map { $0.wholeNumberValue! })
}

let nBits = lines[0].count
var gamma = 0
var epsilon = 0
for i in 0..<nBits {
  let input = lines.map { $0[i] }
  if oneIsMost(input: input) {
    gamma += 1 << (nBits - i - 1)
  } else {
    epsilon += 1 << (nBits - i - 1)
  }
}

let result = gamma * epsilon
// print(String(result, radix: 2))
print(result)
