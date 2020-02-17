def make_bread(arg1, arg2, arg3):
     if arg1 == 'water':
         if arg2 == 'flour':
            if arg3 == 'eggs':
                 return 'dough'
     else:
        'not dough'

# tests for make bread
# make_bread('water', 'flour', 'eggs') == 'dough'

def bake(arg):
    if arg == 'dough':
        return 'brioche'
# tests for bake
# bake('dough') == 'brioche'

print(make_bread('water', 'flour', 'eggs'))
print(bake('dough'))


def run_factory(arg1, arg2, arg3):
    result = make_bread(arg1, arg2, arg3)
    result_bake = bake(result)
    return result_bake