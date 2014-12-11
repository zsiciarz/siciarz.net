import re

import markdown


def markitup_filter(content, *args, **kwargs):
    content = markdown.markdown(content, *args, **kwargs)
    content = re.sub(
        r'<span class="o">&amp;</span><span class="n">amp</span><span class="p">;(.*)</span>',
        r'<span class="o">&amp;</span><span class="p">\1</span>',
        content
    )
    return content.replace('<span class="n">amp</span><span class="p">;</span>', '')
