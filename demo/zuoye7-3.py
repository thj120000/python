#!@Author : Sanwat
#!@File : .py
def biggest(Dict):
    length = 0
    for key in Dict:
        if len(Dict[key]) > length:
            length = len(Dict[key])
            key1 = key
    return key1

if __name__ == "__main__":
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}  # 值都是列表
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')

    print(biggest(animals))
    print(biggest({'a': [3, 3, 18], 'c': [3, 15, 12, 10, 0], 'b': [10, 19, 14, 5, 16, 20,
                  11, 6], 'd': [5,16, 8, 16, 6, 1]}))