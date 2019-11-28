starLine n = (take n (cycle "*")) ++ "\n"
multiLine n s = take (n * (length s)) (cycle s)
steps a b c = starLine b

main = do putStr (multiLine 4 (starLine 6))