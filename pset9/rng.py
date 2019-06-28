class rng:
  def __init__(self, seed, a, c, m):
    self.__I = seed
    self.__a = a
    self.__c = c
    self.__m = m

  def next_int(self):
    self.__I = (self.__a * self.__I + self.__c) % self.__m
    return self.__I
