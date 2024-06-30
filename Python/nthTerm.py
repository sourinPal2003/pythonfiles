def calculate_nth_term_in_series(n):
    if n % 2 == 0:  
        power = n // 2
        nth_term = 2 ** power
    else: 
        power = n // 2
        nth_term = 3 ** power
    return nth_term

if __name__ == "__main__":
    user_input = int(input("Enter the value of n: "))  
    resulting_nth_term = calculate_nth_term_in_series(user_input - 1) 
    print(f"The element is: {resulting_nth_term}")
