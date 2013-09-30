# -*- coding: utf-8 -*-
from django import template


PAGES = 5

register = template.Library()


@register.inclusion_tag('monitor/pagination.html', takes_context=True)
def bootstrap_pagination(context):
    tag_context = {'is_paginated': context['is_paginated']}
    if tag_context['is_paginated']:
        page_obj = context['page_obj']
        if page_obj.number > PAGES + 1:
            min_num = page_obj.number - PAGES
            dots_left = True
        else:
            min_num = 1
            dots_left = False
        if page_obj.paginator.num_pages - page_obj.number > PAGES:
            max_num = page_obj.number + PAGES
            dots_right = True
        else:
            max_num = page_obj.paginator.num_pages
            dots_right = False
        page_range = xrange(min_num, max_num + 1)

        get_dict = context['request'].GET.copy()
        if 'page' in get_dict:
            del get_dict['page']
        get_query = get_dict.urlencode() + '&' if get_dict else ''

        tag_context.update({
            'page_obj': page_obj,
            'page_range': page_range,
            'dots_left': dots_left,
            'dots_right': dots_right,
            'get_query': get_query,
        })
    return tag_context
