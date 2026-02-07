import re
raw_data = """
User Database Dump:
1. Name: Alice Smith, Email: alice.smith@example.com, Phone: 555-123-4567
2. Name: Bob Jones, Email: bob_j@work-place.org, Phone: (Invalid)
3. Name: Charlie, Email: charlie123@gmail.com, Phone: 555-987-6543
4. [SENSITIVE] Password: 123456
5. [SENSITIVE] Credit Card: 4444-5555-6666-7777
"""
# Extracting valid email addresses
emails = re.findall(r'\w+[\w\.-]*@\w+[\w\.-]+\.\w+', raw_data)
print("Extracted Emails:")
for email in emails:
    print(email)
# Extracting valid phone numbers
phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', raw_data)
print("\nExtracted Phone Numbers:") 
for phone in phone_numbers:
    print(phone)
# Masking sensitive information
masked_data = re.sub(r'\b\d{6}\b', '******', raw_data)  # Masking passwords
masked_data = re.sub(r'\b\d{4}[-.]?\d{4}[-.]?\d{4}[-.]?\d{4}\b', '****-****-****-****', masked_data)  # Masking credit card numbers
print("\nMasked Data:") 
print(masked_data)  
