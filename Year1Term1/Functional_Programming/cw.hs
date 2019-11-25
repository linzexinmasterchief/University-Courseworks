starLine n = (take n (cycle "*")) ++ "\n"
multiLine n s = take (n * (length s)) (cycle s)
steps a b c = starLine b