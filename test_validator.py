
# Import the validator function.
from validator import validate_answer

# Create a valid JSON response for testing.
test_response = '''
{
    "answer": "We open at 8:00 AM.",
    "category": "opening_hours",
    "found": true
}
'''

# Pass the response to the validator.
result = validate_answer(test_response)

# Display the validation result.
if result is not None:
    print("AI response is valid!")
    print(result)
else:
    print("AI response is invalid!")
