from fastapi import FastAPI
from util import get_block_info


app = FastAPI()


@app.get("/get_latest_block/")
def get_info_from_latest_block() -> dict:
    """
    Receives a GET request.
    :return: should return info about latest block: timestamp
    and count of transactions.
    """
    block_info = get_block_info()
    return {
        "Timestamp": block_info.get("timestamp"),
        "Count of transactions in the block":
            block_info.get("transactions_count")
    }
