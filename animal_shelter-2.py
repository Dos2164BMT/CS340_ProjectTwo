from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for the AAC animal shelter MongoDB collection."""

    def __init__(self, username, password):
        """Initialize MongoDB connection using username and password."""
        self.client = MongoClient(
            f"mongodb://{username}:{password}@localhost:27017/?authSource=aac"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert one document into the animals collection."""
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as error:
                print(f"Create error: {error}")
                return False
        return False

    def read(self, query):
        """Find documents in the animals collection using find()."""
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.find(query)
                return list(result)
            except PyMongoError as error:
                print(f"Read error: {error}")
                return []
        return []

    def update(self, query, new_values):
        """Update document(s) in the animals collection."""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, new_values)
                return result.modified_count
            except PyMongoError as error:
                print(f"Update error: {error}")
                return 0
        return 0

    def delete(self, query):
        """Delete document(s) from the animals collection."""
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as error:
                print(f"Delete error: {error}")
                return 0
        return 0