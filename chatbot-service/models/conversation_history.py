from datetime import datetime as dt
from bson.objectid import ObjectId
from config.mongo import mongo


class ConversationHistoryModel:
    collection = mongo.conversation_history

    @staticmethod
    def create_message(chat_id: str, sender: str, message: str):
        message_data = {
            "chat_id": chat_id,
            "sender": sender,
            "message": message,
            "timestamp": dt.utcnow()
        }
        return ConversationHistoryModel.collection.insert_one(message_data)

    @staticmethod
    def get_messages_by_chat_id(chat_id: str):
        return list(ConversationHistoryModel.collection.find({"chat_id": chat_id}).sort("timestamp", 1))

    @staticmethod
    def get_message_by_id(message_id: str):
        try:
            return ConversationHistoryModel.collection.find_one({"_id": ObjectId(message_id)})
        except Exception as e:
            print(f"Erro ao buscar mensagem por ID: {e}")
            return None

    @staticmethod
    def update_message(message_id: str, update_data: dict):
        update_data["updated_at"] = dt.utcnow()
        ConversationHistoryModel.collection.update_one(
            {"_id": ObjectId(message_id)},
            {"$set": update_data}
        )
        return ConversationHistoryModel.get_message_by_id(message_id)

    @staticmethod
    def delete_message(message_id: str):
        try:
            result = ConversationHistoryModel.collection.delete_one({"_id": ObjectId(message_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(str(e))
            return False
