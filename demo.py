import re

# Input paragraph
input_text = """
Here are some details from a few of the contracts: 
1. *Cheryl Strayed and Houghton Mifflin Company: 
   - **Date of Agreement: January 26, 2004 
   - **Work: "Torch" 
   - **Advance: $100,000 
   - **Rights: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide 
   - **Manuscript Delivery: 110,000 to 130,000 words by June 30, 2004 
   - [Contract Details](#doc9) 
2. **Alyssa Satin Capucilli and HarperCollins Children's Books: 
   - **Date of Agreement: November 1, 1994 
   - **Work: "Biscuit (An I Can Read Book)" 
   - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide 
   - **Manuscript Delivery: Complete manuscript suitable for a 24-page book 
   - [Contract Details](#doc3) 
3. **John Atkinson and HarperCollins Publishers LLC: 
   - **Date of Agreement: September 25, 2017 
   - **Work: "ABRIDGED CLASSICS: Tiny Versions of Classic Tomes" 
   - **Advance: $15,000 
   - **Description: A collection of approximately 2,500 words with 100 four-color illustrations 
   - [Contract Details](#doc5) 
4. **Laura Numeroff and HarperCollins Publishers Inc.: 
   - **Date of Agreement: December 30, 1998 
   - **Work: "If You Give a Moose a Muffin" 
   - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide 
   - **Manuscript Delivery: Complete and final manuscript by November 15, 2000 
   - [Contract Details](#doc7) 
5. **Adam Silvera and HarperCollins Publishers LLC: 
   - **Date of Agreement: October 9, 2015 
   - **Works: Two works by the author 
   - **Rights: Worldwide, all languages 
   - **Publication Date*: Within 18 months of acceptance 
   - [Contract Details](#doc12)
"""
print(input_text)
# Regular expression to parse the input
contract_pattern = re.compile(
    r"(?P<index>\d+)\.\s\*(?P<author>.*?) and (?P<publisher>.*?):"
    r"(?:\s+- \*\*(?P<details>.*?))(?=\d+\.|\Z)",
    re.DOTALL
)

# Regular expression to parse the details of each contract
detail_pattern = re.compile(r"- \*\*(.+?):\s(.+?)\s*(?=- \*\*|$)", re.DOTALL)

# Function to format a single contract
def format_contract(match):
    author = match.group("author").strip()
    publisher = match.group("publisher").strip()
    details_text = match.group("details").strip()

    details = re.findall(detail_pattern, details_text)
    formatted_details = "\n".join([f"*   **{key.strip()}**: {value.strip()}" for key, value in details])

    return f"""
#### {match.group("index")}. {author} and {publisher}

{formatted_details}

* * *
"""

# Process and format the input text
formatted_output = "\n".join([format_contract(match) for match in contract_pattern.finditer(input_text)])

# Output the formatted result
print(formatted_output)
