function solution(next_student) {
  next_student.unshift(0)
  var answer = 0, N = next_student.length;
  var infoArr = new Array(N).fill(0)

  for (var i = 1; i <= N; i++) {
    var nowStudent = i, nextStudent = next_student[i];
    var tmpArr = [nowStudent]

    var nxtIdx = nextStudent;
    while (nxtIdx && !infoArr[nxtIdx]) {
      tmpArr.push(nxtIdx)
      nxtIdx = next_student[nxtIdx]
      if (nxtIdx === nextStudent){
        break
      }
    }
    console.log(i, tmpArr)
    infoArr[nowStudent] = infoArr[nxtIdx] + tmpArr.length
    console.log(...infoArr, nxtIdx)
  }
  var max = Math.max(...infoArr)
  for (var k = N; k > 0; k--) {
    if (infoArr[k] === max) {
      return k
    }
  }
}


solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7])