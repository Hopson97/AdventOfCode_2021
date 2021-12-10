


readLines :: FilePath -> IO[String]
readLines = fmap lines . readFile

larger :: [Int] -> Int
x

day1 :: IO ()
day1 = do
  input <- readLines "day1/input.txt"
  let result = sum $ map (\x -> read x :: Int) input
  print result