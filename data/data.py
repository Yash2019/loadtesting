from faker import Faker
import csv
import random

fake = Faker("en_IN")

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "roll_number",
        "name",
        "maths",
        "physics",
        "chemistry",
        "total",
    ])

    for i in range(1, 100_001):
        maths, physics, chemistry = (
            random.randint(20, 100) for _ in range(3)
        )

        writer.writerow([
            f"2026{i:07d}",
            fake.name(),
            maths,
            physics,
            chemistry,
            maths + physics + chemistry,
        ])