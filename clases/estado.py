# Importaciones

class Estado:

  def __init__(self, nombreEstado, esFinal):
    """
    Constructor de la clase Estado
    :param nombreEstado: nombre del estado
    :param esFinal: indica si es un estado final
    """
    self.nombre = nombreEstado
    self.esFinal = esFinal
    self.estadosAdyacentes = []

  # Accesores y modificadores
  def getNombre(self):
    """
    Obtiene el nombre del estado
    :return: nombre del estado
    """
    return self.nombre

  def setNombre(self, nombre):
    """
    Modifica el nombre del estado
    :param nombre: nuevo nombre del estado
    """
    self.nombre = nombre

  def getEstadosAdyacentes(self):
    """
    Obtiene la lista de estados adyacentes
    :return: lista de estados adyacentes
    """
    return self.estadosAdyacentes

  def setEstadosAdyacentes(self,listaAdyacentes):
    """
    Modifica la lista de estados adyacentes
    :param listaAdyacentes: nueva lista de estados adyacentes
    """
    self.listaAdyacentes = listaAdyacentes

  def getEsFinal(self):
    """
    Obtiene el valor de esFinal
    :return: esFinal
    """
    return self.esFinal

  def setEsFinal(self, esFinal):
    """
    Modifica el valor de esFinal
    :param esFinal: nuevo valor de esFinal
    """
    self.esFinal = esFinal