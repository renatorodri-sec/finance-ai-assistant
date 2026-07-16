class ConversationContext:
    def __init__(self):
        self.history = []

    def add_message(self, user, message):
        self.history.append({
            "user": user,
            "message": message
        })

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
