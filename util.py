from elasticsearch import Elasticsearch
from web3 import Web3
from web3.middleware import geth_poa_middleware


def get_block_info() -> dict:
    """
    Make requests to the public Ethereum endpoints and get info 
    about latest block. Adds info to the Elasticsearch.
    :return: should return dictionary with timestamp and count of transactions
    in the block
    """
    block_info = dict()
    w3 = Web3(Web3.WebsocketProvider('wss://rinkeby-light.eth.linkpool.io/ws'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    block_info["timestamp"] = w3.eth.get_block('latest').get('timestamp')
    block_info["transactions_count"] = len(
        w3.eth.get_block('latest').get('transactions')
    )

    es = Elasticsearch()
    index: str = "block_info"
    response: dict = es.index(index=index, id=1, document=block_info)
    print(response['result'])

    es.indices.refresh(index=index)

    response: dict = es.search(index=index, query={"match_all": {}})
    print("Got %d Hits:" % response['hits']['total']['value'])
    for hit in response['hits']['hits']:
        print("%(timestamp)s, %(transactions_count)s" % hit["_source"])

    return block_info
