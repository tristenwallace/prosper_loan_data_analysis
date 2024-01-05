def map_occupation_to_isco(occupation: str) -> str:
    """
    Map an occupation to its corresponding ISCO category name.

    Args:
    occupation (str): The occupation to be mapped.

    Returns:
    str: The ISCO category name.
    
    ISCO Categories:
        Managers
        Professionals
        Technicians and Associate Professionals
        Clerical Support Workers
        Service and Sales Workers
        Skilled Agricultural, Forestry and Fishery Workers
        Craft and Related Trades Workers
        Plant and Machine Operators, and Assemblers
        Elementary Occupations
        Armed Forces Occupations
    """

    # Define mapping of occupations to shortened ISCO category names
    mapping = {
        'Other': None,
        'Professional': 'Professionals',
        'Skilled Labor': 'Craft Workers',
        'Executive': 'Managers',
        'Sales - Retail': 'Service/Sales',
        'Laborer': 'Elementary',
        'Food Service': 'Service/Sales',
        'Fireman': 'Skilled Agr/Forestry',
        'Waiter/Waitress': 'Service/Sales',
        'Construction': 'Craft Workers',
        'Computer Programmer': 'Professionals',
        'Sales - Commission': 'Service/Sales',
        'Retail Management': 'Managers',
        'Engineer - Mechanical': 'Professionals',
        'Military Enlisted': 'Armed Forces',
        'Clerical': 'Clerical Support',
        'Teacher': 'Professionals',
        'Clergy': 'Professionals',
        'Accountant/CPA': 'Professionals',
        'Attorney': 'Professionals',
        'Nurse (RN)': 'Professionals',
        'Analyst': 'Professionals',
        "Nurse's Aide": 'Technicians',
        'Investor': 'Other',
        'Realtor': 'Professionals',
        'Flight Attendant': 'Service/Sales',
        'Nurse (LPN)': 'Technicians',
        'Military Officer': 'Armed Forces',
        'Food Service Management': 'Managers',
        'Truck Driver': 'Operators/Assemblers',
        'Administrative Assistant': 'Clerical Support',
        'Police Officer/Correction Officer': 'Skilled Agr/Forestry',
        'Social Worker': 'Professionals',
        'Tradesman - Mechanic': 'Craft Workers',
        'Medical Technician': 'Technicians',
        'Professor': 'Professionals',
        'Postal Service': 'Clerical Support',
        'Civil Service': 'Clerical Support',
        'Pharmacist': 'Professionals',
        'Tradesman - Electrician': 'Craft Workers',
        'Scientist': 'Professionals',
        'Dentist': 'Professionals',
        'Engineer - Electrical': 'Professionals',
        'Architect': 'Professionals',
        'Landscaping': 'Skilled Agr/Forestry',
        'Tradesman - Carpenter': 'Craft Workers',
        'Bus Driver': 'Operators/Assemblers',
        'Tradesman - Plumber': 'Craft Workers',
        'Engineer - Chemical': 'Professionals',
        'Doctor': 'Professionals',
        'Chemist': 'Professionals',
        'Student - College Senior': None,
        'Principal': 'Managers',
        "Teacher's Aide": 'Technicians',
        'Pilot - Private/Commercial': 'Operators/Assemblers',
        'Religious': 'Professionals',
        'Homemaker': None,
        'Student - College Graduate Student': None,
        'Student - Technical School': None,
        'Psychologist': 'Professionals',
        'Biologist': 'Professionals',
        'Student - College Sophomore': None,
        'Judge': 'Professionals',
        'Student - College Junior': None,
        'Car Dealer': 'Service/Sales',
        'Student - Community College': None,
        'Student - College Freshman': None
    }

    return mapping.get(occupation, 'Other')

# Example usage
print(map_occupation_to_isco('Engineer - Mechanical')) # Expected output: 'Professionals'

# Assuming df is your DataFrame and 'occupation' is the column name
# Transform each occupation to its new ISCO category
# for index, row in df.iterrows():
#     df.at[index, 'occupation'] = map_occupation_to_isco(row['occupation'])