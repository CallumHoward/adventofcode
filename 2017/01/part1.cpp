#include <algorithm>    // rotate_copy, transform
#include <iostream>
#include <iterator>     // istringstream
#include <numeric>      // accumulate
#include <vector>

int main() {
    auto ss = std::string{};
    std::cin >> ss;
    const auto input = std::vector<char>{ss.cbegin(), ss.cend()};

    const auto shift = input.size() / 2;
    auto shifted_input = std::vector<char>{};
    std::rotate_copy(input.cbegin(), input.cbegin() + shift, input.cend(), std::back_inserter(shifted_input));

    auto repeated = std::vector<int>{};
    std::transform(input.begin(), input.end(), shifted_input.begin(), std::back_inserter(repeated),
            [](auto x, auto y) { return x == y ? x - '0' : 0; });
    std::cout << std::accumulate(repeated.cbegin(), repeated.cend(), 0) << "\n";

    return 0;
}
