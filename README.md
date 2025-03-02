# Stripe Bulk Promocode Generator

A Python tool to generate multiple Stripe promotion codes in bulk.

## Usage

You can run the tool in 3 ways:

1. Using uvx:

First [install uvx](https://docs.astral.sh/uv/getting-started/installation/), then run

```bash
uvx stripe-bulk-promocodes
```

2. Using pip then the command line:

```bash
pip install stripe-bulk-promocode-generator
```

```bash
stripe-bulk-promocode-generator
```

3. Using pip then within a Python script:

```bash
pip install stripe-bulk-promocode-generator
```

```python
from stripe_bulk_promocode_generator.main import create_promotion_codes

create_promotion_codes(
    coupon_id="your_coupon_id",
    num_coupons=10,
    prefix="PROMO"  # optional
)
```

## Configuration

The tool requires a Stripe secret key. You can provide it in two ways:

1. Enter it when prompted
2. Set it in a `.env` file:

```
STRIPE_SECRET_KEY=your_stripe_secret_key
```

## Features

- Generate multiple promotion codes at once
- Optional prefix for promotion codes
- Automatic expiration after 1 year
- First-time transaction restriction
- Single-use codes (max 1 redemption)
- Saves codes to a text file

## License

MIT License
