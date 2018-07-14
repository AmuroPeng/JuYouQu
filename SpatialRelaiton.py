# -*- coding:utf-8 -*-


def isPolygonContainsPoint(friend_loc_list, shop_loc):
    nCross = 0;
    for index in range(len(friend_loc_list)):
        p1 = friend_loc_list[index]
        p2 = friend_loc_list[(index + 1) % len(friend_loc_list)]
        if p1[1] == p2[1]:
            continue
        if shop_loc[1] < min(p1[1], p2[1]):
            continue
        if shop_loc[1] >= max(p1[1], p2[1]):
            continue
        x = (shop_loc[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
        if x > shop_loc[0]:
            nCross += 1
    return nCross % 2 == 1


if __name__ == '__main__':
    print(isPolygonContainsPoint([[1, 1], [100, 100], [1, 100], [100, 1]], [500, 50]))
