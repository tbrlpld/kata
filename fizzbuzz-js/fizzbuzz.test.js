const fizzbuzz = require('./fizzbuzz')

describe('Is divisible by', () => {
  test('6 is divisible by 3', () => {
    expect(fizzbuzz.isDivisible(6, 3)).toEqual(true)
  })

  test('7 is not divisible by 3', () => {
    expect(fizzbuzz.isDivisible(7, 3)).toEqual(false)
  })

  test('10 is not divisible by 3', () => {
    expect(fizzbuzz.isDivisible(10, 3)).toEqual(false)
  })

  test('4 is divisible by 2', () => {
    expect(fizzbuzz.isDivisible(4, 2)).toEqual(true)
  })
})

describe('Convert single number to fizzbuzz or string', () => {
  test('2 to string', () => {
    expect(fizzbuzz.numToFizzBuzz(2)).toEqual('2')
  })

  test('3 to fizz', () => {
    expect(fizzbuzz.numToFizzBuzz(3)).toEqual('Fizz')
  })

  test('5 to buzz', () => {
    expect(fizzbuzz.numToFizzBuzz(5)).toEqual('Buzz')
  })

  test('11 to string', () => {
    expect(fizzbuzz.numToFizzBuzz(11)).toEqual('11')
  })

  test('15 to fizzbuzz', () => {
    expect(fizzbuzz.numToFizzBuzz(15)).toEqual('FizzBuzz')
  })
})

// describe('Main function', () => {
//   test('1 through 10', () => {
//     expect(fizzbuzz.main(0, 10)).toEqual(
//       ['1', '2', 'fizz', '4', 'buzz', '6', '7', '8', 'fizz', 'buzz']
//     )
//   })

//   test('90 through 100', () => {
//     expect(fizzbuzz.main(90, 100)).toEqual(
//       ['fizzbuzz', '91', '92', 'fizz', '94', 'buzz', 'fizz', '97', '98', 'fizz', 'buzz']
//     )
//   })
// })
