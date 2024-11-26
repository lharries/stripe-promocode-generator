import concurrent.futures
import time
import stripe
import os

from dotenv import load_dotenv

load_dotenv(".env.local")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
COUPON_ID = input("Enter the coupon ID: ")
NUM_COUPONS = int(input("Enter the number of coupons to generate: "))

if not COUPON_ID:
    raise ValueError(
        "COUPON_ID is not set. Please create a coupon in Stripe and add the ID to the .env.local file."
    )
if not NUM_COUPONS:
    raise ValueError(
        "NUM_COUPONS is not set. Please enter the number of coupons to generate."
    )

# Generate promotion codes
NUM_THREADS = 1  # Adjust this to the number of threads you want to use
PREFIX = "11-"


def create_single_promotion_code(thread_id):
    random_code = os.urandom(4).hex()
    code = PREFIX + random_code
    try:
        promotion_code = stripe.PromotionCode.create(
            coupon=COUPON_ID,
            code=code,
            max_redemptions=1,
            restrictions={"first_time_transaction": True},
            active=True,
            expires_at=int(time.time())
            + (365 * 24 * 3600),  # Expiry defaults to 1 year
        )
        with open(f"{PREFIX}_{thread_id}.txt", "a") as f:
            f.write(f"{promotion_code.code}\n")
            print("writing")
    except Exception as e:
        print(f"Error creating promotion code: {e}")


def create_promotion_code(thread_id):
    for _ in range(NUM_COUPONS // NUM_THREADS):
        create_single_promotion_code(thread_id)


with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(create_promotion_code, range(NUM_THREADS))
