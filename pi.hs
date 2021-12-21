#!/usr/bin/env runhaskell

import Data.BigDecimal

forloop :: BigDecimal -> BigDecimal -> BigDecimal -> [Char]
forloop n k value = do
  let one = BigDecimal 1 0
  let four = BigDecimal 4 0
  let two = BigDecimal 2 0
  let pi = value + (one/(16^(getValue k)))*(four/(8*k+1)-two/(8*k+4)-one/(8*k+5)-one/(8*k+6))
  if ((getValue n) == (getValue k)) then
    toString pi
  else
    forloop n (k+1) pi

main :: IO ()
main = do
  putStrLn "Calculate Digits of Pi"
  putStrLn "Enter Number of Hexadecimal Digits (result is decimal):"
  i <- getLine
  let n = BigDecimal (read i :: Integer) 0
  let k = BigDecimal 0 0
  let pi = BigDecimal 0 0
  putStrLn (forloop n k pi)
  return ()
