import re
import glob

wikilink_regex = re.compile(r'\[\[\s*([^\s]+)\s*\|\s*(.*)\s*\]\]')

for filename in glob.glob('./**/*.md', recursive=True):
    print('Processing', filename)
    with open(filename, 'r+') as fp:
        mdFile = fp.read()
        
        output = wikilink_regex.sub(r'[\2](@notes/\1.md)', mdFile)
        if output == mdFile:
            continue
        with open(filename+'.bak', 'w') as fpbak:
            fpbak.write(mdFile)
        fp.seek(0)
        fp.write(output)
