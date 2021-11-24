// The io library comes from the standard library (std)
use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    //println!("The secret number is: {}", secret_number);

    loop {
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

        // This guess variable will shadow the previous shadow
        // The parse method on strings parses a string into some kind of number
        // but rust will infer the type to u32 since we have declared the variable
        // that way
        // The following code will crash the program if you enter a non-number
        //let guess: u32 = guess.trim().parse().expect("Please type a number!");
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        /*
          The cmp method compares two values and can be called on anything that can
          be compared. It takes a reference to whatever you want to compare with
        */
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
