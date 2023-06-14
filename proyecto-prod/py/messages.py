class MessageType:
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    WINDOWS = 'windows'
    GMAIL = 'gmail'
    

    @classmethod
    def values(cls):
        return [value for name, value in vars(cls).items() if not name.startswith('_')]


MESSAGE_TYPE = MessageType()

