


def solution(arrayA, arrayB):
    answer = 0
    
    
    def get_gcd(array):
        res = array[0]
        
        for num in array[1:]:
            
            check_num = num
            ## 유클리드 호제법이란걸 처음 써봄
            while check_num != 0:
                res, check_num = check_num, res % check_num
                
        return res
    
    def division(div, array):
        for num in array:
            if num % div == 0:
                return 0
        return div
  
    gcd_a = get_gcd(arrayA)
    gcd_b = get_gcd(arrayB)
    
    answer = max(division(gcd_a, arrayB), division(gcd_b, arrayA))
    
    return answer
