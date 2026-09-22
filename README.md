# Task 02 — Structured Output

## Project Overview

This project demonstrates how to make an AI model return structured JSON data that code can reliably use.

The project uses a product review example. The model output is parsed as JSON and validated against a predefined Pydantic schema. If the output is invalid or does not match the schema, the program rejects it and retries.

## Requirements

* Python 3.8+
* Pydantic 2.x

## Project Structure

```text
task-02-structured-output/
├── structured_output.py
├── requirements.txt
└── README.md
```

## How It Works

The program follows this process:

1. A mock model generates a JSON response.
2. The program parses the response as JSON.
3. The JSON is validated against the `ProductReview` schema.
4. Invalid JSON or incorrect data types are rejected.
5. The program retries when validation fails.
6. The first valid response is returned as typed data.

## Schema

The expected output contains:

* `product` — string
* `sentiment` — positive, negative, or neutral
* `rating` — integer from 1 to 5
* `pros` — list of strings
* `cons` — list of strings
* `recommendation` — boolean

## Validation and Retry

The mock model intentionally produces invalid responses during the first two attempts.

* Attempt 1 fails because `rating` is returned as a string.
* Attempt 2 fails because `recommendation` is returned as a string.
* Attempt 3 matches the schema and is accepted.

This demonstrates that the application does not blindly trust model output.

## How to Run

Install the dependency:

```bash
pip install -r requirements.txt
```

Run the program:
