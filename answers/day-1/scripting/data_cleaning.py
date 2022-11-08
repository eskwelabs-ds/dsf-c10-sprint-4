class DataCleaning:

    def __init__(self):
        pass

    def to_lowercase(self, message):
        return message.lower()

    def remove_extra_whitespaces(self, message):
        return message.strip("")


if __name__ == '__main__':
    data_cleaning = DataCleaning()
    lower_data = data_cleaning.to_lowercase('Testing Message  ')
    print(lower_data)

    lower_clean_data = data_cleaning.remove_extra_whitespaces(lower_data)
    print(lower_clean_data)


