# text5에서 4번 출현하는 단어들을 중복되지 않게 오름차순으로 출력
# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *

freq5 = FreqDist(text5)
arr = [word for word in text5 if freq5[word] == 4]
print(sorted(set(arr)))

#>>> ["''", '(((', '((((((((', '(((((((((', '))))))))))', ',,,,', '..........', '10', '15', '23', '8', '80', ':-(', ':-@', ':O', ':beer:', ':p', '<<', 'Any', 'Dawnstar', 'EST', 'Everyone', 'Florida', 'Go', 'Kittie', 'Like', 'MY', 'Messaging', 'N', 'ONE', 'Ok', 'Private', 'ROOM', 'S', 'South', 'To', 'U', 'U117', 'U123', 'U126', 'U130', 'U133', 'U146', 'U154', 'U196', 'U219', 'U819', 'U820', 'U85', 'U88', 'U988', 'U989', 'Visit', 'We', 'Wellbutrin', 'White', 'Wow', 'afternoon', 'ahh', 'alright', 'asses', 'barbie', 'beat', 'behind', 'between', 'bitch', 'blank', 'box', 'bring', 'c', 'calling', 'caught', 'charge', 'cheap', 'choice', 'claws', 'com', 'country', 'cup', 'cute', 'dam', 'dances', 'darlin', 'date', 'dating', 'daughter', 'depends', 'desert', 'different', 'dirty', 'dis', 'door', 'drive', 'each', 'evil', 'fabric', 'falls', 'fart', 'figure', 'found', 'giggles', 'glad', 'grrr', 'guitar', 'hahahaha', 'happens', 'hehehehe', 'hes', 'heyyy', 'high', 'himself', 'history', 'holy', 'hook', 'http://www.shadowbots.com', 'huge', 'id', 'idiots', 'imagine', 'interested', 'interesting', 'invite', 'j/k', 'jerk', 'joining', 'jus', 'kent', 'knees', 'lame', 'laugh', 'laundry', 'lie', 'line', 'lives', 'lmaoo', 'lmaooo', 'lookin', 'lord', 'lunch', 'mad', 'md', 'mmm', 'mmmm', 'mmmmm', 'mouth', 'needed', 'noise', 'none', 'o.o', 'o/~', 'o0', 'ones', 'open', 'ouch', 'pain', 'parent', 'pass', 'perving', 'pfft', 'pissed', 'pms', 'poooland', 'pretty', 'prison', 'probably', 'promise', 'proud', 'puff', 'pursued', 'questions', 'quit', 'reading', 'realize', 'rest', 'rocker', 'rolling', 'rum', 'screen', 'sea', 'self', 'shane', 'shes', 'shore', 'shot', 'sigh', 'silver', 'smoking', 'socks', 'special', 'spins', 'stuck', 'swear', 'talked', 'team', 'temptations', 'tho', 'three', 'throught', 'tongue', 'trials', 'trying', 'turn', 'ugh', 'ugly', 'umm', 'ummm', 'until', 'w/', 'waiting', 'wanting', 'ways', 'window', 'woohoo', 'woot', 'worked', 'worse', 'wut', 'yawns', 'yeppers', 'yesterday', 'yours', 'yourself']