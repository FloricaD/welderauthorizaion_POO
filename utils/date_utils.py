class InvalidDateException(Exception):
    pass


def read_date(text: str):
    """
    Read from user's input a date in the specified format

    Arguments:
      text: str -- the text to show the user
    Return:
      result: tuple -- a tuple containing the day, month, year as int
  """
    while True:
        expiration_date = input(f"{text} (format: day/month/year) :")
        try:
            date = transform_date(expiration_date, "/")
            return date
        except (InvalidDateException, ValueError):
            print("Please insert the date again!")


def bisect(year):
    result = False
    if year % 4 == 0:  # verificam daca e divizibil cu 4
        if year % 100 == 0:  # verificam daca e divizibil cu 100
            if year % 400 == 0:  # verificam daca e divizibil cu 400
                result = True  # este divizibil cu 4, 100 si 400
            else:
                result = False  # este divizibil cu 4 si 100
        else:
            result = True  # este divizibil cu 4
    return result


def validate_date(day: int, month: int, year: int):
    if month == 2:
        if day == 29:
            if not bisect(year):
                raise InvalidDateException
    if day not in range(1, 32):
        raise InvalidDateException
    if month not in range(1, 13):
        raise InvalidDateException


def transform_date(text: str, separator) -> tuple[int, int, int]:
    day, month, year = text.split(separator)
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        print("One of the values is not an integer")
        raise
    try:
        validate_date(day, month, year)
    except InvalidDateException:
        print("The input date is incorrect.")
        raise
    return day, month, year


def date_difference(today_date: tuple[int, int, int], expiration_date: tuple[int, int, int]) -> bool:
    today_day, today_month, today_year = today_date
    exp_day, exp_month, exp_year = expiration_date
    if exp_year > today_year:  # exp_year 2025 today_year 2024
        if exp_year - today_year > 2:
            return False
        if exp_year - today_year == 1:
            return ((12 - today_year) + exp_month) <= 3
    elif exp_year < today_year:
        # the authorization already expired
        return False
    else:  # exp_year == today_year
        return (exp_month - today_month) <= 3
