function solution(next_student) {
  next_student.unshift(0)
  var answer = 0, N = next_student.length;
  var infoArr = new Array(N).fill(0)

  for (var i = 1; i < N; i++) {
    var now = i, nxt = next_student[i];
    var tmpArr = [now]
    cnt = 1

    while (nxt) {
      if (infoArr[nxt]) {
        cnt = infoArr[nxt]
        break
      } else if (tmpArr.includes(nxt)) {
        var targetIdx = tmpArr.indexOf(nxt)
        distance = tmpArr.length - targetIdx
        cnt = distance
        while (distance) {
          var idx = tmpArr.pop()
          infoArr[idx] = cnt
          distance--;
          // console.log(tmpArr)
        }
        cnt++;
        break
      }
      tmpArr.push(nxt)
      nxt = next_student[nxt]
    }
    console.log(tmpArr, cnt)
    for (var j = tmpArr.length - 1; j >= 0; j--) {
      infoArr[tmpArr[j]] = cnt;
      cnt += 1
    }
    console.log(infoArr)
  }
}



solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2])