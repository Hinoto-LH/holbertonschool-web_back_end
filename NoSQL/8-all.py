#!/usr/bin/env python3
"""Module that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of documents, or empty list if no documents
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
