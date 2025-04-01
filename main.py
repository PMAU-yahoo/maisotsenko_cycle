from hx_cell import HXCell


# Define inputs (all numbers here, nothing in the code)

working_temperature_in = 25   # ºC
working_relative_humidity_in = 40   # %
product_temperature_in = 35   # ºC
product_relative_humidity_in = 40   # %

cell = HXCell(working_temperature_in,
              working_relative_humidity_in,
              product_temperature_in,
              product_relative_humidity_in)

print(cell.working_temperature_out)
