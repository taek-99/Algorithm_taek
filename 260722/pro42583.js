function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    
    const n = truck_weights.length
    const wait_truck = [...truck_weights].reverse()
    
    let idx = 0
    let current_bridge_truck = []
    let current_weight_truck = 0
    let bridge_idx = 0

    while (idx < n || bridge_idx < current_bridge_truck.length) {
        answer++

        // 현재 시간에 다리를 빠져나가는 트럭 확인
        if (
            bridge_idx < current_bridge_truck.length &&
            current_bridge_truck[bridge_idx].exit_time === answer
        ) {
            current_weight_truck -= current_bridge_truck[bridge_idx].weight
            bridge_idx++
        }

        // 기다리는 트럭이 남아있다면
        if (idx < n) {
            const next_truck = wait_truck[wait_truck.length - 1]

            // 다음 트럭이 올라가도 제한 무게 이하인 경우
            if (current_weight_truck + next_truck <= weight) {
                const truck = wait_truck.pop()

                current_bridge_truck.push({
                    weight: truck,
                    exit_time: answer + bridge_length
                })

                current_weight_truck += truck
                idx++
            }
        }
    }

    return answer;
}