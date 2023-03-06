from ExcelModel import ExcelModel

model = ExcelModel()

#################
## 1- Revenues
#################

# get values
volume, annual_volume_growth, price, annual_price_growth = model.get_revenues()
# edit values
volume = 100
model.edit_revenues(volume, annual_volume_growth, price, annual_price_growth)

volume, annual_volume_growth, price, annual_price_growth = model.get_revenues()
print(f"volume:{volume}, annual_volume_growth:{annual_volume_growth}, price: {price}, annual_price_growth: {annual_price_growth}")

## same for others