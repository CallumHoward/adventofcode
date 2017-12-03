fn main() {

    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("read error");

    const RADIX: u32 = 10;
    let v: Vec<u32> = input.chars()
        .filter_map(|c| c.to_digit(RADIX)).collect();

    println!("{}", sum_if_repeated(v));
}

fn sum_if_repeated(v: Vec<u32>) -> u32 {
    let shift = 1;
    let shifted_it = v.iter().skip(v.len() - shift).chain(v.iter().take(shift));

    for (a, b) in v.iter().zip(shifted_it) {
        
    }

    1
}