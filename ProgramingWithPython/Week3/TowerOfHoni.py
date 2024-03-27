
def honai(disk, source, helper, destination):
    # Base condation
    if disk == 1:
        print('Disk {} moves from tower {} to tower {}.'.format(disk, source, destination))
        return
    honai(disk -1 , source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disk, source, destination))
    honai(disk - 1, helper,source,destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))

# Actual function call
honai(disks, 'A', 'B', 'C')