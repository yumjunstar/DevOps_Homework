from flask import Flask, request
import pandas as pd
app = Flask(__name__)
share_dir_file = "share_dir/output.txt"

@app.route('/', methods=['GET'])
def print_origin():
    data = pd.read_csv(share_dir_file).values.tolist()
    return data, 200

if __name__ == '__main__':
    app.run()


# Methods
# GET, POST, UPDATE, DELETE