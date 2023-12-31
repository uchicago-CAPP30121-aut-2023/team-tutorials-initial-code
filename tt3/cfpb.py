"""
Team Tutorial #4: Dictionaries
CAPP 30121
"""

import json

CFPB_16 = json.load(open("cfpb16_1000.json"))

# Task 1
def find_companies(complaints):
    """
    Compute a list of companies complained about

    Args:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (list or set) of companies
    """

    # Your code goes here
    # replace [] with a suitable return value
    return []


# Task 2
def count_complaints_about(complaints, company_name):
    """
    Count complaints about a specified company

    Args:
        complaints (list) A list of complaints, where each complaint is a
            dictionary
        company_name (str): The company name to count complaints for

    Returns: (int) count of complaints
    """

    # Your code goes here
    # replace 0 with a suitable return value
    return 0


# Task 3
def count_by_state(complaints):
    """
    Compute counts by state of all complaints

    Args:
         complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) that relates states to complaint number
    """

    # Your code goes here
    # replace {} with a suitable return value
    return {}


# Task 4
def state_with_most_complaints(cnt_by_state):
    """
    Find the state with the most complaints. Can break ties arbitrarily.

    Args:
        cnt_by_state (dict) A dictionary relating each state to the
            count of complaints in that state

    Returns: (str) the state with the most complaints
    """

    # Your code goes here
    # replace "" with a suitable return value
    return ""


# Task 5
def count_by_company_by_state(complaints):
    """
    Computes a dict of {company: {state: count, state: count}} for all states
        and companies

    Args:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) with count per company per state
    """

    # Your code goes here
    # replace {} with a suitable return value
    return {}


# Task 6
def complaints_by_company(complaints):
    """
    Create a dictionary that maps the name of a company to a list of the
    complaint dictionaries that concern that company.

    Args:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) mapping the name of the company to a list of complaints
    """

    # Your code goes here
    # replace {} with a suitable return value
    return {}


# Task 7
def count_by_company_by_state_2(complaints):
    """
    Computes a dict of {company: {state: count, state: count}} for all states
        and companies

    Args:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) with count per company per state

    This implementation involves composing complaints_by_company with 
        count_by_state
    """

    # Your code goes here
    # replace {} with a suitable return value
    return {}
