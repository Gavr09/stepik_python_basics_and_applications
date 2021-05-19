'''
верхний уровень - ценность 1
средний уровень - ценность 2
нижний уровень - ценность 3

вывести в порядке: красный зеленый синий

<cube color='blue'><cube color='red'><cube color='green'></cube></cube><cube color='red'></cube></cube>

4 3 1

<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>

10 18 10
'''

from xml.etree import ElementTree

str = input().strip()

high_element = ElementTree.fromstring(str)

color_dict = {'red':0, 'green':0, 'blue':0}

color_dict[high_element.attrib['color']] += 1

def calc_weight(element, weight):
    for downward_element in element:
        color_dict[downward_element.attrib['color']] += weight + 1
        calc_weight(downward_element, weight+1)

calc_weight(high_element, 1)
# for medium_element in high_element:
#     color_dict[medium_element.attrib['color']] += 2
#     for low_element in medium_element:
#         color_dict[low_element.attrib['color']] += 3

print('{} {} {}'.format(color_dict['red'], color_dict['green'], color_dict['blue']))