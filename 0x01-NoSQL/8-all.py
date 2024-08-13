#!/usr/bin/env python3
"""
function that lists all documents in a collection
Return an empty list if no document in the collection
"""

def list_all(mongo_collection):
    """
    lists all documents in a MongoDB collection.
    """
    return [doc for doc in mongo_collection.find()]
