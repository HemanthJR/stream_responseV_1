
from flask import Flask, jsonify, render_template
import re

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home_view():
    return render_template('index.html')

def format_response(response):
    # Replace double asterisks with <strong> tags for bold formatting
    response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)
    # Ensure each '-' followed by a space moves to a new line
    response = re.sub(r'(?<!:)\s-\s', r'\n- ', response)
    # Ensure each number followed by a period moves to a new line
    response = re.sub(r'(?<!\n)(\d+\.)', r'\n\1', response)
    return response

@app.route('/get_response', methods=['GET'])
def get_response():
    # Example response text
    response_text = """
    Here are some details from a few of the contracts: 1. ** Cheryl Strayed and Houghton Mifflin Company **: - ** Date of Agreement **: January 26, 2004 - ** Work **: \"Torch\" - ** Advance **: $100,000 - ** Rights **: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide - ** Manuscript Delivery **: 110,000 to 130,000 words by June 30, 2004 - [Contract Details](#doc9) 2. ** Alyssa Satin Capucilli and HarperCollins Children's Books **: - ** Date of Agreement **: November 1, 1994 - ** Work **: \"Biscuit (An I Can Read Book)\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete manuscript suitable for a 24-page book - [Contract Details](#doc3) 3. ** John Atkinson and HarperCollins Publishers LLC **: - ** Date of Agreement **: September 25, 2017 - ** Work **: \"ABRIDGED CLASSICS: Tiny Versions of Classic Tomes\" - ** Advance **: $15,000 - ** Description **: A collection of approximately 2,500 words with 100 four-color illustrations - [Contract Details](#doc5) 4. ** Laura Numeroff and HarperCollins Publishers Inc **: - ** Date of Agreement **: December 30, 1998 - ** Work **: \"If You Give a Moose a Muffin\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete and final manuscript by November 15, 2000 - [Contract Details](#doc7) 5. ** Adam Silvera and HarperCollins Publishers LLC **: - ** Date of Agreement **: October 9, 2015 - ** Works **: Two works by the author - ** Rights **: Worldwide, all languages - ** Publication Date **: Within 18 months of acceptance - [Contract Details](#doc12) If you need more detailed information on any specific contract, please let me know!
    """

    formatted_response = format_response(response_text)
    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, Response, render_template
# import re
# import time

# app = Flask(__name__)

# @app.route('/home', methods=['GET'])
# def home_view():
#     return render_template('index.html')

# def format_response(response):
#     # Replace double asterisks with <strong> tags for bold formatting
#     response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)
#     # Ensure each '-' followed by a space moves to a new line
#     response = re.sub(r'(?<!:)\s-\s', r'\n- ', response)
#     # Ensure each number followed by a period moves to a new line
#     response = re.sub(r'(?<!\n)(\d+\.)', r'\n\1', response)
#     return response

# @app.route('/stream_response', methods=['GET'])
# def stream_response():
#     response_text = """
#     Here are some details from a few of the contracts: 1. ** Cheryl Strayed and Houghton Mifflin Company **: - ** Date of Agreement **: January 26, 2004 - ** Work **: \"Torch\" - ** Advance **: $100,000 - ** Rights **: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide - ** Manuscript Delivery **: 110,000 to 130,000 words by June 30, 2004 - [Contract Details](#doc9) 2. ** Alyssa Satin Capucilli and HarperCollins Children's Books **: - ** Date of Agreement **: November 1, 1994 - ** Work **: \"Biscuit (An I Can Read Book)\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete manuscript suitable for a 24-page book - [Contract Details](#doc3) 3. ** John Atkinson and HarperCollins Publishers LLC **: - ** Date of Agreement **: September 25, 2017 - ** Work **: \"ABRIDGED CLASSICS: Tiny Versions of Classic Tomes\" - ** Advance **: $15,000 - ** Description **: A collection of approximately 2,500 words with 100 four-color illustrations - [Contract Details](#doc5) 4. ** Laura Numeroff and HarperCollins Publishers Inc **: - ** Date of Agreement **: December 30, 1998 - ** Work **: \"If You Give a Moose a Muffin\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete and final manuscript by November 15, 2000 - [Contract Details](#doc7) 5. ** Adam Silvera and HarperCollins Publishers LLC **: - ** Date of Agreement **: October 9, 2015 - ** Works **: Two works by the author - ** Rights **: Worldwide, all languages - ** Publication Date **: Within 18 months of acceptance - [Contract Details](#doc12) If you need more detailed information on any specific contract, please let me know!
#     """

