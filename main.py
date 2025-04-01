from hx_cell import HXCell


# Define inputs (all numbers here, nothing in the code)

working_temperature_in = 25   # ºC
working_relative_humidity_in = 40   # %
product_temperature_in = 35   # ºC
product_relative_humidity_in = 40   # %
length = 0.1  # m

cell = HXCell(length)

cell.working_temperature_in = working_temperature_in

cell.heat_exchange_model()

print(cell.working_temperature_out)
