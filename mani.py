# Original content as a string
content = """
1. *Cheryl Strayed and Houghton Mifflin Company: - **Date of Agreement: January 26, 2004 - **Work: "Torch" - **Advance: $100,000 - **Rights: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide - **Manuscript Delivery: 110,000 to 130,000 words by June 30, 2004 - [Contract Details](#doc9) 
2. **Alyssa Satin Capucilli and HarperCollins Children's Books: - **Date of Agreement: November 1, 1994 - **Work: "Biscuit (An I Can Read Book)" - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - **Manuscript Delivery: Complete manuscript suitable for a 24-page book - [Contract Details](#doc3) 
3. **John Atkinson and HarperCollins Publishers LLC: - **Date of Agreement: September 25, 2017 - **Work: "ABRIDGED CLASSICS: Tiny Versions of Classic Tomes" - **Advance: $15,000 - **Description: A collection of approximately 2,500 words with 100 four-color illustrations - [Contract Details](#doc5) 
4. **Laura Numeroff and HarperCollins Publishers Inc.: - **Date of Agreement: December 30, 1998 - **Work: "If You Give a Moose a Muffin" - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - **Manuscript Delivery: Complete and final manuscript by November 15, 2000 - [Contract Details](#doc7) 
5. *Adam Silvera and HarperCollins Publishers LLC: - **Date of Agreement: October 9, 2015 - **Works: Two works by the author - **Rights: Worldwide, all languages - **Publication Date: Within 18 months of acceptance.
"""

# Split the content into individual contracts
contracts = content.strip().split("\n")

# Process each contract
formatted_contracts = []
for contract in contracts:
    # Remove leading numbers and split by ':'
    parts = contract.split(":")
    title = parts[0].strip().replace("", "").replace("*", "").strip()
    details = parts[1].strip().split(" - ")

    # Create formatted output
    formatted_contract = f"## {title}\n"
    for detail in details:
        formatted_contract += f"- {detail.strip()}\n"
    
    formatted_contracts.append(formatted_contract)

# Print the formatted contracts
for formatted_contract in formatted_contracts:
    print(formatted_contract)