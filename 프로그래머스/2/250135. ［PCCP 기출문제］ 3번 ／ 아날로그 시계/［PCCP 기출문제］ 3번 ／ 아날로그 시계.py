def solution(h1, m1, s1, h2, m2, s2): 
    rlt = 0
    mcnt, hcnt = 0,0
    sec1 = h1*60*60 + m1*60 + s1
    sec2 = h2*60*60 + m2*60 + s2
    if sec1 == 0 or sec1 == 60*60*12 :
        rlt += 1
    for i in range(sec1, sec2) :
        s = (i*6)%360
        m = (i/10)%360
        h = (i/120)%360
        ns = 360 if (i+1)*6%360 == 0 else (i+1)*6%360
        nm = 360 if (i+1)/10%360 == 0 else (i+1)/10%360
        nh = 360 if (i+1)/120%360 == 0 else (i+1)/120%360       
        if s < h and ns >= nh :
            hcnt += 1
        if s < m and ns >= nm :
            mcnt += 1
        if ns==nm==nh :
            rlt -= 1
    rlt += mcnt + hcnt
    return rlt