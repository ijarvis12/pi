#!/usr/bin/env runhaskell

-- cabal install HasBigDecimal --lib
import Data.BigDecimal

forLoop :: BigDecimal -> BigDecimal -> Integer -> IO ()
forLoop k pval 2 = print pval
forLoop k pval end = do
  let one1 = (BigDecimal 1 0)/((8*k)+5)
  let one2 = (BigDecimal 1 0)/((8*k)+6)
  let four = (BigDecimal 4 0)/((8*k)+1)
  let two = (BigDecimal 2 0)/((8*k)+4)
  let hex = (BigDecimal 1 0)/(BigDecimal (16^(value k)) 0)
  -- Can't use pi b/c it's a constant in Prelude
  let p = (hex*(four-two-one1-one2)) + pval
  forLoop (k+1) p (end-1)

main :: IO ()
main = do
  putStrLn "Calculate Digits of Pi"
  putStrLn "Enter Number of Hexadecimal Digits (result is decimal):"
  i <- getLine
  let n = read i :: Integer
  let k = BigDecimal 0 0
  forLoop k k n
