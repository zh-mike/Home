text = "aaabbbbcc"

def text_in_list(text):
    new_list = []
    i = 0
    while i < len(text):
        try:
            if text[i+1] != text[i]:
                new_list.append(text[:i+1])
                text = text[i+1:]
                i = 0
            else:
                i +=1
        except IndexError:
            new_list.append(text)
            return new_list


def compress(lis):
    final_st = ""
    for i in lis:
        final_st = f"{final_st }{len(i)}{i[0]}"
    return final_st

    

my_text = "aaabbbbcc"
lis = text_in_list(my_text)
print(f"{my_text} = {compress(lis)}")