num = int(input(""))
prompt_list = []
prompt_word = []
prompt_comparison = []


for i in range(num):
    prompt_list.append(input(""))

prompt_word = [list(word) for word in prompt_list]

for word in prompt_word:
    if not prompt_comparison:
        prompt_comparison = word
    else:
        for i, word_comparison in enumerate(word, 0):
            if word_comparison != prompt_comparison[i]:
                prompt_comparison[i] = '?'

prompt_result = ''.join(prompt_comparison)
print(prompt_result)
