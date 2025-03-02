import time
import stripe
import os
from typing import Optional


def create_promotion_codes(
    coupon_id: str, num_coupons: int, prefix: Optional[str] = None
) -> None:
    """
    Create multiple Stripe promotion codes and save them to a file.

    Args:
        coupon_id: The Stripe coupon ID to associate with the promotion codes
        num_coupons: Number of promotion codes to generate
        prefix: Optional prefix to add to each promotion code
    """
    output_file = "promotion_codes.txt"
    if prefix:
        output_file = f"{prefix}codes.txt"

    for _ in range(num_coupons):
        random_code = os.urandom(4).hex()
        code = f"{prefix + '' if prefix else ''}{'-' if prefix else ''}{random_code}"
        try:
            promotion_code = stripe.PromotionCode.create(
                coupon=coupon_id,
                code=code,
                max_redemptions=1,
                restrictions={"first_time_transaction": True},
                active=True,
                expires_at=int(time.time())
                + (365 * 24 * 3600),  # Expiry defaults to 1 year
            )
            with open(output_file, "a") as f:
                f.write(f"{promotion_code.code}\n")
            print(f"Created promotion code: {promotion_code.code}")
        except Exception as e:
            print(f"Error creating promotion code: {e}")


def main() -> None:
    """Main entry point for the command-line interface."""
    # Get Stripe API key from input first
    api_key = input(
        "Enter your Stripe secret key (press Enter to use .env file): "
    ).strip()

    # If no key provided, try to load from .env
    if not api_key:
        from dotenv import load_dotenv

        load_dotenv()
        api_key = os.getenv("STRIPE_SECRET_KEY")
        if not api_key:
            raise ValueError("STRIPE_SECRET_KEY not found in input or .env file")

    stripe.api_key = api_key

    # Get user inputs
    coupon_id = input("Enter the coupon ID: ").strip()
    if not coupon_id:
        raise ValueError(
            "Coupon ID is required. Please create a coupon in Stripe first."
        )

    try:
        num_coupons = int(input("Enter the number of coupons to generate: "))
        if num_coupons <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Please enter a valid positive number of coupons to generate.")

    # Get optional prefix
    prefix = (
        input("Enter prefix for promotion codes (press Enter to skip): ").strip()
        or None
    )

    # Create the promotion codes
    create_promotion_codes(coupon_id, num_coupons, prefix)


if __name__ == "__main__":
    main()
