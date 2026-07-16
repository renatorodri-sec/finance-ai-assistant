def format_currency(value):
    return f"R$ {value:,.2f}"


def validate_number(value):
    try:
        return float(value)
    except ValueError:
        return None


def print_separator():
    print("=" * 40)
