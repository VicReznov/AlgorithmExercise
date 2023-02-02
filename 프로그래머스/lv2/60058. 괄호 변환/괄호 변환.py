# '균형잡힌 괄호 문자열'로 나누기 위한 인덱스 찾는 함수
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# '올바른 괄호 문자열'인지 판단하는 함수
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''

    if p == '':
        return answer

    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    # '올바른 괄호 문자열' -> v에 대한 함수를 수행한 결과를 붙여서 반환
    if check_proper(u):
        answer = u + solution(v)
    # '올바른 괄호 문자열' 아니면 -> 아래 과정 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer