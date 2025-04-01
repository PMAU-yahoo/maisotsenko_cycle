

class HXCell:
  """
  This class models the heat exchanged in one single cell known the input properties of both flows
  """
  def __init__(self,
               working_temperature_in,
               working_relative_humidity_in,
               product_temperature_in,
               product_relative_humidity_in):
    # todo: add any other required inputs, like dimensions
    self._working_temperature_in = working_temperature_in
    self._working_relative_humidity_in = working_relative_humidity_in
    self._product_temperature_in = product_temperature_in
    self._product_relative_humidity_in = product_relative_humidity_in
    self._working_temperature_out = None
    self._working_relative_humidity_out = None
    self._product_temperature_out = None
    self._product_relative_humidity_out = None

    self._heat_exchange_model()

  def _heat_exchange_model(self):
    # todo: add all equations using the variables defined in __init__ and erase this:
    self._working_temperature_out = self._working_temperature_in
    self._working_relative_humidity_out = self._working_relative_humidity_in
    self._product_temperature_out = self._product_temperature_in
    self._product_relative_humidity_out = self._product_relative_humidity_in

  @property
  def working_temperature_out(self):
    """
    Gets the output temperature of the working flow in ºC
    :return: float
    """
    return self._working_temperature_out

