from utils.user_input import  read_today_date
from utils.input_welder import  read_welders_from_file
from utils.date_utils import date_difference

if __name__ == '__main__':
    today_date = read_today_date()
    welders = read_welders_from_file()
    expired_authorizations = {}
    for welder in welders:
        # check if the welder's authorization expired
        if date_difference(today_date=today_date, expiration_date=welder.authorization_expiration_date):
            if welder.company_name in expired_authorizations:
                # if there's a company_name key, add the welder
                expired_authorizations[welder.company_name].append((welder.full_name, welder.authorization_expiration_date))
            else:
                # if there is no company_name as key, add it
                expired_authorizations[welder.company_name] = [(welder.full_name, welder.authorization_expiration_date)]
    print()
    for company, welders in expired_authorizations.items():
        print(f"For company {company} there are {len(welders)} expired authorizations")
        for full_name, expiration_date in welders:
            day, month, year = expiration_date
            print(f"      {full_name}'s authorization expires on {day}/{month}/{year}")
        print()