var nums: [Int] = []
while let line = readLine() {
    nums.append(Int(line)!)
}
let sums = zip(zip(nums, nums[1...]), nums[2...]).map {($0.0.0 + $0.0.1 + $0.1)}
print(zip(sums, sums[1...]).filter {$0.0 < $0.1}.count)
