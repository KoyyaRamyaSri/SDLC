# prompt: generate python code to implement Smart SDLC - AI - Enhanced Software Development LifeCycle in Online Shopping (here we need the code with fixing bugs also and futher implementing features using AI) {output need virtual explaination }

# Install necessary libraries (if not already installed)
!pip install spacy
!python -m spacy download en_core_web_sm

import spacy

# --- Simulated Requirement Analysis ---
def analyze_requirement_with_ai(requirement_text):
    """
    Simulates AI analysis of a requirement using NLP.
    In a real scenario, this would involve more sophisticated models.
    """
    print("\n--- AI-Enhanced Requirement Analysis ---")
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(requirement_text)

    print(f"Original Requirement: {requirement_text}")
    print("Identified Entities:")
    for ent in doc.ents:
        print(f"- {ent.text} ({ent.label_})")

    # Simple rule: Check for keywords related to payment or pricing
    if "price" in requirement_text.lower() or "payment" in requirement_text.lower():
        print("AI Suggestion: Ensure robust handling of currency and tax calculations.")
    if "users" in requirement_text.lower() or "customers" in requirement_text.lower():
         print("AI Suggestion: Consider user authentication and authorization requirements.")

    print("--- End Requirement Analysis ---")

# --- Simulated Bug Fixing (Example: Price Calculation Bug) ---

# Defective code with a potential bug
def calculate_total_price_defective(price, quantity, discount_percentage):
    """
    Calculates total price, but has a potential bug with discount application.
    """
    subtotal = price * quantity
    # Bug: Discount is applied incorrectly (e.g., not handled as a percentage)
    discount_amount = subtotal * discount_percentage # This should likely be discount_percentage / 100
    total = subtotal - discount_amount
    return total

# Hypothetical AI bug detection and suggestion (rule-based for this example)
def ai_suggest_bug_fix_price_calculation(code_snippet):
    """
    Simulates AI detecting a common price calculation bug and suggesting a fix.
    In a real scenario, this would involve code analysis models.
    """
    print("\n--- AI-Enhanced Bug Detection and Fixing ---")
    print("Analyzing code snippet for potential price calculation issues...")

    if "subtotal * discount_percentage" in code_snippet and "/" not in code_snippet.split("discount_percentage")[0]:
        print("AI Detected Potential Bug: Discount is likely being applied as a raw value instead of a percentage.")
        print("AI Suggested Fix: Change 'subtotal * discount_percentage' to 'subtotal * (discount_percentage / 100)'.")
    else:
        print("AI Analysis: No obvious price calculation bugs detected in this snippet.")
    print("--- End Bug Detection and Fixing ---")

# Fixed code
def calculate_total_price_fixed(price, quantity, discount_percentage):
    """
    Fixed calculation of total price.
    """
    subtotal = price * quantity
    # Fixed: Correctly apply the discount as a percentage
    discount_amount = subtotal * (discount_percentage / 100)
    total = subtotal - discount_amount
    return total

# --- Simulated Test Case Generation ---

def generate_test_cases_for_price_calculation(function_name):
    """
    Simulates AI generating basic test cases for a price calculation function.
    In a real scenario, this would involve analyzing function signature and logic.
    """
    print("\n--- AI-Enhanced Test Case Generation ---")
    print(f"Generating test cases for function: {function_name}")

    test_cases = [
        {"price": 10, "quantity": 2, "discount_percentage": 0, "expected_output": 20},
        {"price": 10, "quantity": 1, "discount_percentage": 10, "expected_output": 9},
        {"price": 20, "quantity": 3, "discount_percentage": 25, "expected_output": 45},
        {"price": 5, "quantity": 0, "discount_percentage": 10, "expected_output": 0}, # Edge case: quantity is 0
    ]

    print("Generated Test Cases:")
    for i, tc in enumerate(test_cases):
        print(f"Test Case {i+1}: Input={tc['price']}, {tc['quantity']}, {tc['discount_percentage']} Expected Output={tc['expected_output']}")

    print("--- End Test Case Generation ---")
    return test_cases

# --- Running the Simulation ---

# Example Requirement
online_shopping_requirement = "As a customer, I want to be able to add products to my cart and see the total price, including any applicable discounts, before proceeding to payment."
analyze_requirement_with_ai(online_shopping_requirement)

# Analyze the defective code for bugs
defective_code_snippet = """
def calculate_total_price_defective(price, quantity, discount_percentage):
    subtotal = price * quantity
    discount_amount = subtotal * discount_percentage
    total = subtotal - discount_amount
    return total
"""
ai_suggest_bug_fix_price_calculation(defective_code_snippet)

# Test the defective function
print("\n--- Testing Defective Function ---")
test_cases = generate_test_cases_for_price_calculation("calculate_total_price_defective")
for tc in test_cases:
    actual_output = calculate_total_price_defective(tc['price'], tc['quantity'], tc['discount_percentage'])
    print(f"Input: {tc['price']}, {tc['quantity']}, {tc['discount_percentage']}, Expected: {tc['expected_output']}, Actual: {actual_output}")
    if actual_output != tc['expected_output']:
        print("BUG DETECTED!")
    else:
        print("Test Passed")

# Test the fixed function
print("\n--- Testing Fixed Function ---")
for tc in test_cases:
    actual_output = calculate_total_price_fixed(tc['price'], tc['quantity'], tc['discount_percentage'])
    print(f"Input: {tc['price']}, {tc['quantity']}, {tc['discount_percentage']}, Expected: {tc['expected_output']}, Actual: {actual_output}")
    if actual_output != tc['expected_output']:
        print("BUG DETECTED!") # This should not happen with the fixed function
    else:
        print("Test Passed")


