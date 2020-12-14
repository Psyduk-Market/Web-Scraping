import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("propertySheet.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Property_spreadsheet_for_populating").sheet1

data = sheet.get_all_records()  # Get a list of all records

# Create data, update, delete and insert ###############################################################################

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

insertRow = ["hello", "02/09/2019", "red", "blue"]
sheet.insert_row(insertRow, 40)  # Insert the list as a row at index 4
# sheet.delete_row(35)
# sheet.update_cell(35,1, "Hello World")

numRows = sheet.row_count

print(row)
print(col)
print(cell)
print(numRows)

########################################################################################################################
