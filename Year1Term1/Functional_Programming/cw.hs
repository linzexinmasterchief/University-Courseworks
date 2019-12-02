-- course work 1
starLine n = (take n (cycle "*")) ++ "\n"

multiLine :: Int -> String -> String
multiLine n s = take (n * (length s)) (cycle s)

steps :: Int -> Int -> Int -> String
steps _ _ 0 = ""
steps a b c = (steps a b (c - 1)) ++ multiLine a (starLine (b * c))

main = do putStr (steps 7 2 3)

-- course work 2
flagpattern a = take a (cycle "*")