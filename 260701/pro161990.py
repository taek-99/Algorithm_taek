def solution(wallpaper):
    answer = []

    n = len(wallpaper)
    m = len(wallpaper[0])


    file_list = []
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                file_list.append((i, j))


    aa = list(zip(*file_list))

    x1 = min(aa[0])
    x2 = min(aa[1])
    x3 = max(aa[0]) + 1
    x4 = max(aa[1]) + 1

    answer = [x1, x2, x3, x4]
    return answer