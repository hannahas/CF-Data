def check_anagrams(first_words, second_words):
    anagrams = []
	for words in range(0,len(first_words)):
    	first_letters = sorted(list(first_words[words]))
	    second_letters = sorted(list(second_words[words]))
	    if first_letters == second_letters:
    	    anagrams.append(1)
    	else:
        	anagrams.append(0)
	print(anagrams)
	
anagrams = []
for words in range(0,len(first_words)):
    str1_list = list(first_words[words])
    str1_list.sort()
    str2_list = list(second_words[words])
    str2_list.sort()
    if str1_list == str2_list:
    	anagrams.append(1)
    else:
    	anagrams.append(0)
print(anagrams)


def check_braces(expressions):
output = []
opens = "{[(<"
closes = "}])>"
for x in expressions:
	stack = []
    for c in x:
        if c in opens:
            stack.append(c)
        elif c in closes:
            if not len(stack): #if the stack is empty
                output.append(0)
                break
            else:
                stackTop = stack.pop()
                balancer = opens[closes.index(c)]
                if stackTop == balancer:
                    output.append(1)
                    break
                else:
                    output.append(0)
                    break
print output