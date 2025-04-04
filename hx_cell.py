

class HXCell:
  """
  This class models the heat exchanged in one single cell known the input properties of both flows
  """
  def __init__(self, length):
    # todo: add any other required inputs, like dimensions (all fix parameters should be in the __init__ list, like "lenght", and all variables in the list below, like self._working_temperature_in
    self._length = length
    self._working_temperature_in = None
    self._working_relative_humidity_in = None
    self._product_temperature_in = None
    self._product_relative_humidity_in = None
    self._working_temperature_out = None
    self._working_relative_humidity_out = None
    self._product_temperature_out = None
    self._product_relative_humidity_out = None

  def heat_exchange_model(self):
    # todo: add all equations using the variables defined in __init__ and erase this. Yo can add all together here or divide them in parts and call each part here (like _latent_exchange)
    self._working_temperature_out = self._working_temperature_in
    self._product_temperature_out = self._product_temperature_in
    self._latent_exchange()

  def _latent_exchange(self):
    self._working_relative_humidity_out = self._working_relative_humidity_in
    self._product_relative_humidity_out = self._product_relative_humidity_in

  # todo: all inputs should have two functions, @property and .setter
  @property
  def working_temperature_in(self):
    """
    Gets the input temperature of the working flow in ºC
    :return: float
    """
    return self._working_temperature_in

  @working_temperature_in.setter
  def working_temperature_in(self, value):
    """
    Sets the input temperature of the working flow in ºC
    :param value: float
    """
    self._working_temperature_in = value

  # todo: all outputs should have only one function, @property
  @property
  def working_temperature_out(self):
    """
    Gets the output temperature of the working flow in ºC
    :return: float
    """
    return self._working_temperature_out

