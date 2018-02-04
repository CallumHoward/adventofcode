// part1.cpp
// http://adventofcode.com/2017/day/4
// Callum Howard, 2018

#include <cassert>
#include <iostream>
#include <set>
#include <sstream>      // istringstream
#include <string>       // getline
#include <vector>

std::vector<std::string> split(const std::string& input);
bool no_duplicates(const std::string& line);
void test_no_duplicates();

int main() {
    test_no_duplicates();

    auto result = 0;

    for (auto line = std::string{}; std::getline(std::cin, line);) {
        if (no_duplicates(line)) { ++result; }
    }

    std::cout << result << '\n';

    return 0;
}

std::vector<std::string> split(const std::string& input) {
    auto iss = std::istringstream{input};

    return std::vector<std::string>{std::istream_iterator<std::string>{iss},
            std::istream_iterator<std::string>{}};
}

bool no_duplicates(const std::string& line) {
    auto words = std::set<std::string>();

    for (const auto& word : split(line)) {
        if (words.find(word) != std::cend(words)) { return false; }
        words.insert(word);
    }

    return true;
}

void test_no_duplicates() {
    assert(no_duplicates("aa bb cc dd ee"));
    assert(not no_duplicates("aa bb cc dd aa"));
    assert(no_duplicates("aa bb cc dd aaa"));
}
