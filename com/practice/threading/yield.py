def keep_learning_asynchronous():
    yield 'Educative'

if __name__ == '__main__':
    gen = keep_learning_asynchronous()
    print(next(gen))