#     formatted_response = format_response(response_text)
#     # print(formatted_response)
#     lines = formatted_response.split('\n')  # Split the response into lines

#     def generate_stream():
#         for line in lines:
#             yield f"{line}\n"
#             time.sleep(0.2)  # Simulate delay for streaming effect

#     return Response(generate_stream(), content_type='text/event-stream')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, jsonify, Response, render_template, request
# import time
# import re

# app = Flask(__name__)

# @app.route('/response', methods=['GET'])
# def response_handler():
#     response_text = """
#     Here are some details from a few of the contracts: 1. ** Cheryl Strayed and Houghton Mifflin Company **: - ** Date of Agreement **: January 26, 2004 - ** Work **: \"Torch\" - ** Advance **: $100,000 - ** Rights **: Exclusive rights to publish in hardcover and softcover in English and other languages worldwide - ** Manuscript Delivery **: 110,000 to 130,000 words by June 30, 2004 - [Contract Details](#doc9) 2. ** Alyssa Satin Capucilli and HarperCollins Children's Books **: - ** Date of Agreement **: November 1, 1994 - ** Work **: \"Biscuit (An I Can Read Book)\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete manuscript suitable for a 24-page book - [Contract Details](#doc3) 3. ** John Atkinson and HarperCollins Publishers LLC **: - ** Date of Agreement **: September 25, 2017 - ** Work **: \"ABRIDGED CLASSICS: Tiny Versions of Classic Tomes\" - ** Advance **: $15,000 - ** Description **: A collection of approximately 2,500 words with 100 four-color illustrations - [Contract Details](#doc5) 4. ** Laura Numeroff and HarperCollins Publishers Inc **: - ** Date of Agreement **: December 30, 1998 - ** Work **: \"If You Give a Moose a Muffin\" - ** Rights **: Exclusive rights to publish, reproduce, and distribute the work in all languages worldwide - ** Manuscript Delivery **: Complete and final manuscript by November 15, 2000 - [Contract Details](#doc7) 5. ** Adam Silvera and HarperCollins Publishers LLC **: - ** Date of Agreement **: October 9, 2015 - ** Works **: Two works by the author - ** Rights **: Worldwide, all languages - ** Publication Date **: Within 18 months of acceptance - [Contract Details](#doc12) If you need more detailed information on any specific contract, please let me know!
#     """
    
#     def format_response(response):
#         # Replace double asterisks with <strong> tags for bold formatting
#         response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)
#         # Ensure each '-' followed by a space moves to a new line
#         response = re.sub(r'(?<!:)\s-\s', r'\n- ', response)
#         # Ensure each number followed by a period moves to a new line
#         response = re.sub(r'(?<!\n)(\d+\.)', r'\n\1', response)
#         return response

#     formatted_response = format_response(response_text)

#     # Check for the 'stream' query parameter
#     if request.args.get('stream', 'false').lower() == 'true':
#         lines = formatted_response.split('\n')  # Split the response into lines

#         def generate_stream():
#             for line in lines:
#                 yield f"{line}\n"
#                 time.sleep(0.5)  # Simulate delay for streaming effect

#         return Response(generate_stream(), content_type='text/plain')
#     else:
#         return jsonify({"response": formatted_response})

# if __name__ == '__main__':
#     app.run(debug=True)
