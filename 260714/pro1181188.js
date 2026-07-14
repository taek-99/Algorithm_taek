


function solution(targets) {
    var answer = 0;

    // 미사일 오름차순 진행
    targets.sort((a, b) => a[1] - b[1])

    let last_end_missile = -1

    for (const [start_missile, end_missile] of targets){
        // 마지막 지점이랑 다음 시작 지점이 같아도 별개로 처리해야되서 >= 처리
        if (start_missile >= last_end_missile) {
            answer += 1
            last_end_missile = end_missile
        }
    }

    return answer;
}


solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])