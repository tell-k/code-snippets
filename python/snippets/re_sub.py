
import re

print re.sub(r'(http(:?s)?://\S+)\b', r'<a href="\1">\1</a>', u'a http://example.com/a/b/c a http://beproud.jpあ')
#a <a href="http://example.com/a/b/c">http://example.com/a/b/c</a> a <a href="http://beproud.jp">http://beproud.jp</a>あ
print re.sub(r'(http(:?s)?://\S+)\b', r'<a href="\1">\1</a>', u'http://aodag.com←おぬぬめ')
#<a href="http://aodag.com">http://aodag.com</a>←おぬぬめ
