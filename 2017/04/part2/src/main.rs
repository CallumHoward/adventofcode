// part2
// http://adventofcode.com/2017/day/4

use std::collections::HashSet;
use std::io::{stdin, BufRead};

fn no_duplicates(passphrase: &str) -> bool {
    let mut words = HashSet::new();
    for mut i in passphrase.split_whitespace() {
        let mut chars : Vec<char> = i.chars().collect();
        chars.sort();
        let i: String = chars.into_iter().collect();
        if !words.insert(i) {
            return false;
        }
    }

    true
}

fn main() {
    let in_stream = stdin();

    let result = in_stream.lock()
        .lines()
        .filter_map(|x| x.ok())
        .filter(|x| no_duplicates(x))
        .count();

    println!("{}", result);

    assert!(no_duplicates("aa bb cc dd ee"));
    assert!(!no_duplicates("aa bb cc dd aa"));
    assert!(no_duplicates("aa bb cc dd aaa"));
}

//12 |         word = chars.into_iter().collect();
//   |                                  ^^^^^^^ a collection of type `&str` cannot be built from an iterator over elements of type `char`
