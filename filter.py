# Trueは無効、 Falseは有効な単語
def blackList(word, mo):
  ignoreWords = [
    'なる','ある','する','いる','こと','なく',
    'れる','よう','ため','ない','とき','なり',
    'とる','もの','ぞれぞれ','この','その','せる',
    'うち','では','でも','もっ','べき','より','もより',
    'でき','必ず','もた',
    '及び','および','または','できる','られる','また',
    '図','第',
  ]
  if word in ignoreWords: return True
  if len(word) == 1 and ("あ" <= word[0] <= "ん"): return True
  return False
