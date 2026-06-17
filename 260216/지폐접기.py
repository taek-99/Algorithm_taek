

def answer_check(a_wx, a_wy, a_bx, a_by):

    if a_wx >= a_bx and a_wy >= a_by:
        return False
    
    if a_wy >= a_bx and a_wx >= a_by:
        return False
    
    return True



def solution(wallet, bill):
    answer = 0
    wx, wy = wallet
    bx, by = bill


    while answer_check(wx, wy, bx, by):
        
        if bx > by:
            bx //= 2
        else:
            by //= 2

        answer += 1

    return answer

