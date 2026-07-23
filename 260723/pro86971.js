



function solution(n, wires) {
    var answer = n;

    const net_list = Array.from({ length: n + 1}, () => [])

    // 인접리스트 만들기
    for (const [x, y] of wires) {
        net_list[x].push(y)
        net_list[y].push(x)
    }


    // dfs로 진행
    function dfs(current, cut_x, cut_y, visited) {
        visited[current] = true;  // 방문처리 먼저

        let count = 1;

        for (const next of net_list[current]) {
            if ((current === cut_x && next === cut_y) || (current === cut_y && next === cut_x)) {
                continue;
            }

            if (!visited[next]) {
                count += dfs(next, cut_x, cut_y, visited);
            }
        }

        return count;
    }


    // 순서대로 다 끊어서 수 비교해보기
    for (const [cut_x, cut_y] of wires) {
        const visited = Array(n + 1).fill(false)
        
        const count = dfs(1, cut_x, cut_y, visited)
        const countt = n - count

        answer = Math.min(answer, Math.abs(count - countt))
    }

    


    return answer;
}