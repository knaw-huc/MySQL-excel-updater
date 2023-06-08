import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="bonzo",
                               db="pandas"))

def create_table(excel, columns, table_name, query=""):
    data = pd.DataFrame(excel_file, columns=columns)
    if query == "":
        data_target = data
    else:
        data_target = data.query(query)
    data_target.to_sql(name=table_name, con=engine, if_exists='replace')
    print("Data written to table " + table_name)

print("Reading excel file...")
excel_file = pd.read_excel('data/ESTA.xlsx')
# create_table(excel_file, ["subvoyage_id", "sub_dept_date_year"], "dep_year", "sub_dept_date_year > 0")
# create_table(excel_file, ["subvoyage_id", "sub_dept_date_month"], "dep_month", "sub_dept_date_month > 0")
# create_table(excel_file, ["subvoyage_id", "sub_dept_date_day"], "dep_day", "sub_dept_date_day > 0")
# create_table(excel_file, ["subvoyage_id", "sub_arrival_date_year"], "arr_year", "sub_arrival_date_year > 0")
# create_table(excel_file, ["subvoyage_id", "sub_arrival_date_month"], "arr_month", "sub_arrival_date_month > 0")
# create_table(excel_file, ["subvoyage_id", "sub_arrival_date_day"], "arr_day", "sub_arrival_date_day > 0")
# create_table(excel_file, ["subvoyage_id", "sub_source"], "sub_source")
# create_table(excel_file, ["voyage_id", "summary"], "summary")
# create_table(excel_file, ["sub_slaves", "slaves_total_standardized_total"], "slaves_total", "slaves_total_standardized_total > 0")
# create_table(excel_file, ["voyage_id", "year"], "voyage_year", "year > 0")



# for index, row in data.iterrows():
#     if not pd.isna(row["sub_dept_date_year"]):
#         print(row["subvoyage_type"])
#         print(int(row["sub_dept_date_year"]))