from django.core.files.uploadedfile import InMemoryUploadedFile


class CNABParser:
    def __init__(self, file: InMemoryUploadedFile) -> None:
        self.file = file
        self.transactions = self.handle_parser()

    def handle_parser(self):
        transaction_list = self.txt_to_str_list(self.file)
        parsed_data = []

        for transaction in transaction_list:
            file_data = self.str_to_file_data(transaction)
            parsed_data.append(file_data)

        return parsed_data

    def txt_to_str_list(self, file):
        file_object = file.file
        text: str = file_object.read().decode()
        transaction_list = text.split("\n")

        return transaction_list

    def str_to_file_data(self, transaction: str):
        type = transaction[0]
        hour = f"{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}"
        value = int(transaction[9:19]) / 100
        date = f"{transaction[1:5]}-{transaction[5:7]}-{transaction[7:9]}"

        if type in ["2", "3", "9"]:
            value *= -1

        file_data = {
            "type": type,
            "date": date,
            "value": value,
            "itin": transaction[19:30],
            "card": transaction[30:42],
            "hour": hour,
            "owner": transaction[48:62].title(),
            "store_name": transaction[62:81].capitalize(),
        }

        return file_data
