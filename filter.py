def blackList(word, mo):
  if word == 'ある' or word == 'する' or word == 'いる' or word == 'こと' or word == 'れる' or word == 'よう' or word == 'ため' or word == 'ない': True
  if word == '及び' or word == 'および' or word == 'または' or word == 'できる': True
  if len(word) == 1 and ("あ" <= word[0] <= "ん"): True
  return False
