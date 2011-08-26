
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP')
print locale.currency(188518982.18)
print locale.currency(188518982.18, grouping=True)
