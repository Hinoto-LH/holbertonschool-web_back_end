#!/usr/bin/env python3
"""Module that returns schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search

    Returns:
        list of schools with the given topic
    """
    return list(mongo_collection.find({"topics": topic}))
