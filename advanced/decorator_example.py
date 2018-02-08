

def printStar(fn):
    def warrper(*args, **kwargs):
        print("*" * 30)
        fn(*args, **kwargs)
        print("*" * 30)
    return warrper


@printStar
def displayTitle(title):
    print(title)


displayTitle("Welcome to decorators in python")
