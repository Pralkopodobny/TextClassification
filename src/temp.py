import pandas as pd
y = pd.read_csv('.\\scale_data\\scaledata\\Dennis+Schwartz\\subj2.Dennis+Schwartz', 
                error_bad_lines=False, delimiter='twuj kutas jebany', header=None)
words_count = {}
for line in y[0]:
    words = line.split(' ')
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else
            words_count[word] = 1

words_count.keys