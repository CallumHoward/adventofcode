#include <iostream>
#include <cstdlib>
#include <string>
#include "md5.h"

inline bool startsWith(std::string a, std::string b) {
    return !a.compare(0, b.length(), b);
}

int main(int argc, char *argv[]) {
    int count = 0;
    while (true) {
        if (startsWith(md5("ckczppom" + std::to_string(count)), "000000")) {
            std::cout << count << std::endl;
            break;
        }
        ++count;
    }

    return EXIT_SUCCESS;
}

