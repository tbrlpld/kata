
function isDivisible (dividend, divisior) {
  const rest = dividend % divisior
  if (rest === 0) {
    return true
  } else {
    return false
  }
}

exports.isDivisible = isDivisible

function main (start = 1, end = 100) {
  console.log('Main')
  for (let i = start; i <= end; i++) {
    console.log(i)
  }
  return []
}

exports.main = main

// main()
