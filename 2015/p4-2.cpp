// peter kydd pkydd@cse.unsw.edu.au
// advent of code, day4
// adventcoin

#include <iostream>
#include <cstdlib>
#include <regex>
#include <limits>

#include "md5.h"


unsigned int getSuffix(void);
bool leadingZeros(const std::string& str, int numZeros);

int main(int argc, char *argv[])
{
    int suffix = getSuffix();

    std::cout << "suff: " << suffix << std::endl;

    return EXIT_SUCCESS;
}

unsigned int getSuffix(void)
{
    int suffix = 0;
    
    std::string key;
    std::cin >> key;

    std::string toHash;
    
    while(suffix < std::numeric_limits<int>::max() ){

        toHash = key;
        toHash.append(std::to_string(suffix));

        std::string hash = md5(toHash);

        if(leadingZeros(hash, 6)){{
            return suffix;
        }

        /*
        if (suffix %100000 == 0){
            std::cout << "suffix value: " << suffix << std::endl;
        }
        */

        ++suffix;
    }

    return suffix;
}

// will simplify after testing
bool leadingZeros(const std::string& str, int numZeros)
{
    
    // ( OLD METHOD )
    //std::regex leadingZero("^0{6}");
    //return std::regex_search(str, leadingZero );
    
    unsigned int count = 0;
    while (count < str.size()){
        if(str[count] != '0'){
            break;
        }
        ++count;
    }
    return (count == numZeros);
}


