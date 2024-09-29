def reach_home(step , destination):

    if step == destination:
        return
    
    print(step)

    step = step + 1

    return reach_home(step , destination)



destination = 6
step = 1
reach_home(step , destination)