
def print_comparison(name, dates, times, original_data, computed_data):
    """
    PRint a comparison of 2 time series (original and computed)

    Parameters:
        name: string name for data being compared (<= 9 chars)
        dates: list of strings repres. dates
        times:list of strings repres. times
        original_data: List of original data (every element is a float)
        computed_data: List of computed data (floats)
    """


    print('               ORIGINAL  COMPUTED')
    print(f' DATE    TIME  {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        #               time object 6 chars, right justified  >6 LIMITS it to 6; stupid
        #                                 9 char, 6 after dec point
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')
        # no return statement
