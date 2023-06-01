function solution(numbers, hand) {
    const left = [1, 4, 7];
    const mid = { 2: [0, 1], 5: [1, 1], 8: [2, 1], 0: [3, 1] };
    const right = [3, 6, 9];
  
    let now_l = [3, 0];
    let now_r = [3, 2];
  
    let result = numbers.map((n) => {
      if (left.includes(n)) {
        now_l = [Math.floor(n / 3), 0];
        return "L";
      }
      if (right.includes(n)) {
        now_r = [Math.floor(n / 3) - 1, 2];
        return "R";
      }
  
      let now_m = mid[n];
      let ld = Math.abs(now_l[0] - now_m[0]) + Math.abs(now_l[1] - now_m[1]);
      let rd = Math.abs(now_r[0] - now_m[0]) + Math.abs(now_r[1] - now_m[1])
      if (ld < rd) {
        now_l = now_m;
        return "L";
      } else if (ld > rd) {
        now_r = now_m;
        return "R";
      } else {
        if (hand === "left") {
          now_l = now_m;
        } else {
          now_r = now_m;
        }
      }
        return hand[0].toUpperCase();
    });
  
    return result.join('')
  }

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right");
