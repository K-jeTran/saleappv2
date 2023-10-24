def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]

def load_products(kw):
    products = [{
        'id': 1,
        'name': 'Ipad pro 2022',
        'price': 24000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }, {
        'id': 1,
        'name': 'Iphone 15',
        'price': 14000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }, {
        'id': 1,
        'name': 'Ipad pro 2020',
        'price': 24000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }, {
        'id': 1,
        'name': 'Ipad pro 2018',
        'price': 24000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }, {
        'id': 1,
        'name': 'Ipad 1920',
        'price': 24000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }, {
        'id': 1,
        'name': 'Airpods',
        'price': 24000000,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dIpOKH5CRY6QtTrvDL8GQgjaz8WVyPkgQA&usqp=CAU'
    }]

    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]

    return products