def reachHome(src , dest):

    # Base Case

    if src == dest:
        print(src , dest)
        return 
    
    # PreProcessing

    print(src , dest)
    src = src + 1

    # Recursive Relation

    reachHome(src , dest)

src = 1
dest = 10
reachHome(src , dest)