# prompt: prompt: generate python code to implement Smart SDLC - AI - Enhanced Software Development LifeCycle in Online Shopping (here we need the code with fixing bugs also and futher implementing features using AI) {output need virtual explaination } include payment details also

# --- Simulated AI-Enhanced Payment Processing ---

def simulate_payment_processing(amount, payment_method, payment_details):
    """
    Simulates processing a payment with hypothetical AI assistance for validation or fraud detection.
    In a real scenario, this would integrate with payment gateways.
    """
    print("\n--- AI-Enhanced Payment Processing ---")
    print(f"Attempting to process payment of {amount} using {payment_method}...")

    # Hypothetical AI validation/fraud check
    is_valid_payment = ai_validate_payment(payment_details)

    if is_valid_payment:
        print("AI Analysis: Payment details appear valid and not flagged for fraud.")
        # Simulate successful payment processing
        print("Payment successful!")
        return True
    else:
        print("AI Analysis: Payment details flagged as potentially invalid or suspicious.")
        print("Payment failed.")
        return False

def ai_validate_payment(payment_details):
    """
    Simulates AI validating payment details. This could involve checking for
    anomalies, known fraudulent patterns, etc.
    """
    print("AI performing payment validation...")
    # Simple rule: Reject if card number is a specific invalid pattern
    if "1111222233334444" in payment_details.get("card_number", ""):
        print("AI Flagged: Known invalid card number.")
        return False
    # Simple rule: Reject if expiry date is in the past
    import datetime
    from dateutil.parser import parse
    try:
        expiry_date_str = payment_details.get("expiry_date", "")
        if expiry_date_str:
            expiry_date = parse(expiry_date_str).date()
            if expiry_date < datetime.date.today():
                print("AI Flagged: Expired card.")
                return False
    except:
        print("AI Note: Could not parse expiry date for validation.")
        pass # Continue if date parsing fails

    # In a real system, much more complex AI models would be used here
    print("AI Validation: Details seem okay (simple check).")
    return True

# --- Further Implementing Features using AI ---

def ai_suggest_product_recommendations(user_history, current_product):
    """
    Simulates AI generating product recommendations based on user history and current product.
    """
    print("\n--- AI-Enhanced Product Recommendations ---")
    print(f"Analyzing user history: {user_history}")
    print(f"Considering current product: {current_product}")

    recommendations = []
    if "laptop" in user_history and "mouse" not in user_history and current_product == "laptop":
        recommendations.append("wireless mouse")
        recommendations.append("laptop bag")
    elif "book" in user_history and "ebook reader" not in user_history and current_product == "book":
        recommendations.append("ebook reader")
        recommendations.append("bookmark")
    elif "t-shirt" in user_history and current_product == "t-shirt":
        recommendations.append("jeans")
        recommendations.append("sneakers")

    if recommendations:
        print("AI Suggested Recommendations:")
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("AI Analysis: No specific recommendations based on simple rules.")
    print("--- End Product Recommendations ---")
    return recommendations

def ai_generate_marketing_copy(product_description, key_features):
    """
    Simulates AI generating marketing copy for a product.
    """
    print("\n--- AI-Enhanced Marketing Copy Generation ---")
    print("Generating marketing copy...")

    copy = f"Introducing the {product_description}! "
    if key_features:
        copy += "Featuring: " + ", ".join(key_features) + ". "
    copy += "Shop now and experience the difference!"

    print(f"Generated Marketing Copy: {copy}")
    print("--- End Marketing Copy Generation ---")
    return copy

# --- Running the Extended Simulation ---

# Simulate a purchase process including payment
print("\n--- Simulating a Full Purchase with Payment ---")

# Assuming a calculated total price from previous steps
final_total_price = calculate_total_price_fixed(price=50, quantity=2, discount_percentage=10) # Example calculation
print(f"Calculated Final Price: {final_total_price}")

# Simulate collecting payment details
valid_payment_details = {
    "payment_method": "credit card",
    "card_number": "1234567890123456",
    "expiry_date": "2025-12-31",
    "cvv": "123"
}

invalid_card_payment_details = {
    "payment_method": "credit card",
    "card_number": "1111222233334444", # Known invalid
    "expiry_date": "2026-01-01",
    "cvv": "456"
}

expired_card_payment_details = {
    "payment_method": "credit card",
    "card_number": "9876543210987654",
    "expiry_date": "2020-01-01", # Expired
    "cvv": "789"
}


# Attempt valid payment
simulate_payment_processing(final_total_price, valid_payment_details["payment_method"], valid_payment_details)

# Attempt invalid card payment
simulate_payment_processing(final_total_price, invalid_card_payment_details["payment_method"], invalid_card_payment_details)

# Attempt expired card payment
simulate_payment_processing(final_total_price, expired_card_payment_details["payment_method"], expired_card_payment_details)


# Simulate using AI for recommendations
user_browse_history = ["book", "pen", "notebook"]
current_product_viewing = "book"
ai_suggest_product_recommendations(user_browse_history, current_product_viewing)

user_browse_history_2 = ["laptop", "monitor"]
current_product_viewing_2 = "laptop"
ai_suggest_product_recommendations(user_browse_history_2, current_product_viewing_2)


# Simulate using AI for marketing copy
product_desc = "High-Quality Wireless Mouse"
product_features = ["Ergonomic Design", "Long Battery Life", "Precise Tracking"]
ai_generate_marketing_copy(product_desc, product_features)

