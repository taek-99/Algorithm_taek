



function solution(n) {
    var answer = [];
    const triangle = Array.from({ length: n }, (_, i) => Array(i + 1).fill(0))

    const dx = [1, 0, -1]
    const dy = [0, 1, -1]

    let x = -1
    let y = 0
    let num = 1

    for (let i = 0; i < n; i++) {
        const move_count = n - i
        const dir = i % 3

        for (let j = 0; j < move_count; j++) {
            x += dx[dir]
            y += dy[dir]

            triangle[x][y] = num
            num++
        }
    }

    answer = triangle.flat()

    return answer;
}