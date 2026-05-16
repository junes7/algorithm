def solution(record):
    rlt = []
    dic = {}  
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]   
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            rlt.append('%s님이 들어왔습니다.' %dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            rlt.append('%s님이 나갔습니다.' %dic[sentence_split[1]])  
    return(rlt)