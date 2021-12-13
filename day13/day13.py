

def get_sheet():
    sheet = set()
    x_max, y_max = 0, 0
    folds = []
    section = 0
    with open("day13/input.txt") as f:
        for line in f:
            if len(line.strip()) == 0:
                section = 1
                continue    

            if section == 0:
                line = [int(x) for x in line.strip().split(",")]
                x_max = max(x_max, line[0])
                y_max = max(y_max, line[1])

                sheet.add((line[0], line[1]))

            elif section == 1:
                line = line.strip().split("=")
                folds.append((line[0][-1], int(line[1])))

    return sheet,x_max,y_max, folds



def print_sheet(sheet, x_max, y_max):
    for y in range(y_max):
        for x in range(x_max):
            if (x,y) in sheet:
                print("#", end="")
            else:
                print(".", end="")
        print()

def fold(sheet, xy, point):
    changes = []

    for coord in sheet:
        if xy == "y":
            if coord[1] >= point:
                changes.append(((coord[0], point - abs(coord[1] - point)), coord))
        elif xy == "x":
            if coord[0] >= point:
                changes.append(((point - abs(coord[0] - point), coord[1]), coord))

    for change in changes:
        sheet.add(change[0])
        sheet.remove(change[1])

if __name__ == "__main__":
    sheet, x_max, y_max, folds = get_sheet()
    #print_sheet(sheet, x_max, y_max)
    print(len(sheet))
    

    print()
    for xy, point in folds:
        print(xy, point)
        # folds the sheet in half
        if xy == "y":
            y_max = point
        elif xy == "x":
            x_max = point
        fold(sheet, xy, point)




        print_sheet(sheet, x_max, y_max)
        print(len(sheet))
        print()