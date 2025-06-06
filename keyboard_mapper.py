import string
from typing import Tuple, Optional, List

# Maximum syllable length to check for (Amharic syllables are at most 3 chars in transliteration)
MAX_BUFFER_LEN =2
VOWELS = {'a', 'e', 'i', 'o', 'u'}
PUNCTUATION = set(string.punctuation + " ")  # Includes spaces and common punctuation

# Base map: maps single Latin letters to Amharic base characters
base_map = {
    'h': 'ሀ', 'l': 'ለ', 'm': 'መ', 's': 'ሰ', 'r': 'ረ',
    'b': 'በ', 't': 'ተ', 'c': 'ቸ', 'n': 'ነ', 'k': 'ከ',
    'x': 'ኸ', 'x': 'አ', 'z': 'ዘ', 'y': 'የ', 'd': 'ደ',
    'g': 'ገ', 'f': 'ፈ', 'p': 'ጰ',
    # Additional base characters
    'S': 'ሠ', 'H': 'ሐ', 'M': 'መ', 'q': 'ቀ', 'v': 'ቨ', 'N': 'ኘ',
    'K': 'ኸ', 'w': 'ወ', 'Z': 'ዐ', 'Z': 'ዠ', 'j': 'ጀ', 'T': 'ጠ',
    'C': 'ጨ', 'P': 'ፐ', 'X': 'ጸ', 'Q': 'ፀ',
}

# Syllable map: maps Latin phonetic syllables to full Amharic syllables
syllable_map = {
    'h':['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ','ኋ'],
    'l':['ለ','ሉ','ሊ','ላ','ሌ','ል','ሎ','ሏ'],
    'h2':['ሐ','ሑ','ሒ','ሓ','ሔ','ሕ','ሖ','ሗ'],
    'm':['መ','ሙ','ሚ','ማ','ሜ','ም','ሞ','ሟ'],
    's2':['ሠ','ሡ','ሢ','ሣ','ሤ','ሥ','ሦ','ሧ'],
    'r':['ረ','ሩ','ሪ','ራ','ሬ','ር','ሮ','ሯ'],
    's':['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ','ሷ'],
    'sh':['ሸ','ሹ','ሺ','ሻ','ሼ','ሽ','ሾ','ሿ'],
    'q':['ቀ','ቁ','ቂ','ቃ','ቄ','ቅ','ቆ','ቋ'],
    'b':['በ','ቡ','ቢ','ባ','ቤ','ብ','ቦ','ቧ'],
    'v':['ቨ','ቩ','ቪ','ቫ','ቬ','ቭ','ቮ','ቯ'],
    't':['ተ','ቱ','ቲ','ታ','ቴ','ት','ቶ','ቷ'],
    'ch':['ቸ','ቹ','ቺ','ቻ','ቼ','ች','ቾ','ቿ'],
    'n':['ነ','ኑ','ኒ','ና','ኔ','ን','ኖ','ኗ'],
    'gn':['ኘ','ኙ','ኚ','ኛ','ኜ','ኝ','ኞ','ኟ'],
    'e':['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ','ኧ'],
    'a':['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ','ኧ'],
    'k':['ከ','ኩ','ኪ','ካ','ኬ','ክ','ኮ','ኳ'],
    'w':['ወ','ዉ','ዊ','ዋ','ዌ','ው','ዎ',''],
    'z':['ዘ','ዙ','ዚ','ዛ','ዜ','ዝ','ዞ','ዟ'],
    'zh':['ዠ','ዡ','ዢ','ዣ','ዤ','ዥ','ዦ','ዧ'],
    'y':['የ','ዩ','ዪ','ያ','ዬ','ይ','ዮ','ዯ'],
    'd':['ደ','ዱ','ዲ','ዳ','ዴ','ድ','ዶ','ዷ'],
    'j':['ጀ','ጁ','ጂ','ጃ','ጄ','ጅ','ጆ','ጇ'],
    'g':['ገ','ጉ','ጊ','ጋ','ጌ','ግ','ጎ','ጏ'],
    'x':['ጠ','ጡ','ጢ','ጣ','ጤ','ጥ','ጦ','ጧ'],
    'c':['ጨ','ጩ','ጪ','ጫ','ጬ','ጭ','ጮ','ጯ'],
    'ts2':['ጰ','ጱ','ጲ','ጳ','ጴ','ጵ','ጶ','ጷ'],
    'ph':['ጰ','ጹ','ጺ','ጻ','ጼ','ጽ','ጾ','ጷ'],
    'ts':['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ','ፇ'],
    'f':['ፈ','ፉ','ፊ','ፋ','ፌ','ፍ','ፎ','ፏ'],
    'p':['ፐ','ፑ','ፒ','ፓ','ፔ','ፕ','ፖ','ፗ'],
    ' ':[' ',' ',' ',' ',' ',' ',' ',' '],
    '-':['፡'],
    ',':['፣'],
    '.':['።'],
    ';':['፤'],
    ':':['፥']
    
   
}

def get_phonetic_amharic(buffer):
    """
    Match the longest suffix of the buffer against the syllable_map and the base map.
    """
    if not buffer:
        return None, 0

    joined = ''.join(buffer).lower()

    # Try longest match first (e.g., "sh", "sha", etc.)
    for size in reversed(range(1, min(MAX_BUFFER_LEN, len(joined)) + 1)):
        piece = joined[-size:]
        if piece in syllable_map:
            return syllable_map[piece], size
        elif joined in VOWELS:
            return None, 1

    return None, 0


