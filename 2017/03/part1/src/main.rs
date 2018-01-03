// Advent of Code day 3

use std::io::stdin;

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

struct Direction {
    x: i32, // 30deg
    y: i32,
}

struct Cardinality {
    n: Direction,
    s: Direction,
    e: Direction,
    w: Direction,
}


fn go(p: &Point, d: &Direction) -> Point {
    Point{
        x: p.x + d.x,
        y: p.y + d.y
    }
}

fn prev_odd_square(input: i32) -> i32 {
    let n = (input as f32)
        .sqrt()
        .floor() as i32;
    if is_even(n) {
        n - 1
    } else {
        n
    }
}

fn find_diagonal(square_root: i32) -> Point {
    Point{
        x: square_root / 2,
        y: square_root / 2
    }
}

fn is_even(n: i32) -> bool {
    n % 2 == 0
}

fn manhattan(point: Point) -> i32 {
    point.x.abs() + point.y.abs()
}

fn solve(target: i32) -> i32 {
    let card = Cardinality {
        n: Direction{x: 0,  y:-1},
        s: Direction{x: 0,  y: 1},
        e: Direction{x: 1,  y: 0},
        w: Direction{x:-1,  y: 0},
    };

    let square_root = prev_odd_square(target);
    let mut destination = find_diagonal(square_root);
    let mut index = square_root * square_root;

    for &(direction, distance) in [(&card.e, 1),
                                    (&card.n, square_root),
                                    (&card.w, square_root + 1),
                                    (&card.s, square_root + 1),
                                    (&card.e, square_root + 1)].iter() {
        for _ in 0..distance {
            if index == target { return manhattan(destination); }
            destination = go(&destination, &direction);
            index += 1;
        }
    }

    manhattan(destination)


}

fn main() {
    let mut input = String::new();

    stdin().read_line(&mut input)
        .expect("failed to read line");

    let input: i32 = input.trim().parse()
        .expect("Please type a number!");

    println!("{}", solve(input));
}
