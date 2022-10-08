print('영어 단어 맞추기 퀴즈')
eng_words={'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car','비행기':'airplane'}
for key in eng_words:
    ans=input('%s 에 해당하는 영어단어를 입력해 주세요.'%key)
    if ans==eng_words[key]:
        print('정답 입니다.')
    else:
        print('틀렸습니다.')
