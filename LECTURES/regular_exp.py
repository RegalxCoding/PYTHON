#match returns true when exp matches
#character class
#predefined character clas
#quantifier
# import re
# matcher=re.finditer(".","a7b @k9z")
# for match in matcher:
#    print(match.start(),"......",match.group())

import re           #exp    #string
matcher=re.finditer("[abc]","a7b@k9z")
for match in matcher :
   print(match.start(),"......",match.group())


#exclude abc using pattern [^abc]
import re
matcher=re.finditer("[^abc]","a7b@k9z")
for match in matcher :
   print(match.start(),"......",match.group())