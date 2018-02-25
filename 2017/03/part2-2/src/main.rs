// Advent of Code day 3

use std::io::stdin;
use std::collections::HashMap;
use std::hash::{Hash, Hasher};

// custom types
#[derive(Clone, Copy)]
struct Point {
    x: i32, // 10km
    y: i32,
}

impl PartialEq for Point {
    fn eq(&self, rhs: &Point) -> bool {
        self.x == rhs.x && self.y == rhs.y
    }
}
impl Eq for Point {}
impl Hash for Point {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.x.hash(state);
        self.y.hash(state);
    }
}

struct Direction {
    x: i32, // 30deg
    y: i32,
}

struct Cardinality {
    n: Direction,
    ne: Direction,
    e: Direction,
    se: Direction,
    s: Direction,
    sw: Direction,
    w: Direction,
    nw: Direction,
}

// globals
const CARD: Cardinality = Cardinality {
    n: Direction{x: 0,  y:-1},
    ne: Direction{x: 1, y:-1},
    e: Direction{x: 1, y: 0},
    se: Direction{x: 1, y:1},
    s: Direction{x: 0, y: 1},
    sw: Direction{x: -1, y: 1},
    w: Direction{x:-1, y: 0},
    nw: Direction{x: -1, y: -1},
};

const ALL_DIRECTIONS: [Direction; 8] = [
        CARD.n,
        CARD.ne,
        CARD.e,
        CARD.se,
        CARD.s,
        CARD.sw,
        CARD.w,
        CARD.nw];


fn neighbours(p: &Point) -> Vec<Point> {
    ALL_DIRECTIONS.iter().map(|direction| go(p, direction)).collect()
}

fn go(p: &Point, d: &Direction) -> Point {
    Point{
        x: p.x + d.x,
        y: p.y + d.y
    }
}

fn spiral(square_root: i32) -> [(Direction, i32); 5] {
    [
        (CARD.e, 1),
        (CARD.n, square_root),
        (CARD.w, square_root + 1),
        (CARD.s, square_root + 1),
        (CARD.e, square_root + 1),
    ]
}

fn is_odd(n: i32) -> bool {
    n % 2 == 1
}

fn solve(target: i32) -> i32 {
    // key = Point, value = solution for point
    let mut solutions = HashMap::new();
    let mut current_point = Point{x:0, y:0};
    solutions.insert(current_point, 1);

    // for each spiral
    for odd_root in (1..).filter(|&x| is_odd(x)) {
        // for each point in the spiral
        let s = spiral(odd_root);
        for &(ref direction, distance) in s.iter() {
            for _ in 0..distance {
                // move our current position
                current_point = go(&current_point, direction);

                // sum the neighbours' solution values
                let sum = neighbours(&current_point)
                        .iter()
                        .filter_map(|neighbour| solutions.get(neighbour))
                        .sum();

                // add solution to the map
                solutions.insert(current_point, sum);

                //println!("({}, {}), {}", );

                // exit when we have exceeded the target
                if sum > target {
                    return sum;
                }
            }
        }
    }

    0
}

fn main() {
    let mut input = String::new();

    stdin().read_line(&mut input)
        .expect("failed to read line");

    let input: i32 = input.trim().parse()
        .expect("Please type a number!");

    println!("{}", solve(input));
}
