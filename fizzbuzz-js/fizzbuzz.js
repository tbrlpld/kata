
function isDivisible (dividend, divisior) {
  const rest = dividend % divisior
  if (rest === 0) {
    return true
  } else {
    return false
  }
}

exports.isDivisible = isDivisible

function numToFizzBuzz (num) {
  let response = ''
  if (isDivisible(num, 3)) {
    response += 'Fizz'
  }
  if (isDivisible(num, 5)) {
    response += 'Buzz'
  }
  if (!response) {
    response = num.toString()
  }
  return response
}

exports.numToFizzBuzz = numToFizzBuzz

function main (start = 1, end = 100) {

}

exports.main = main

// main()
