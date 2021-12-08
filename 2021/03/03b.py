from sys import stdin

def mode(nums, default: str, anti):
    if nums.count("1") == nums.count("0"):
        return default
    return "0" if (nums.count("1") <= len(nums) // 2) != anti else "1"

def rating(lines, default: str, anti = False):
    results = lines
    for i in range(len(lines[0])):
        mode_at_i = mode(list(zip(*results))[i], default, anti)
        results = [line for line in results if line[i] == mode_at_i]
        if len(results) <= 1:
            break
    return results

lines = [line.strip() for line in stdin.readlines()]
ox = rating(lines, "1")
co2 = rating(lines, "0", anti=True)
print(int("".join(ox), 2) * int("".join(co2), 2))
