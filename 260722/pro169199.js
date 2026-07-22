function solution(board) {
    var answer = 0;

    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, 1, -1]
    const n = board.length
    const m = board[0].length
    const q = []
    const visited = Array.from({ length: n }, () => Array(m).fill(false))

    let head = 0
    let start_pos
    let end_pos

    // 시작, 골 위치 찾기
    for (let i = 0; i < n; i ++) {
        for (let j = 0; j <m; j ++) {
            if (board[i][j] === 'R') {
                start_pos = [i, j]
            }

            if (board[i][j] === 'G') {
                end_pos = [i, j]
            }
        }
    }

    q.push([start_pos[0], start_pos[1], 0])
    visited[start_pos[0]][start_pos[1]] = true

    // bfs 시작
    while (head < q.length) {
        const [x, y, c] = q[head]
        head ++

        // 골에 도착
        if (x === end_pos[0] && y === end_pos[1]) {
            return c
        }

        for (let d = 0; d < 4; d++) {
            let nx = x
            let ny = y

            // 한 방향으로 끝까지 이동
            while (true) {
                const nnx = nx + dx[d]
                const nny = ny + dy[d]

                // 범위 벗어나면 아웃
                if (nnx < 0 || nnx >= n || nny < 0 || nny >= m) {
                    break
                }

                // 다음 칸이 장애물이면 현재 위치에서 정지
                if (board[nnx][nny] === 'D') {
                    break
                }

                nx = nnx
                ny = nny
            }

            // 제자리면 패스
            if (nx === x && ny === y) {
                continue
            }

            // 방문한적 있으면 패스
            if (visited[nx][ny]) {
                continue
            }

            visited[nx][ny] = true
            q.push([nx, ny, c + 1])
        }
    }

    return -1;
}