import data

regression_options = {1: "CAPM"}

indicies = {1: "SP500"}

ticker = input("Enter Ticker Symbol: ")

start_date = input("Enter Start Date (yyyy-mm-dd): ")

end_date = input("Enter End Date (yyyy-mm-dd): ")

print("Choose Index:")

for key in indicies:
    print("{key}: {value}".format(key=key, value=indicies[key]))
    
index = indicies[int(input("Enter Index Number From Above: "))]


print("Choose Your Pricing Model:")

for key in regression_options:
    print("{key}: {value}".format(key=key, value=regression_options[key]))

model = regression_options[int(input("Enter Model Number From Above: "))]

if model == 'CAPM':
    
    data.make_capm_data_frame(ticker, index, start_date, end_date)

