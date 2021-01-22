function solution(s, n) {
  var answer = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") continue
    let char = s[i].charCodeAt(0) + n
    console.log(String.fromCharCode(char))
  }

  return answer;
}