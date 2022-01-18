from elasticsearch import Elasticsearch
from web3 import Web3
from web3.middleware import geth_poa_middleware


def get_block_info() -> dict:
    """
    Make requests to the public Ethereum endpoints and get info
    about latest block.
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

    add_document_to_elastic(block_info)

    return block_info


def add_document_to_elastic(block_info: dict) -> None:
    """
    Adds info to the Elasticsearch.
    """
    es = Elasticsearch()
    index: str = "block_info"
    response: dict = es.index(index=index, document=block_info)

    es.indices.refresh(index=index)

    response: dict = es.search(index=index, query={"match_all": {}},
                               sort={"timestamp": "desc"}, size=1)
    documents_quantity = response['hits']['total']['value']
    latest_block_info = response["hits"]["hits"][0].get("_source")
    print(f"Total documents quantity: {documents_quantity}")
    print(f"Info from latest block: {latest_block_info}")
