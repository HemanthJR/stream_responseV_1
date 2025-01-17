from flask import Flask, Response, render_template
import time

app = Flask(__name__)

# data = '''
# Here are some details from a few of the contracts: 1. *Cheryl Strayed and Houghton Mifflin Company: - **Date of Agreement: January 26, 2004 - **Work: "Torch" - **Advance: $100,000 - **Rights: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide - **Manuscript Delivery: 110,000 to 130,000 words by June 30, 2004 - [Contract Details](#doc9) 2. **Alyssa Satin Capucilli and HarperCollins Children's Books: - **Date of Agreement: November 1, 1994 - **Work: "Biscuit (An I Can Read Book)" - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - **Manuscript Delivery: Complete manuscript suitable for a 24-page book - [Contract Details](#doc3) 3. **John Atkinson and HarperCollins Publishers LLC: - **Date of Agreement: September 25, 2017 - **Work: "ABRIDGED CLASSICS: Tiny Versions of Classic Tomes" - **Advance: $15,000 - **Description: A collection of approximately 2,500 words with 100 four-color illustrations - [Contract Details](#doc5) 4. **Laura Numeroff and HarperCollins Publishers Inc.: - **Date of Agreement: December 30, 1998 - **Work: "If You Give a Moose a Muffin" - **Rights: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - **Manuscript Delivery: Complete and final manuscript by November 15, 2000 - [Contract Details](#doc7) 5. **Adam Silvera and HarperCollins Publishers LLC: - **Date of Agreement: October 9, 2015 - **Works: Two works by the author - **Rights: Worldwide, all languages - **Publication Date*: Within 18 months of acceptance - [Contract Details](#doc12) If you need more detailed information on any specific contract, please let me know!
# '''

# def parse_contracts(data):
#     # Split the text into individual contracts based on numbering
#     contracts = data.split("\n\n")
    
#     for contract in contracts:
#         if not contract.strip():  # Skip empty sections
#             continue
        
#         # Extract details from the contract using basic string parsing
#         details = {}
#         lines = contract.split("\n")
#         for line in lines:
#             line = line.strip()
#             if line.startswith("*"):  # Extract details starting with *
#                 key_value = line.split(": ", 1)
#                 if len(key_value) == 2:
#                     key, value = key_value
#                     details[key.lstrip("* ")] = value.strip()
#             elif line.startswith("-"):  # Handle keys starting with -
#                 key_value = line.split(": ", 1)
#                 if len(key_value) == 2:
#                     key, value = key_value
#                     details[key.lstrip("- ")] = value.strip()
        
#         if details:
#             yield f"data: {details}\n\n"

def generate_stream():
    data = ['**','abcde','efghij','**', 'karthika \n', 'mani', '**','mahesh','**']
    bold = False

    for item in data:
        if item == '**':
            bold = not bold  
            continue
        yield f"data: {item}|{'bold' if bold else 'normal'}\n\n"  
        time.sleep(0.3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(generate_stream(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
