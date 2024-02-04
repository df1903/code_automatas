# Importaciones

class Transicion:

  def __init__(self, origen, destino, simbolo):
    """
    Constructor de la clase Transición
    :param origen: estado de origen
    :param destino: estado de destino
    :param simbolo: símbolo de la transición
    """
    self.origen = origen
    self.destino = destino
    self.simbolo = simbolo

  # Accesores y modificadores
  def getOrigen(self):
    """
    Obtiene el estado de origen
    :return: estado de origen
    """
    return self.origen

  def setOrigen(self, origen):
    """
    Modifica el estado de origen
    :param origen: nuevo estado de origen
    """
    self.origen = origen

  def getDestino(self):
    """
    Obtiene el estado de destino
    :return: estado de destino
    """
    return self.destino

  def setDestino(self, destino):
    """
    Modifica el estado de destino
    :param destino: nuevo estado de destino
    """
    self.destino = destino

  def getSimbolo(self):
    """
    Obtiene el símbolo de la transición
    :return: símbolo de la transición
    """
    return self.simbolo

  def setSimbolo(self, simbolo):
    """
    Modifica el simbolo de la transición
    :param simbolo: nuevo símbolo de la transición
    """
    self.simbolo = simbolo