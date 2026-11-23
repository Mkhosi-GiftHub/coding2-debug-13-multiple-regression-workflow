"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "883d275c92c38d5167e373d334ddaf53"
GRADE_HASH = "a54f20ce9ece8f2f2529bb0830d6b76a89d07acc81520ba274f824d2a33d8e9b"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
