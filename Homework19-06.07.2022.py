# Data Analysis from .csv file
# 1. How often people take coffee or tea in 1.Weekends and 2.Weekdays (% OF HOT DRINKS from all purchases
#       in WEEKDAYS and in WEEKENDS?). ++
# 2. top-15 of goods ++
# 3. Sales by month in % ++
# 4. Sales by part of the day ++


def hot_drinks_freq(file: list) -> tuple[float, float]:
    """
    Parameter "file": a list of strings from .csv file.
    \nFunction prints percent of Hot drinks among all purchases on:
    \n1)Weekends and
    \n2)Weekdays.
    \nFunction returns two float numbers accordingly.
    """
    array_copy = file
    array_copy.pop(0)
    total_weekend = 0
    total_weekday = 0
    hot_drinks_weekend = 0
    hot_drinks_weekday = 0
    for line in array_copy:
        line = line.rstrip()
        column = line.split(",")
        if column[4] == "Weekend":
            total_weekend += 1
            if column[1] == "Coffee" or column[1] == "Tea":
                hot_drinks_weekend += 1
        else:
            total_weekday += 1
            if column[1] == "Coffee" or column[1] == "Tea":
                hot_drinks_weekday += 1
    we_perc = round((hot_drinks_weekend / total_weekend) * 100, 2)
    wd_perc = round((hot_drinks_weekday / total_weekday) * 100, 2)
    print("\nSales of hot drinks:")
    print(f"Weekend percent of Hot drinks in items bought: {we_perc}%")
    print(f"Weekday percent of Hot drinks in items bought: {wd_perc}%")
    return we_perc, wd_perc


def top_goods(file: list) -> dict:
    """
    Parameter "file": a list of strings from .csv file.
    \nFunction prints top-15 of the goods and returns dictionary with result.
    """
    array_copy = file
    array_copy.pop(0)
    goods_top = {}
    for line in array_copy:
        line = line.rstrip()
        column = line.split(",")
        if column[1] in goods_top:
            goods_top[column[1]] += 1
        else:
            goods_top[column[1]] = 1
    top_15_goods = sorted(goods_top.items(), key=lambda el: el[1], reverse=True)
    top_15_goods = dict(top_15_goods[:15])
    print("\nTop-15 items are:")
    i = 0
    # Printing dictionary in readable format:
    for key, value in top_15_goods.items():
        i += 1
        print(f"{i}: {key}: {value} purchases")
    return top_15_goods


def sales_by_month(file: list) -> dict:
    """
     Parameter "file": a list of strings from .csv file.
     \nFunction prints quantity and distribution of sales by month and returns dictionary with result.
     """
    array_copy = file
    array_copy.pop(0)
    sales_monthly = {}
    total_sales = 0
    for line in array_copy:
        total_sales += 1
        line = line.rstrip()
        column = line.split(",")
        if str(column[2][:7]) in sales_monthly:
            sales_monthly[str(column[2][:7])] += 1
        else:
            sales_monthly[str(column[2][:7])] = 1
    print("\nSales distribution by month:")
    for date, sales in sales_monthly.items():
        a = str(f"{sales} Items bought, percent of Sales: {round((sales / total_sales) * 100, 2)}%")
        sales_monthly[date] = a
        print(f"{date}: {a}")
    return sales_monthly


def sales_by_time(file: list) -> dict:
    """
    Parameter "file": a list of strings from .csv file.
    \nFunction prints distribution of sales by part of the day:
    \nFunction returns dict with results.
    """
    array_copy = file
    array_copy.pop(0)
    total_sales = 0
    sales_by_time_dict = {}
    for line in array_copy:
        total_sales += 1
        line = line.rstrip()
        column = line.split(",")
        if column[3] in sales_by_time_dict:
            sales_by_time_dict[column[3]] += 1
        else:
            sales_by_time_dict[column[3]] = 1
    print("\nSales distribution by time:")
    for time, sales in sales_by_time_dict.items():
        a = str(f"{sales} Items bought, percent of Sales: {round((sales / total_sales) * 100, 2)}%")
        sales_by_time_dict[time] = a
        print(f"{time}: {a}")
    return sales_by_time


# reading file
with open("Bakery.csv", "r") as bakery_file:
    array = bakery_file.readlines()

# Calling function on Hot drinks bought frequency:
hot_drinks_freq(array)
# Calling function on top-15 goods:
top_goods(array)
# Calling function on Sales per Month
sales_by_month(array)
# Calling Sales by time distribution:
sales_by_time(array)
