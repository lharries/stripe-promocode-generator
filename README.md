# Stripe Bulk Promocode Generator

A Python tool to generate multiple Stripe promotion codes in bulk.

It's designed to be run as a CLI tool, but can also be used as a Python package.

It's hosted on [pypi here](https://pypi.org/project/stripe-bulk-promocode-generator/)

## Usage

You can run the tool in 2 ways:

1. Using uvx:

First [install uvx](https://docs.astral.sh/uv/getting-started/installation/), then run

```bash
uvx stripe-bulk-promocode-generator
```

2. Clone this repo then run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit the .env file with your Stripe secret key
python3 stripe_bulk_promocode_generator/main.py
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
