from textstat import textstat
if __name__ == '__main__':
    test_data = 'The quick brown fox jumps over the lazy dog'

#File to be used to test the function
print(textstat.flesch_reading_ease(test_data))
print(textstat.smog_index(test_data))
print(textstat.flesch_kincaid_grade(test_data))
print(textstat.coleman_liau_index(test_data))
print(textstat.automated_readability_index(test_data))
print(textstat.dale_chall_readability_score(test_data))
print(textstat.difficult_words(test_data))
print(textstat.linsear_write_formula(test_data))
print(textstat.gunning_fog(test_data))
print(textstat.text_standard(test_data))
