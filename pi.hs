#!/usr/bin/env runhaskell

-- cabal install HasBigDecimal
import Data.BigDecimal

forloop :: BigDecimal -> BigDecimal -> BigDecimal -> IO ()
forloop n k value = do
  let one1 = (BigDecimal 1 0)/((8*k)+5)
  let one2 = (BigDecimal 1 0)/((8*k)+6)
  let four = (BigDecimal 4 0)/((8*k)+1)
  let two = (BigDecimal 2 0)/((8*k)+4)
  let hex = (BigDecimal 1 0)/(BigDecimal (16^(getValue k)) 0)
  -- Can't use pi b/c it's a constant in Prelude
  let p = (hex*(four-two-one1-one2)) + value
  if ((getValue n) == (getValue k)) then
    putStrLn (toString p)
  else
    forloop n (k+1) p

main :: IO ()
main = do
  putStrLn "Calculate Digits of Pi"
  putStrLn "Enter Number of Hexadecimal Digits (result is decimal):"
  i <- getLine
  let n = BigDecimal (read i :: Integer) 0
  let k = BigDecimal 0 0
  forloop n k k
