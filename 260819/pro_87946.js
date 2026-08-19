



function solution(k, dungeons) {
    let answer = 0
    const visited = Array(dungeons.length).fill(false);

    function dfs(piro, total) {
        answer = Math.max(answer, total)

        for (let i = 0; i < dungeons.length; i++) {
            const [need, cost] = dungeons[i]
            
            if (!visited[i] && piro >= need) {
                visited[i] = true

                dfs(piro - cost, total + 1)

                visited[i] = false
            }
        }
    }

    dfs(k, 0)
    return answer;
}


console.log(solution(80, [[80, 20], [50, 40], [30, 10]]))