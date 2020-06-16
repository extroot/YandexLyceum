def goods_analysis(*names, in_sale=lambda x: 'шоколад' in x['название'].lower()):
    return sorted([x for x in names if in_sale(x)], key=lambda x: x['количество'], reverse=True)[:3]
