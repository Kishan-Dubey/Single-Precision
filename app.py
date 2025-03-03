from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_number():
    try:
        data = request.json
        num_str = data.get("number")

        # Ensure the input is a valid number
        if "." in num_str or "e" in num_str.lower():
            number = float(num_str)  # Convert to float
            binary = bin(int(number))  # Convert integer part to binary
            hexadecimal = hex(int(number))  # Convert integer part to hexadecimal
        else:
            number = int(num_str)  # Convert to integer
            binary = bin(number)
            hexadecimal = hex(number)

        decimal = number  # Decimal representation remains the same

        return jsonify({
            "success": True,
            "decimal": decimal,
            "binary": binary,
            "hexadecimal": hexadecimal,
            "float": float(decimal)
        })
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Invalid number"}), 400

if __name__ == '__main__':
    app.run(debug=True)
