function solution(a, b) {
    let g_com_div = 0;
    for(let i = 1 ; i <= b ; i++){
        if(a % i === 0 && b % i === 0)
            g_com_div = i;
    }
    b /= g_com_div;
    while(b % 2 === 0) b /= 2;
    while(b % 5 === 0) b /= 5;
    return b === 1 ? 1 : 2;

}
