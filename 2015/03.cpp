// 03.cpp
// Advent of Code
// Callum Howard 2016

#include <iostream>
#include <cstdlib>
#include <utility>
#include <unordered_set>
#include <string>


inline const std::string coord(int x, int y) {
    return std::to_string(x) + "," + std::to_string(y);
}


int main(int argc, char *argv[]) {
    auto input = std::string{};
    std::cin >> input;

    auto loc_x = int{0};
    auto loc_y = int{0};
    auto houses = std::unordered_set<std::string>{coord(loc_x, loc_y)};

    for (auto direction : input) {
        switch (direction) {
            case '<' : --loc_x; break;
            case '>' : ++loc_x; break;
            case '^' : ++loc_y; break;
            case 'v' : --loc_y; break;
        }
        houses.insert(coord(loc_x, loc_y));
    }

    std::cout << houses.size() << std::endl;

    return EXIT_SUCCESS;
}
