shape=("Rectangle",10,5)
match shape:
    case("Circle",radius):
        print("Shape: Circle")
        print("Radius:",radius)
    case ("Rectangle",length,breadth):
        print("Shape: Rectangle")
        print("Length:",length)
        print("Breadth:",breadth)
    case _:
        print("Unknown shape")

