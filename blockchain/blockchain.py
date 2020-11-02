
from flask import Flask, render_template
from time import time

class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(0, '00')

    def create_block(self, nonce, previous_hash):
        '''
        Add a block of transactions to the blockcchain
        '''
        block = {'block_number':len(self.chain) +1, 'timestamp': time() , 'nonce': nonce, 'previous_hash': previous_hash}
        #Reset the current list of transactions
        self.transactions = []
        self.chain.append(block)


# Instantiate the Blockchain
blockchain = Blockchain()

# Instantiate the Node
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8081, type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(debug=True)