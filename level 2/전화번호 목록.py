# 재귀함수를 최대한 줄이자
# 정렬과 이진분류를 항상 생각!

def solution(phone_book) :
    
    answer = True
    phone_book.sort()
    phone_book_len = len(phone_book)
    for i in range(phone_book_len - 1) :
      if len(phone_book[i]) < len(phone_book[i + 1]) :
         prefix = phone_book[i]
         prefix_len = len(phone_book[i])
         letter = phone_book[i + 1][ : prefix_len]
         if prefix == letter :
           answer = False
    return answer



# zip : 짝지어주는 함수
# startswith : 괄호 안의 문자로 시작하면 True, 아니면 False를 산출

def solution(phoneBook):
    
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1 :]) :
        if p2.startswith(p1) :
            return False
    return True




def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer








