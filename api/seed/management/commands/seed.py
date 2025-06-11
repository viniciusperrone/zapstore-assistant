from django.core.management.base import BaseCommand
from django.utils.timezone import now

from brands.models import Brand
from categories.models import Category
from products.models import Product


"""
    Populates the database with initial data on brands, categories and products.
"""
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        brands_data = [
            (1, 'Logitech', 'Marca líder em periféricos de informática'),
            (2, 'Razer', 'Especialista em produtos gamer de alta performance'),
            (3, 'Corsair', 'Fabricante de hardware e periféricos premium'),
            (4, 'HyperX', 'Periféricos e componentes voltados ao público gamer'),
            (5, 'Dell', 'Marca tradicional em tecnologia e computadores'),
        ]

        for id, name, desc in brands_data:
            Brand.objects.update_or_create(id=id, defaults={
                'name': name,
                'description': desc,
                'updated_at': now(),
            })

        categories_data = [
            (1, 'Teclados', 'Teclados mecânicos, gamer e convencionais'),
            (2, 'Mouses', 'Mouses com fio, sem fio e gamer'),
            (3, 'Monitores', 'Monitores LED, LCD, 144Hz, 4K'),
            (4, 'Headsets', 'Fones de ouvido e headsets para jogos e uso profissional'),
            (5, 'Acessórios', 'Outros acessórios como mousepads, suportes e hubs USB'),
        ]

        for id, name, desc in categories_data:
            Category.objects.update_or_create(id=id, defaults={
                'name': name,
                'description': desc,
                'updated_at': now(),
            })

        products_data = [
            (1, 'Logitech K380', 'Teclado Bluetooth compacto multidispositivos', 'LK380-001', 120.00, 199.00, 15, 1, 1),
            (2, 'Razer BlackWidow V3', 'Teclado mecânico gamer com switches verdes Razer', 'RBWV3-202', 380.00, 599.00, 10, 1, 2),
            (3, 'Corsair Harpoon RGB', 'Mouse gamer com sensor óptico de 6000 DPI', 'CHRGB-311', 90.00, 159.00, 25, 2, 3),
            (4, 'HyperX Cloud II', 'Headset com som surround 7.1, microfone removível', 'HXCI-044', 250.00, 399.00, 12, 4, 4),
            (5, 'Dell SE2422H', 'Monitor 24” Full HD 75Hz com HDMI e VGA', 'DSE24-500', 480.00, 799.00, 8, 3, 5),
            (6, 'Razer Goliathus Medium', 'Mousepad gamer com superfície otimizada', 'RGMP-066', 50.00, 89.00, 30, 5, 2),
        ]

        for id, title, desc, sn, cost, sell, qty, cat_id, brand_id in products_data:
            Product.objects.update_or_create(id=id, defaults={
                'title': title,
                'description': desc,
                'serie_number': sn,
                'cost_price': cost,
                'selling_price': sell,
                'quantity': qty,
                'category_id': cat_id,
                'brand_id': brand_id,
                'updated_at': now(),
            })

        self.stdout.write(self.style.SUCCESS('Seed applied successfully!'))
