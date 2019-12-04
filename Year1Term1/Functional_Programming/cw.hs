-- course work 1
starLine n = (take n (cycle "*")) ++ "\n"

multiLine :: Int -> String -> String
multiLine n s = take (n * (length s)) (cycle s)

steps :: Int -> Int -> Int -> String
steps _ _ 0 = ""
steps a b c = (steps a b (c - 1)) ++ multiLine a (starLine (b * c))


-- course work 2
x_line_odd n a
    | a == (n + 1) `div` 2 = take (n `div` 2) (cycle " ") ++ "*" ++ take (n `div` 2) (cycle " ")
    | (a /= (n + 1) `div` 2) && n > (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")
    | (a /= (n + 1) `div` 2) && n < (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a - 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")

x_pattern_odd _ 0 = ""
x_pattern_odd n a = "*" ++ x_line_odd n a ++ "*\n" ++ x_pattern_odd n (a - 1)

x_line_even n a
    | a == n `div` 2 = ""
    | (a /= (n + 1) `div` 2) && n > (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a + 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")
    | (a /= (n + 1) `div` 2) && n < (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a - 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")

x_pattern_even _ 0 = ""
x_pattern_even n a
    | a == n `div` 2 = x_pattern_even n (a - 1)
    | otherwise = "*" ++ x_line_even n a ++ "*\n" ++ x_pattern_even n (a - 1)

flagpattern a 
    | a `mod` 2 == 1 = take a (cycle "*") ++ "\n" ++ x_pattern_odd (a - 2) (a - 2) ++ take a (cycle "*") ++ "\n"
    | otherwise = take a (cycle "*") ++ "\n" ++ x_pattern_even (a - 2) (a - 2) ++ take a (cycle "*") ++ "\n"


-- course work 3

main = do putStr (flagpattern 13)