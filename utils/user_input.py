"""This package is used to read the user's input"""
from utils.date_utils import read_date
def read_today_date():
    input_ = read_date("What's today's date")
    return input_