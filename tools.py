import random

def greet(name: str) -> str:
    """Generate a greeting message"""
    return f"Hello, {name}!"

def roll_dice(n_dice: int) -> list[int]:
    """Roll n_dice 6-sided dice and return results"""
    return [random.randint(1, 6) for _ in range(n_dice)]

def generate_lottery_numbers() -> list[int]:
    """Generate 6 unique random numbers between 1 and 49"""
    return sorted(random.sample(range(1, 50), 6))
