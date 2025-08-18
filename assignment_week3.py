def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, applies the discount.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

        # Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price != original_price:
    print(f"The final price after discount is: ${final_price:.2f}")
else:
    print(f"The original price is: ${original_price:.2f} (No discount applied)")


    print("Please enter valid numeric values for price and discount.")