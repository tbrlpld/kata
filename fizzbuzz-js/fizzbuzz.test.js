const fizzbuzz = require('./fizzbuzz')

describe('Main function', () => {
  test('1 through 10', () => {
    expect(fizzbuzz.main(0, 10)).toEqual(
      ['1', '2', 'fizz', '4', 'buzz', '6', '7', '8', 'fizz', 'buzz']
    )
  })

  test('90 through 100', () => {
    expect(fizzbuzz.main(90, 100)).toEqual(
      ['fizzbuzz', '91', '92', 'fizz', '94', 'buzz', 'fizz', '97', '98', 'fizz', 'buzz']
    )
  })
})
