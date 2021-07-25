def select_dates(potential_dates):
    date_list = [date["name"] for date in potential_dates if (date["age"] > 30 and "art" in date["hobbies"] and date["city"] == "Berlin")]
    return ", ".join(date_list)
