// getline_test.cpp
// Callum Howard, 2018

#include <iostream>
#include <string>


int main() {

    for (auto buffer = std::string{}; std::getline(std::cin, buffer);) {
        std::cout << buffer << '\n';
    }

    return 0;
}
