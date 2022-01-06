--compile with ghc -Ox -threaded --make pi2.hs [where x is # of threads]
--run with ./pi2 +RTS -Nx [where x is the number from above]

--program that finds pi
--multiprocessed

-- cabal-install HasBigDecimal
import Data.BigDecimal
-- cabal-install parallel
import Control.Monad
import Control.Parallel

forloop :: Integer -> [BigDecimal]
forloop n = do
  let k = BigDecimal n 0
  let one1 = (BigDecimal 1 0)/((8*k)+5)
  let one2 = (BigDecimal 1 0)/((8*k)+6)
  let four = (BigDecimal 4 0)/((8*k)+1)
  let two = (BigDecimal 2 0)/((8*k)+4)
  let hex = (BigDecimal 1 0)/(BigDecimal (16^n) 0)
  [hex*(((four-two)-one1)-one2)]

result :: Integer -> [[BigDecimal]]
result n = forM [0..n] $ \k -> forloop k

main :: IO ()
main = do
  putStrLn "Calculate Digits of Pi"
  putStrLn "Enter Number of Hexadecimal Digits (result is decimal):"
  i <- getLine
  let n = read i :: Integer
  -- can't use pi it's a constant in Prelude
  let p = foldr (+) (BigDecimal 0 0) (head (result n))
  putStrLn (toString p)
