# Math Toys API

A simple AWS Lambda-powered API that exposes various mathematical functions via HTTP GET requests.

## Overview

This API provides endpoints to calculate various mathematical values such as:
- **Phi (Golden Ratio)** for each power up to the one specified
- **Decimal expansions** for fractions and reciprocals
- **Pythagorean triples** based on corner difference
- **Reciprocal** for the reciprocal of a specified number


## API Endpoints

### 1. `/phi/{power}`

Calculates **phi** (the Golden Ratio) raised to each power up to the specified one.

- **Method**: GET
- **Path Parameter**: `power` (integer, the exponent to which phi is raised)
- **Example**:
  - Request: `GET /phi/5`
  - Response:
    ```json
    {
      "description": "phi to the power of 5",
      "data": [
        { "nth": 1, "fraction": "(1 V5 + 1) / 2", "[a*V5, b]": [2.23606797749979, 1], "diff": 1.2360679774997898, "[F, L]": [1, 1] },
        { "nth": 2, "fraction": "(1 V5 + 3) / 2", "[a*V5, b]": [2.23606797749979, 3], "diff": -0.7639320225002102, "[F, L]": [1, 3] },
        ...
      ]
    }
    ```

### 2. `/dc/{denom}`

Generates the decimal expansion for each fraction of a given denominator.

- **Method**: GET
- **Path Parameter**: `denom` (integer, the denominator of the fraction)
- **Example**:
  - Request: `GET /dc/7`
  - Response:
    ```json
    {
      "description": "decimal expansion for denominator 7",
      "data": [
        { "non_repeating": "", "repeating_1": "142", "repeating_complement": "857", "period_length": 6, "repeating": 6, "period": "142857" },
        { "non_repeating": "", "repeating_1": "285", "repeating_complement": "714", "period_length": 6, "repeating": 6, "period": "285714" },
        ...
      ]
    }
    ```

### 3. `/recip/{denom}`

Generates the decimal expansion for the reciprocal of a given denominator.

- **Method**: GET
- **Path Parameter**: `denom` (integer, the denominator for which the reciprocal is calculated)
- **Example**:
  - Request: `GET /recip/17`
  - Response:
    ```json
    {
      "description": "decimal expansion for reciprocal of 5",
      "data": { "non_repeating": "", "repeating_1": "05882352", "repeating_complement": "94117647", "period_length": 16, "repeating": 16, "period": "0588235294117647" }
    }
    ```

### 4. `/pythag/{corner}`

Returns a list of **Pythagorean triples** where the difference between the hypotenuse and the second leg equals the specified corner.

- **Method**: GET
- **Path Parameter**: `corner` (integer, the difference between hypotenuse and second leg)
- **Example**:
  - Request: `GET /pythag/1`
  - Response:
    ```json
    {
      "description": "Pythagorean triples where c - b = 2",
      "data": [
        { "a": 4, "b": 3, "c": 5, "is_primitive": true },
        { "a": 6, "b": 8, "c": 10, "is_primitive": false },
        { "a": 8, "b": 15, "c": 17, "is_primitive": true },
        ...
      ]
    }
    ```


## Usage Examples

### Example 1: Using cURL to call the API

```bash
curl https://api.math-toys.app/phi/3


fetch('https://api.math-toys.app/phi/3')
  .then(response => response.json())
  .then(data => console.log(data));
