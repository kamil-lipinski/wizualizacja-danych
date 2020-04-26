class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

lista = Wspak([1, 2, 3, 4, 5])
print('lista:', end=' ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista))

napis = Wspak('ananas')
print('napis:', end=' ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis))