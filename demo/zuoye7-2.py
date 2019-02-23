#!@Author : Sanwat
#!@File : .py
def howMany(Dict):
    num = 0
    for animal in Dict.values():
        num += len(animal)
    return num

if __name__ == "__main__":
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}  # 值为列表
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')

    print(howMany(animals))
    print(howMany({'a': [8, 11, 4, 18], 'H': [19, 19, 16], 'L': [12], 'O': [12, 2, 14, 2],
                   'p': [7, 15, 7, 15, 10], 's': [], 't': [], 'y': [11, 19, 12, 0]}))