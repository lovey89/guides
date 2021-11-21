// The io library comes from the standard library (std)
use std::io;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    // The 'mut' keyword makes the variable mutable
    // In Rust, variables are immutable by default
    let mut guess = String::new();

    // If the 'use' import on the second line wasn't present we could have written
    // std::io::stdin
    io::stdin()
        // Append (don't overwrite) the guess string
        // & indicates that this is a reference
        // references are also immutable, so we need to use mut once again
        .read_line(&mut guess)
        // A Result enum is returned indicating either 'Ok' or 'Err'
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}
