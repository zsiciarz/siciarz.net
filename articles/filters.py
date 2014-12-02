import markdown


def markitup_filter(content, *args, **kwargs):
    content = markdown.markdown(content, *args, **kwargs)
    return content.replace(
        '<span class="o">&amp;</span><span class="n">amp</span><span class="p">;</span>',
        '<span class="o">&amp;</span>',
    )
