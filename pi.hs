#!/usr/bin/env runhaskell

-- cabal install HasBigDecimal
import Data.BigDecimal

forloop :: BigDecimal -> BigDecimal -> Integer -> IO ()
forloop k pval 0 = putStrLn (toString pval)
forloop k pval end = do
  let one1 = (bigDecimal 1 0)/((8*k)+5)
  let one2 = (bigDecimal 1 0)/((8*k)+6)
  let four = (bigDecimal 4 0)/((8*k)+1)
  let two = (bigDecimal 2 0)/((8*k)+4)
  let hex = (bigDecimal 1 0)/(bigDecimal (16^(value k)) 0)
  -- Can't use pi b/c it's a constant in Prelude
  let p = (hex*(four-two-one1-one2)) + pval
  forloop (k+1) p (end-1)

main :: IO ()
main = do
  putStrLn "Calculate Digits of Pi"
  putStrLn "Enter Number of Hexadecimal Digits (result is decimal):"
  i <- getLine
  let n = bigDecimal (read i :: Integer) 0
  let k = bigDecimal 0 0
  forloop k k (value n)
