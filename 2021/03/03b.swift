func boolArray2Int(boolArray: [Int]) -> Int {
  let nBits = boolArray.count
  var result = 0
  for i in 0..<nBits {
    if boolArray[i] == 1 {
      result += 1 << (nBits - i - 1)
    }
  }
  return result
}

func oneIsMost(input: [Int], def: Bool, anti: Bool) -> Bool {
  let sum = input.reduce(0) { $0 + $1 }
  if Double(sum) == Double(input.count) / 2.0 {
    return def
  }
  return (sum > input.count / 2) != anti
}

func rating(lines: [[Int]], def: Bool, anti: Bool) -> [Int] {
  let nBits = lines[0].count
  var results = lines
  for i in 0..<nBits {
    let transposed = results.map { $0[i] }
    let modeAtI = oneIsMost(input: transposed, def: def, anti: anti)
    results = results.filter { ($0[i] == 1) == modeAtI }
    if results.count <= 1 {
      break
    }
  }
  return results[0]
}

var lines: [[Int]] = []
while let line = readLine() {
  lines.append(Array(line).map { $0.wholeNumberValue! })
}

let ox = rating(lines: lines, def: true, anti: false)
let co2 = rating(lines: lines, def: false, anti: true)
print(boolArray2Int(boolArray: ox) * boolArray2Int(boolArray: co2))
