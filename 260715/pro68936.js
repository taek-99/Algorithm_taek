function solution(arr) {
    var answer = [0, 0];

    // 방문 처리를 위한 visited 생성
    let idx = 0
    const n = arr.length
    const visited = Array.from({ length: n }, () => Array(n).fill(false))

    function num_check(check, start_i, start_j) {   // 해당 구역이 같은 값인지 확인
        for (let ii = start_i; ii < start_i+idx; ii++){
            for (let jj = start_j; jj < start_j+idx; jj++){
                if (check != arr[ii][jj]){
                    return
                }
            }
        }

        // 방문처리 진행
        for (let ii = start_i; ii < start_i+idx; ii++){
            for (let jj = start_j; jj < start_j+idx; jj++){
                visited[ii][jj] = true
            }
        }

        answer[check] += 1
        
    }

    // n의 크기에서 2씩 절반으로 나눠가면서 for문 돌리기
    for (idx = n; idx >= 1; idx /= 2){
        for (let i = 0; i < n; i += idx){
            for (let j = 0; j < n; j += idx){
                if (visited[i][j] === false){  // 이미 방문한적이 있으면 확인 안함
                    num_check(arr[i][j], i, j)
                }

            }
        }
    }

    return answer;
}


console.log(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))