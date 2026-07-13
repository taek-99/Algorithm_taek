function solution(fees, records) {
    var answer = [];

    let basic_time = fees[0]
    let basic_price = fees[1]
    let unit_time = fees[2]
    let unit_price = fees[3]

    const car_time_list = {}
    const total_time_list = {}
    

    // 시간+분을 모두 분으로 바꾼 뒤 계산
    for (const record of records) {
        const [time, car_number, type] = record.split(" ")
        const [hh, mm] = time.split(":").map(Number)
        const total_time = (hh * 60) + mm
        
        total_time_list[car_number] ??= 0

        if (type === "IN"){
            car_time_list[car_number] = total_time
        } else {
            total_time_list[car_number] += total_time - car_time_list[car_number]
            delete car_time_list[car_number]
        }
    }

    // 출차기록 없는거 일괄 처리
    const end_time = 23 * 60 + 59
    for (const car_number in car_time_list) {
        total_time_list[car_number] += end_time - car_time_list[car_number]
    }

    // 차량 번호대로 정렬
    const car_list = Object.keys(total_time_list).sort()
    
    // 가격 적용하고 정답에 넣기
    for (const car_number of car_list){
        const park_time = total_time_list[car_number]

        if (park_time <= basic_time){
            answer.push(basic_price)
        } else {
            const exit_time = park_time - basic_time
            const price = basic_price + (Math.ceil(exit_time / unit_time) * unit_price)

            answer.push(price)
        }
    }   

    return answer;
}

const fees = [180, 5000, 10, 600]
const records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)