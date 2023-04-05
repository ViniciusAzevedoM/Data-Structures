import pytest
from stack import *

def sunsetViews(buildings, direction):
    """
    Given an array of buildings and a direction that all of the buildings face,
    return an array of the indices of the buildings that can see the sunset.
    
    A building can see the sunset if it's strictly taller than all of the buildings
    that come after it in the direction that it faces.

    Args:
    buildings (list): A list of positive, non-zero integers representing the heights of the buildings.
    direction (str): A string denoting the direction the buildings face, either 'EAST' or 'WEST'.
    
    Returns:
    list: A sorted list of indices of the buildings that can see the sunset.
    """
    n = len(buildings)
    result = Stack()

    #Verifica se a lista de edifícios está vazia
    if n != 0:
      # Verifica se a direção é leste ou oeste
      if direction == "EAST":
          # Inicia a variável max com o último edifício da lista
          max = buildings[n-1]
          # O último edifício sempre pode ser visto
          result.push(n-1)
          # Percorre os edifícios de trás para frente
          for i in range(n-2, -1, -1):
              if buildings[i] > max:
                  # O edifício atual pode ser visto, adiciona na lista de vistos
                  result.push(i)
                  # Atualiza o valor de max
                  max = buildings[i]
      else:
          # Inicia a variável max com o primeiro edifício da lista
          max = buildings[0]
          # O primeiro edifício sempre pode ser visto
          result.push(0)
          # Percorre os edifícios da frente para trás
          for i in range(1, n):
              if buildings[i] > max:
                  # O edifício atual pode ser visto, adiciona na lista de vistos
                  result.push(i)
                  # Atualiza o valor de max
                  max = buildings[i]
      return sorted(list(result))

    else:
      return (result)

@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([3, 5, 4, 4, 3, 1, 3, 2])

    # test 2 data
    array.append([3, 5, 4, 4, 3, 1, 3, 2])

    # test 3 data
    array.append([10, 11])

    # test 4 data
    array.append([2,4])

    # test 5 data
    array.append([1])

    # test 6 data
    array.append([1])

    # test 7 data
    array.append([])

    # test 8 data
    array.append([])

    # test 9 data
    array.append([7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5])

    # test 10 data
    array.append([1, 2, 3, 4, 5, 6])

    # test 11 data
    array.append([1, 2, 3, 4, 5, 6])

    # test 12 data
    array.append([1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8])

    # test 13 data
    array.append([20, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8])
    
    return array

def test_1(data):
    """
    Test evaluation for [3, 5, 4, 4, 3, 1, 3, 2],EAST
    """
    buildings = data[0]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [1, 3, 6, 7]


def test_2(data):
    """
    Test evaluation for [3, 5, 4, 4, 3, 1, 3, 2],WEST
    """
    buildings = data[1]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0,1]

def test_3(data):
    """
    Test evaluation for [10, 11],EAST
    """
    buildings = data[2]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [1]

def test_4(data):
    """
    Test evaluation for [2,4],WEST
    """
    buildings = data[3]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0,1]

def test_5(data):
    """
    Test evaluation for [1],EAST
    """
    buildings = data[4]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [0]

def test_6(data):
    """
    Test evaluation for [1],WEST
    """
    buildings = data[5]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0]

def test_7(data):
    """
    Test evaluation for [],EAST
    """
    buildings = data[6]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == []

def test_8(data):
    """
    Test evaluation for [],WEST
    """
    buildings = data[7]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == []

def test_9(data):
    """
    Test evaluation for [7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5],EAST
    """
    buildings = data[8]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [4, 5, 6, 7, 11]

def test_10(data):
    """
    Test evaluation for [1, 2, 3, 4, 5, 6],EAST
    """
    buildings = data[9]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [5]

def test_11(data):
    """
    Test evaluation for [1, 2, 3, 4, 5, 6],WEST
    """
    buildings = data[10]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1, 2, 3, 4, 5]

def test_12(data):
    """
    Test evaluation for [1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8],WEST
    """
    buildings = data[11]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1, 2, 4, 5, 6, 10, 13]

def test_13(data):
    """
    Test evaluation for [20, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8],EAST
    """
    buildings = data[12]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [0, 13, 14]
