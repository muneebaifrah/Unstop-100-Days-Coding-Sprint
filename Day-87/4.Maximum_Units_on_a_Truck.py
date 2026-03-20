def maximumUnits(boxTypes, truckSize):
    # Sort the boxTypes based on units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0

    for numberOfBoxes, unitsPerBox in boxTypes:
        if truckSize == 0:
            break

        # Take as many boxes as possible from the current type
        boxes_to_take = min(numberOfBoxes, truckSize)
        total_units += boxes_to_take * unitsPerBox
        truckSize -= boxes_to_take

    return total_units

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # Number of rows in boxTypes
    m = int(data[1])  # Number of columns in boxTypes (always 2 in this case)

    boxTypes = []
    index = 2
    for _ in range(n):
        boxTypes.append([int(data[index]), int(data[index + 1])])
        index += m

    truckSize = int(data[index])

    result = maximumUnits(boxTypes, truckSize)
    print(result)