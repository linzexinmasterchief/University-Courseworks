-- course work 1
starLine n = (take n (cycle "*")) ++ "\n"

multiLine :: Int -> String -> String
multiLine n s = take (n * (length s)) (cycle s)

steps :: Int -> Int -> Int -> String
steps _ _ 0 = ""
steps a b c = (steps a b (c - 1)) ++ multiLine a (starLine (b * c))


-- course work 2
-- in case the number input is odd
x_line_odd n a
    | a == (n + 1) `div` 2 = take (n `div` 2) (cycle " ") ++ "*" ++ take (n `div` 2) (cycle " ")
    | (a /= (n + 1) `div` 2) && n > (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")
    | (a /= (n + 1) `div` 2) && n < (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a - 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")

x_pattern_odd _ 0 = ""
x_pattern_odd n a = "*" ++ x_line_odd n a ++ "*\n" ++ x_pattern_odd n (a - 1)

-- in case the number input is even
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
swapsplit :: String -> String -> String -> [String]
swapsplit d t [] = []
swapsplit d t s
    | x == d    = t : swapsplit d t (drop 1 y)
    | x /= d    = x : swapsplit d t (drop 1 y)
    where
        (x,y) = span (/= ' ') s

swapwords d t s = unwords (swapsplit d t s) ++ "\n"

main = do putStr (swapwords "lamb" "buffalo" "Mary has a little lamb whose fleece")


-- course work 4
find_first_same_char :: [Char] -> Char -> Int -> Int
find_first_same_char [] c _ = -1
find_first_same_char (x:xs) c start_pos 
    | x == c = start_pos
    | otherwise = find_first_same_char xs c (start_pos + 1)

remove_index :: [Char] -> Int -> Int -> [Char]
-- remove index i from str, start at j
remove_index [] i j = []
remove_index str i j
    | i == j = remove_index y i (j + 1)
    | otherwise = x : remove_index y i (j + 1)
    where (x:y) = str

remove_same_char :: [Char] -> [Char] -> [Char]
-- remove the chars that appears in b in the first string, and remove all spaces
remove_same_char [] b = []
-- if x (the first char) is in b, remove x (with "|| x == ' ', ignore spaces")
remove_same_char (x:y) b
    | find_first_same_char b x 0 /= -1 || x == ' ' = remove_same_char y (remove_index b (find_first_same_char b x 0) 0)
    | otherwise = x : remove_same_char y b

-- decide which piece of text should be used
word_decide :: Int -> [Char]
word_decide n
    | n == 0 = " loves "
    | n == 1 = " is physical to "
    | n == 2 = " hates "
    | n == 3 = " is indifferent to "
    | otherwise = " "

compatibility :: [Char] -> [Char] -> [Char]
-- connect all pieces together
compatibility a b = a ++ word_decide ((length (remove_same_char a b) - 1) `mod` 4) ++ b ++ " and " ++ b ++ word_decide ((length (remove_same_char b a) - 1) `mod` 4) ++ a

-- course work 5
split [] d = []
split arr d = x : split (drop 1 y) d where (x,y) = span (/= d) arr