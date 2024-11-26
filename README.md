# Stripe Promotion Code Generator

This script generates a large number of Stripe promotion codes with a specific prefix and expiration date. It uses the Stripe API to create the promotion codes. It's useful for partnerships where you can give a partner a unique coupon code for each customer.

How to use this:

1. Install the dependencies with `pip install -r requirements.txt`.
2. Copy the `.env.example` file to `.env.local` and generate a Stripe API key and put it in the `.env.local` file.
3. Create a coupon in Stripe for the desired product (e.g. a $100 off coupon).
4. Run the script with `python main.py` and enter the desired number of coupons to generate and the coupon ID.
