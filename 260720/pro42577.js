



function solution(phone_book) {
    var answer = true;

    const n = phone_book.length
    let num_list = [...phone_book].sort()


    for (let idx = 0; idx < n-1 ; idx++) {
        let num = num_list[idx]
        let next_num = num_list[idx+1]
        
        if (num === next_num.slice(0, num.length)){
            return false
        }

    }

    return answer;
}



solution(["97674223", "1195524421", "119"])