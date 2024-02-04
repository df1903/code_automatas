# Importaciones
from clases.estado import *
from clases.transicion import *

class Automata:

  def __init__(self):
    """
    Constructor de la clase Automata
    """
    self.estados = []
    self.alfabeto = []
    self.transiciones = []
    self.estadoInicial = None
    self.estadosFinales = []

  def cargarAutomata(self, automata):
    # Ingresar alfabeto
    for a in automata['alfabeto']:
      self.ingresarAlfabeto(a)
    # Ingresar estados
    for e in automata['estados']:
      print(bool(e['es_final']))
      self.ingresarEstado(e['nombre'], bool(e['es_final']))
    # Ingresar transiciones
    for t in automata['transiciones']:
      self.ingresarTransicion(t['origen'], t['simbolo'], t['destino'])

  # Accesores y modificadores
  def getEstados(self):
    """
    Obtiene la lista de estados
    :return: lista de estados
    """
    return self.estados

  def setEstados(self, estados):
    """
    Modifica la lista de estados
    :param estados: nueva lista de estados
    """
    self.estados = estados

  def getAlfabeto(self):
    """
    Obtiene el alfabeto
    :return: alfabeto
    """
    return self.alfabeto

  def setAlfabeto(self, alfabeto):
    """
    Modifica el alfabeto
    :param alfabeto: nuevo alfabeto
    """
    self.alfabeto = alfabeto

  def getTransiciones(self):
    """
    Obtiene la lista de transiciones
    :return: lista de transiciones
    """
    return self.transiciones

  def setTransiciones(self, transiciones):
    """
    Modifica la lista de transiciones
    :param transiciones: nueva lista de transiciones
    """
    self.transiciones = transiciones

  def getEstadoInicial(self):
    """
    Obtiene el estado inicial
    :return: estado inicial
    """
    return self.estadoInicial

  def setEstadoInicial(self, estadoInicial):
    """
    Modifica el estado inicial
    :param estadoInicial: nuevo estado inicial
    """
    self.estadoInicial = estadoInicial

  def getEstadosFinales(self):
    """
    Obtiene la lista de estados finales
    :return: lista de estados finales
    """
    return self.estadosFinales

  def setEstadosFinales(self, estadosFinales):
    """
    Modifica la lista de estados finales
    :param estadosFinales: nueva lista de estados finales
    """
    self.estadosFinales = estadosFinales

  # Métodos de alfabeto
  def ingresarAlfabeto(self, simbolo):
    """
    Ingresa un símbolo al alfabeto
    :param simbolo: símbolo a ingresar
    """
    if not self.verificarAlfabeto(simbolo):
      self.alfabeto.append(simbolo)

  def verificarAlfabeto(self, simbolo):
    """
    Verifica si un simbolo existe en el alfabeto
    :param simbolo: símbolo a buscar
    :return: True si existe, False si no existe
    """
    for a in self.alfabeto:
      if simbolo == a:
        return True
    return False

  def mostrarAlfabeto(self):
    """
    Muestra el alfabeto del autómata
    """
    print("                                    ALFABETO")
    for a in self.alfabeto:
        print("| Símbolo: {0}".format(a))

  # Métodos de estados
  def ingresarEstado(self, nombreEstado, estadoFinal):
    """
    Ingresa un estado a la lista de estados
    :param nombreEstado: nombre del estado a ingresar
    :param estadoFinal: True si es un estado es final, False si no lo es
    """
    if self.estadoInicial == None:
      self.estadoInicial = Estado(nombreEstado, estadoFinal)
      self.estados.append(self.estadoInicial)
      if estadoFinal:
        self.estadosFinales.append(self.estadoInicial)
    elif not self.verificarEstado(nombreEstado):
      self.estados.append(Estado(nombreEstado, estadoFinal))
      if estadoFinal:
        self.estadosFinales.append(self.estados[len(self.estados)-1])

  def verificarEstado(self, nombreEstado):
    """
    Verifica si un estado existe en la lista de estados
    :param nombreEstado: nombre del estado a buscar
    :return: True si existe, False si no existe
    """
    for e in self.estados:
      if nombreEstado == e.getNombre():
        return True
    return False

  def obtenerEstado(self, nombreEstado):
    """
    Obtiene un estado de la lista de estados
    :param nombreEstado: nombre del estado a obtener
    :return: estado si existe, None si no existe
    """
    for e in self.estados:
      if nombreEstado == e.getNombre():
        return e
    return None

  def mostrarEstados(self):
    """
    Muestra los estados del autómata
    """
    print("                                    ESTADOS")
    for e in self.estados:
        print("| Nombre: {0} |  Estado final: {1} |".format(e.getNombre(), e.getEsFinal()))

  def mostrarAdyacencias(self):
    """
    Muestra las adyacencias de los estados
    """
    print("                                    ADYACENCIAS")
    for e in self.estados:
        print("| Estado: {0} |  Adyacencias: {1} |"
              .format(e.getNombre(), e.getEstadosAdyacentes()))

  def mostrarEstadosFinales(self):
    """
    Muestra los estados finales del autómata
    """
    print("                                    ESTADOS FINALES")
    for e in self.estadosFinales:
        print("| Nombre: {0}".format(e.getNombre()))

  def mostrarEstadoInicial(self):
    """
    Muestra el estado inicial del autómata
    """
    print("                                    ESTADO INICIAL")
    print("| Nombre: {0}".format(self.estadoInicial.getNombre()))

  # Métodos de transiciones
  def ingresarTransicion(self, estadoOrigen, simbolo, estadoDestino):
    """
    Ingresa una transición a la lista de transiciones
    :param estadoOrigen: estado de origen de la transición
    :param simbolo: símbolo de la transición
    :param estadoDestino: estado de destino de la transición
    """
    if self.verificarEstado(estadoOrigen) and self.verificarEstado(estadoDestino) and self.verificarAlfabeto(simbolo):
      if not self.verificarTransicion(estadoOrigen, estadoDestino, simbolo):
        self.obtenerEstado(estadoOrigen).getEstadosAdyacentes().append(estadoDestino)
        self.transiciones.append(Transicion(estadoOrigen, estadoDestino, simbolo))

  def verificarTransicion(self, estadoOrigen, estadoDestino, simbolo):
    """
    Verifica si una transición existe en la lista de transiciones
    :param estadoOrigen: estado de origen de la transición
    :param estadoDestino: estado de destino de la transición
    :param simbolo: símbolo de la transición
    :return: True si existe, False si no existe
    """
    for t in self.transiciones:
      if estadoOrigen == t.getOrigen() and estadoDestino == t.getDestino() and simbolo == t.getSimbolo():
        return True
    return False

  def mostrarTransiciones(self):
    """
    Muestra las transiciones del autómata
    """
    print("                                    TRANSICIONES")
    for t in self.transiciones:
      print("| Origen: {0}  →  Destino: {1}  |  Símbolo: {2} |"
            .format(t.getOrigen(),
                    t.getDestino(),
                    t.getSimbolo()))

  # Métodos de validación
  def verificarCadena(self, cadena):
    """
    Verifica si una cadena es válida para el autómata
    :param cadena: cadena a verificar
    :return: True si es válida, False si no es válida
    """
    estadoActual = self.estadoInicial
    for simbolo in cadena:
      if not self.verificarAlfabeto(simbolo):
        return False
      temp = self.obtenerEstadoSiguiente(estadoActual, simbolo)
      if temp == None:
        if (self.verificarTransicionLambda(estadoActual)):
          estadoActual = self.obtenerEstadoSiguiente(estadoActual, "λ")
        else:
          # return estadoActual.getEsFinal()
          return False
      else:
        estadoActual = temp
    while (self.verificarTransicionLambda(estadoActual)):
      estadoActual = self.obtenerEstadoSiguiente(estadoActual, "λ")
    return estadoActual.getEsFinal()
  
  def verificarTransicionLambda(self, estado):
    for t in self.transiciones:
      if estado.getNombre() == t.getOrigen() and t.getSimbolo() == "λ":
        return True
    return False

  def obtenerEstadoSiguiente(self, estadoActual, simbolo):
    """
    Obtiene el estado siguiente de un estado actual
    :param estadoActual: estado actual
    :param simbolo: símbolo de transición
    :return: estado siguiente si existe, None si no existe
    """
    for t in self.transiciones:
      if estadoActual.getNombre() == t.getOrigen() and simbolo == t.getSimbolo():
        return self.obtenerEstado(t.getDestino())
    return None

  def verificarEstadoFinal(self, estado):
    """
    Verifica si un estado es final
    :param estado: estado a verificar
    :return: True si es final, False si no es final
    """
    for e in self.estadosFinales:
      if estado.getNombre() == e.getNombre():
        return True
    return False

  def mostrarValidacion(self, cadena):
    """
    Muestra la validación de una cadena
    :param cadena: cadena a validar
    """
    if self.verificarCadena(cadena):
      print("La cadena {0} es válida para el autómata".format(cadena))
    else:
      print("La cadena {0} no es válida para el autómata".format(cadena))

  def mostrarQuintupla(self):
    """
    Muestra la quintupla del autómata
    """
    print("                                    QUINTUPLA")
    print("--------------------------------------------------------------------------------")
    self.mostrarAlfabeto()
    print("--------------------------------------------------------------------------------")
    self.mostrarEstados()
    print("--------------------------------------------------------------------------------")
    self.mostrarEstadoInicial()
    print("--------------------------------------------------------------------------------")
    self.mostrarEstadosFinales()
    print("--------------------------------------------------------------------------------")
    self.mostrarTransiciones()

  # Operaciones entre autómatas
  def unionEntreAutomatas(self, automata1, automata2):
    """
    Une dos autómatas
    :param automata1: primer autómata
    :param automata2: segundo autómata
    :return: autómata resultante
    """
    automataR = Automata()
    # Ingresar alfabeto
    for a in automata1.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    for a in automata2.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    # Ingresar estados
    for a in automata1.getEstados():
      for b in automata2.getEstados():
        if a.getEsFinal() or b.getEsFinal():
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), True)
        else:
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), False)
    # Ingresar transiciones
    for e in automataR.getEstados():
      for a in automata1.getTransiciones():
        for b in automata2.getTransiciones():
          if a.getOrigen() == e.getNombre()[:len(a.getOrigen())] and b.getOrigen() == e.getNombre()[len(a.getOrigen()):]:
            if a.getSimbolo() == b.getSimbolo():
              automataR.ingresarTransicion(a.getOrigen() + b.getOrigen(), a.getSimbolo(), a.getDestino() + b.getDestino())
    return automataR

  def interseccionEntreAutomatas(self, automata1, automata2):
    """
    Realiza la intersección de 2 dos autómatas
    :param automata1: primer autómata
    :param automata2: segundo autómata
    :return: autómata resultante
    """
    automataR = Automata()
    # Ingresar alfabeto
    for a in automata1.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    for a in automata2.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    # Ingresar estados
    for a in automata1.getEstados():
      for b in automata2.getEstados():
        if a.getEsFinal() and b.getEsFinal():
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), True)
        else:
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), False)
    # Ingresar transiciones
    for e in automataR.getEstados():
      for a in automata1.getTransiciones():
        for b in automata2.getTransiciones():
          if a.getOrigen() == e.getNombre()[:len(a.getOrigen())] and b.getOrigen() == e.getNombre()[len(a.getOrigen()):]:
            if a.getSimbolo() == b.getSimbolo():
              automataR.ingresarTransicion(a.getOrigen() + b.getOrigen(), a.getSimbolo(), a.getDestino() + b.getDestino())
    return automataR

  def reversoAutomata(self, automata):
    """
    Realiza el reverso de un autómata
    :param automata: autómata a reversar
    :return: autómata resultante
    """
    if len(automata.getEstadosFinales()) == 1:
      return self.reversoUnEstadofinal(automata)
    else:
      return self.reversoUnEstadofinal(self.convertirUnFinal(automata))

  def reversoUnEstadofinal(self, automata):
    """
    Realiza el reverso de un autómata con un solo estado final
    :param automata: autómata a reversar
    :return: autómata resultante
    """
    automataR = Automata()
    # Ingresar alfabeto
    for a in automata.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    # Ingresar estado inicial
    estados = automata.getEstados()
    for e in estados:
      if e.getEsFinal():
        final = estados.pop(estados.index(e))
        automataR.ingresarEstado(final.getNombre(), False)
        break
    # Ingresar estados
    for e in automata.getEstados():
      if e.getNombre() == automata.getEstadoInicial().getNombre():
        automataR.ingresarEstado(e.getNombre(), True)
      else:
        automataR.ingresarEstado(e.getNombre(), False)
    # Ingresar transiciones
    for t in automata.getTransiciones():
      automataR.ingresarTransicion(t.getDestino(), t.getSimbolo(), t.getOrigen())
    return automataR

  def convertirUnFinal(self, automata):
    """
    Convierte un autómata con un solo estado final
    :param automata: autómata a convertir
    :return: autómata resultante
    """
    automataR = automata
    automataR.ingresarAlfabeto("λ")
    automataR.setEstadosFinales([])
    automataR.ingresarEstado("qf", True)
    for e in automata.getEstados():
      if e.getEsFinal() and e.getNombre() != "qf":
        e.setEsFinal(False)
        automataR.ingresarTransicion(e.getNombre(), "λ", "qf")
    return automataR

  def complementoAutomata(self, automata):
    """
    Realiza el complemento de un autómata
    :param automata: autómata a complementar
    :return: autómata resultante
    """
    automataR = Automata()
    # Ingresar alfabeto
    for a in automata.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    # Ingresar estados
    for a in automata.getEstados():
      if not a.getEsFinal():
        automataR.ingresarEstado(a.getNombre(), True)
      else:
        automataR.ingresarEstado(a.getNombre(), False)
    # Ingresar transiciones
    for e in automataR.getEstados():
      for a in automata.getTransiciones():
        if a.getOrigen() == e.getNombre():
          automataR.ingresarTransicion(a.getOrigen(), a.getSimbolo(), a.getDestino()) 
    return automataR

  def diferenciaEntreAutomatas(self, automata1, automata2):
    """
    Realiza la diferencia entre dos autómatas
    :param automata1: primer autómata
    :param automata2: segundo autómata
    :return: autómata resultante
    """
    return self.interseccionEntreAutomatas(automata1, self.complementoAutomata(automata2))

  def concatenacionEntreAutomatas(self, automata1, automata2):
    """
    Realiza la concatenación entre dos autómatas
    :param automata1: primer autómata
    :param automata2: segundo autómata
    :return: autómata resultante
    """
    automataR = Automata()
    # Ingresar alfabeto
    for a in automata1.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    for a in automata2.getAlfabeto():
      automataR.ingresarAlfabeto(a)
    # Ingresar estados
    for a in automata1.getEstados():
      for b in automata2.getEstados():
        if a.getEsFinal() and not b.getEsFinal():
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), True)
        else:
          automataR.ingresarEstado(a.getNombre() + b.getNombre(), False)
    # Ingresar transiciones
    for e in automataR.getEstados():
      for a in automata1.getTransiciones():
        for b in automata2.getTransiciones():
          if a.getOrigen() == e.getNombre()[:len(a.getOrigen())] and b.getOrigen() == e.getNombre()[len(a.getOrigen()):]:
            if a.getSimbolo() == b.getSimbolo():
              automataR.ingresarTransicion(a.getOrigen() + b.getOrigen(), a.getSimbolo(), a.getDestino() + b.getDestino())
    return automataR
  


