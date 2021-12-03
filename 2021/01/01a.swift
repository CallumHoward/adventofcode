var nums: [Int] = []
while let line = readLine() {
  nums.append(Int(line)!)
}
print(zip(nums, nums[1...]).filter { $0.0 < $0.1 }.count)
