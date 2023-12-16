from flask import Flask, jsonify, request

app = Flask(__name__)

# POST Endpoint
@app.route('/listings', methods=['POST'])
def create_listing():
    try:
        # Implement logic to create a new listing
        # ...
        # Example logic that may raise an exception for a bad request
        if 'name' not in request.json:
            raise ValueError("Name is required for a listing")

        # Successful request
        return jsonify({"message": "Listing created successfully"}), 200
    except Exception as e:
        # Handle bad request or server error
        return jsonify({"error": str(e)}), 400


# GET Endpoint
@app.route('/listings', methods=['GET'])
def get_all_listings():
    try:
        # Implement logic to get all listings
        # ...

        # Example condition for bad request (modify based on your logic)
        if 'invalid_param' in request.args:
            raise ValueError("Invalid parameter in the request")

        # Successful request
        return jsonify({"listings": ["listing1", "listing2"]}), 200
    except ValueError as ve:
        # Handle bad request
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        # Handle server error
        return jsonify({"error": str(e)}), 500


# Add other endpoints...

if __name__ == '__main__':
    app.run(debug=True)
