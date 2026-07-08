
with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()
import re
# Reduce base font sizes systematically:
# font-size: 1.05rem -> 1.0rem
# font-size: 1.1rem -> 1.0rem
# font-size: 14px -> 13px etc
c = re.sub(r'font-size:\s*1\.1rem;', 'font-size: 1.0rem;', c)
c = re.sub(r'font-size:\s*1\.05rem;', 'font-size: 0.95rem;', c)
c = re.sub(r'font-size:\s*1\.2rem;', 'font-size: 1.1rem;', c)
c = re.sub(r'font-size:\s*1\.5rem;', 'font-size: 1.35rem;', c)
c = re.sub(r'font-size:\s*2\.2rem;', 'font-size: 1.9rem;', c)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(c)

