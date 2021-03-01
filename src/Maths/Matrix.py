class Matrix():
  def __init__(self, rows: int, columns:  int) -> None:
      self.__rows = rows
      self.__columns = columns

  @property
  def rows(self):
    return self.__rows

  @property
  def columns(self):
    return self.__columns

