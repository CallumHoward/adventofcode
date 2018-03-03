// part1.cpp
// http://adventofcode.com/2017/day/5

#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <vector>

auto read_input()
{
   auto instructions = std::vector<int>{};
   std::copy(std::istream_iterator<int>{std::cin}, std::istream_iterator<int>{},
      std::back_inserter(instructions));

   if (not std::cin.eof()) {
      std::cerr << "Bad reading.\n";
      std::exit(1);
   }

   return instructions;
}

auto solve(std::vector<int> instructions) noexcept
{
   auto steps = 0;
   using std::size;
   for (auto i = decltype(size(instructions)){}; i < size(instructions); ++steps) {
      i += instructions[i]++;
   }

   return steps;
}

int main()
{
   assert(solve({0, 3, 0, 1, -3}) == 5);

   std::cout << solve(read_input()) << '\n';
}
