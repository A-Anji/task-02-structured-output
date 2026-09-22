import json
from pydantic import BaseModel, Field, ValidationError
from typing import List


# 1. Schema
class ProductReview(BaseModel):
    product: str
    sentiment: str = Field(pattern="^(positive|negative|neutral)$")
    rating: int = Field(ge=1, le=5)
    pros: List[str]
    cons: List[str]
    recommendation: bool


# 2. Mock model
def mock_model(attempt):
    responses = [
        '{"product": "laptop", "sentiment": "positive", "rating": "five"}',

        '{"product": "laptop", "sentiment": "positive", "rating": 5, '
        '"pros": ["fast", "good display"], "cons": ["heavy"], '
        '"recommendation": "yes"}',

        '{"product": "laptop", "sentiment": "positive", "rating": 5, '
        '"pros": ["fast", "good display"], "cons": ["heavy"], '
        '"recommendation": true}'
    ]

    return responses[attempt - 1]


# 3. Generate and validate
def get_valid_review(max_retries=3):

    for attempt in range(1, max_retries + 1):

        print(f"\nAttempt {attempt}")

        try:
            # Get model response
            response = mock_model(attempt)
            print("Model output:", response)

            # Parse JSON
            data = json.loads(response)

            # Validate against schema
            review = ProductReview.model_validate(data)

            print("✓ Valid output")
            return review

        except json.JSONDecodeError:
            print("✗ Invalid JSON. Retrying...")

        except ValidationError as error:
            print("✗ Schema validation failed.")
            print("Retrying...")

    raise ValueError("Could not obtain valid structured output.")


# 4. Run program
if __name__ == "__main__":

    review = get_valid_review()

    print("\nFinal validated result:")
    print(review.model_dump_json(indent=2))