// part1.cpp
// http://adventofcode.com/2017/day/4
// Callum Howard, 2018

#include <cassert>
#include <iostream>
#include <set>
#include <sstream>      // istringstream
#include <string>       // getline
#include <string_view>
#include <vector>

//std::vector<std::string> split(const std::string& input);
std::vector<std::string_view> split(std::string_view input);
bool no_duplicates(std::string_view line);
void test_no_duplicates();

int main() {
    test_no_duplicates();

    auto result = 0;

    for (auto line = std::string{}; std::getline(std::cin, line);) {
        if (no_duplicates(line.data())) { ++result; }
    }

    std::cout << result << '\n';

    return 0;
}

std::vector<std::string_view> split(const std::string_view input) {
    auto results = std::vector<std::string_view>{};

    auto j = std::cbegin(input);
    for (auto i = j; i != std::cend(input); ++i) {
        if (*i == ' ') {
            results.emplace_back(&*j, std::distance(j, i));
            j = std::next(i);
        }
    }

    results.emplace_back(&*j, std::distance(j, std::cend(input)));

    return results;
}

bool no_duplicates(const std::string_view line) {
    auto words = std::set<std::string_view>();

    for (const auto word : split(line)) {
        if (not words.insert(word).second) { return false; }
    }

    return true;
}

void test_no_duplicates() {
    using namespace std::string_view_literals;
    assert(no_duplicates("aa bb cc dd ee"sv));
    assert(not no_duplicates("aa bb cc dd aa"sv));
    assert(no_duplicates("aa bb cc dd aaa"sv));
}
