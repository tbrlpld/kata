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
