def date_analysis(dates):
    new_dates = [x for x in dates if x.split('/')[1] not in '030405']
    dates = [x.split('/')[::-1] for x in new_dates]
    return "/".join(sorted(dates)[-1][::-1])
