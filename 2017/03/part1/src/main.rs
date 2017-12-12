// Advnet of Code day 3

struct Point {
    x: i32, // 10km
    y: i32,
}

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


fn go(p: Point, d: Direction) -> Point {
    return Point {x: p.x + d.x, y: p.y + d.y};
}

fn next_odd_square(input: i32) -> i32 {
    let n = (input as f32)
        .sqrt()
        .floor() as i32;
    if is_even(n) { n + 1 } else { n + 2 }
}

fn is_even(n: i32) -> bool {
    n % 2 == 0
}

fn main() {
    let card = Cardinality {
        n: Direction{x: 0,  y: 1},
        s: Direction{x: 0,  y:-1},
        e: Direction{x: 1,  y: 0},
        w: Direction{x:-1,  y: 0},
    };

    let p = Point{x: 0, y: 0};
    let p = go(p, card.e);

    //println!("{}, {}", p.x, p.y);



}
