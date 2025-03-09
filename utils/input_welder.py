"""This package is used to read the user's input about"""
from utils.date_utils import read_date, transform_date

class Welder:
    def __init__(self, full_name, authorization_date, company):
        self.full_name = full_name
        self.authorization_expiration_date = authorization_date
        self.company_name = company

    def print_(self):
        day, month, year = self.authorization_expiration_date
        print(f"{self.full_name}'s authorization expires on {day}/{month}/{year}")

def read_welders():
    """
      read from user's input information about the welders

      Return:
        result: list[tuple] -- a list of tuples containing first_name, last_name, expiration date

      Note:
        expiration_date: tuple -- a tuple of day, month, year
    """
    count_welders = int(input("How many welders need to be checked?"))
    welders = []
    for _ in range(count_welders):
        first_name = input("Welder's first name: ")
        last_name = input("Welder's last name: ")
        company = input("Welder's company_name: ")
        expiration_date = read_date("Expiration date")
        welders.append((first_name, last_name, company,expiration_date))
    return welders

def read_welders_from_file() -> list[Welder]:
    file_name = "Valabilitate autorizatii.csv"
    with open(file_name, "rt") as file:
        content = file.readlines()
    welders = []
    for line in content[1:]:
        split_line = line.split(",")
        welder = Welder(
            full_name=split_line[1],
            authorization_date= transform_date(split_line[-2], separator="."),
            company=split_line[0]
        )
        welders.append(welder)
    return welders