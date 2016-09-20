#Given two lines on a Cartesian plane, determine whether the two lines would intersect
def intersects(slope1, yintercept1, slope2, yintercept2):
    if slope1==slope2:
        if yintercept1==yintercept2:
            return True
        else:
            return False
    else:
        return True