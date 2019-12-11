---------------------------------------------------- part 1 ----------------------------------------------------
-- course work 1
-- generate a line with n "*"
starLine :: Int -> String
starLine n = (take n (cycle "*")) ++ "\n"

-- generate s lines of starLine
multiLine :: Int -> String -> String
multiLine n s = take (n * (length s)) (cycle s)

steps :: Int -> Int -> Int -> String
-- the output is directly "" if any of the parameters is 0
steps _ _ 0 = ""
steps _ 0 _ = ""
steps 0 _ _ = ""
-- generate c blocks of multiline with length (b * c)
steps a b c = (steps a b (c - 1)) ++ multiLine a (starLine (b * c))


---------------------------------------------------- part 2 ----------------------------------------------------
-- course work 2
-- in case the number input is odd
-- n is the width of flag, a is the line number of this line
x_line_odd :: Int -> Int -> String
x_line_odd n a
    | a == (n + 1) `div` 2 = take (n `div` 2) (cycle " ") ++ "*" ++ take (n `div` 2) (cycle " ")
    | (a /= (n + 1) `div` 2) && n > (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")
    | (a /= (n + 1) `div` 2) && n < (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a - 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")

-- generate the x pattern in the centre (don't contain flag top and bottom) when the total line amount is odd
-- n is the width of flag, a is the line number of this line
x_pattern_odd :: Int -> Int -> String
x_pattern_odd _ 0 = ""
x_pattern_odd n a = "*" ++ x_line_odd n a ++ "*\n" ++ x_pattern_odd n (a - 1)

-- in case the number input is even
-- n is the width of flag, a is the line number of this line
x_line_even :: Int -> Int -> String
x_line_even n a
    | a == n `div` 2 = ""
    | (a /= (n + 1) `div` 2) && n > (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a + 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")
    | (a /= (n + 1) `div` 2) && n < (2 * a) = take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ") ++ "*" ++ take (abs (n - (2 * a - 2))) (cycle " ") ++ "*" ++ take ((n `div` 2) - abs(a - ((n + 1) `div` 2))) (cycle " ")

-- generate the x pattern in the centre (don't contain flag top and bottom) when the total line amount is odd
-- n is the width of flag, a is the line number of this line
-- manually add "**" ++ take (n - 2) (cycle " ") ++ "**\n" when a == 0 because a is less than one that the actual line amount needed
x_pattern_even :: Int -> Int -> String
x_pattern_even n 0 = "**" ++ take (n - 2) (cycle " ") ++ "**\n"
x_pattern_even n a
    | a == n `div` 2 = x_pattern_even n (a - 1)
    | otherwise = "*" ++ x_line_even n a ++ "*\n" ++ x_pattern_even n (a - 1)

-- decide whether the amount of lines is odd or even and adds flag top and buttom line
-- assign (a - 2) to both n and a because the top and bottom lines are handdled by the flagpattern function already
flagpattern :: Int -> String
flagpattern a 
    | a `mod` 2 == 1 = take a (cycle "*") ++ "\n" ++ x_pattern_odd (a - 2) (a - 2) ++ take a (cycle "*") ++ "\n"
    | otherwise = take a (cycle "*") ++ "\n" ++ x_pattern_even (a - 2) (a - 2) ++ take a (cycle "*") ++ "\n"


---------------------------------------------------- part 3 ----------------------------------------------------
-- course work 3
substring :: Int -> Int -> String -> String
-- take the substring from index start, with length subLength (including end character)
substring start subLength text = take subLength (drop start text)

-- scan through text, cut off a slice at each time with same length as target and match with target
-- if they are same, replace the target with replace
swapwords :: String -> String -> String -> String
swapwords _ _ [] = []
swapwords target replace text
    | target == substring 0 (length target) text = replace ++ swapwords target replace (drop (length target) text)
    | otherwise = x : swapwords target replace y
    where (x:y) = text

---------------------------------------------------- part 4 ----------------------------------------------------
-- course work 4
-- takes in a string s and a char c, return the index of the first character in string that is same as char c
find_first_same_char :: [Char] -> Char -> Int -> Int
find_first_same_char [] c _ = -1
find_first_same_char (x:xs) c start_pos 
    | x == c = start_pos
    | otherwise = find_first_same_char xs c (start_pos + 1)

remove_index :: [Char] -> Int -> Int -> [Char]
-- remove index i character from str, start from index j
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
-- use ((length (remove_same_char a b) - 1) `mod` 4) to get the last letter when mapping (l,p,h or i) repeatly
compatibility a b = a ++ word_decide ((length (remove_same_char a b) - 1) `mod` 4) ++ b ++ " and " ++ b ++ word_decide ((length (remove_same_char b a) - 1) `mod` 4) ++ a


---------------------------------------------------- part 5 ----------------------------------------------------
-- course work 5
remove_empty :: (Eq a) => [[a]] -> [[a]]
-- remove all empty array elements in the big array
remove_empty [] = []
remove_empty arr
    | x == [] = remove_empty y
    | otherwise = x : remove_empty y
    where (x : y) = arr

-- generallized signature
split :: (Eq a) => [a] -> a -> [[a]]
split [] d = []
-- arr is the array/string to be splited, d is the char/number/... that used as a separation sign to do the split
-- for example if arr = "azabzababz" and d = "z", span (/= d) arr will separate arr from the first "z" and generate ("a","zabzababz")
-- therefore x is "a", y is "zabzababz"
-- drop 1 y => "abzababz"
-- then call split again to do this recursively
split arr d = remove_empty(x : split (drop 1 y) d) where (x,y) = span (/= d) arr