#!/usr/bin/env python3
"""Module that updates topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list): list of topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
