import re

def remove_irrelevant_sections(description):
    """
    Removes irrelevant sections such as "About the Company," "Perks & Benefits," 
    and "Responsibilities" from a job description.

    Args:
        description (str): The job description as a string.

    Returns:
        str: The cleaned job description with irrelevant sections removed.
    """
    # Define regex patterns for sections to remove
    patterns = [
        r"(About the Company:|Our Mission:).*?(?=(Qualifications|Requirements|Skills|Experience|$))",
        r"(Perks & Benefits:|What We Offer:).*?(?=(Qualifications|Requirements|Skills|Experience|$))",
        r"(Responsibilities:).*?(?=(Qualifications|Requirements|Skills|Experience|$))"
    ]
    
    # Remove each pattern
    for pattern in patterns:
        description = re.sub(pattern, "", description, flags=re.IGNORECASE | re.DOTALL)
    
    return description.strip()

def extract_qualifications_from_html(description):
    """
    Extracts sections of a job description that begin with keywords like 
    "Qualifications," "Requirements," "Skills," or "Experience."

    Args:
        description (str): The job description as a string.

    Returns:
        str: The relevant section containing qualifications, or the original 
             description if no match is found.
    """
    # Search for sections starting with relevant keywords
    match = re.search(
        r"(Qualifications|Requirements|Skills|Experience).*",
        description,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        # Extract the matched section
        relevant_section = match.group(0)
        return relevant_section
    return description

def remove_eoe_notes(description):
    """
    Removes Equal Opportunity Employer (EOE) notes and similar boilerplate text 
    from a job description.

    Args:
        description (str): The job description as a string.

    Returns:
        str: The cleaned job description with EOE notes removed.
    """
    # Define regex patterns for common EOE notes
    patterns = [
        r"an equal opportunity employer.*?(?=\n|$)",  # Common phrasing
        r"EOE.*?(?=\n|$)",  # Short form
        r"EEO.*?(?=\n|$)",
        r"equal employment*?(?=\n|$)",  # Full boilerplate
        r"Equal employment opportunity.*?(?=\n|$)"  # Variations
    ]
    
    # Remove each pattern from the description
    for pattern in patterns:
        description = re.sub(pattern, "", description, flags=re.IGNORECASE | re.DOTALL)
    
    return description.strip()

