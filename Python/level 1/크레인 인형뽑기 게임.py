# 내 코드
def solution(board, moves) :
    answer = 0
    new_board = list(map(list, zip(*board)))
    for i in range(len(board[0])) :
        new_board[i].reverse()
        
    basket = []

    for i in moves :
        try :
            doll_height_index = new_board[i - 1].index(0) - 1
    
            if doll_height_index != -1 :
                basket.append(new_board[i - 1][doll_height_index])
                new_board[i - 1][doll_height_index] = 0

            else :
                pass

        except :
            basket.append(new_board[i - 1][-1])
            new_board[i - 1][-1] = 0
            
    k = 0
    while k < len(basket) - 1 :
        if basket[k] != basket[k + 1] :
            k += 1
        else :
            basket = basket[: k] + basket[k + 2 : ]
            answer += 2
            k = 0
    
    return answer
  
  
  
  
  
  
  
  
  
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
