# Generated by Django 4.0.3 on 2022-03-01 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('firstName', models.CharField(max_length=200, verbose_name='first name')),
                ('lastName', models.CharField(max_length=200, verbose_name='last name')),
                ('phoneNumberOne', models.CharField(max_length=11, verbose_name='phone number one')),
                ('phoneNumberTwo', models.CharField(blank=True, max_length=11, null=True, verbose_name='phone number two')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='email')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='street')),
                ('detailedAddress', models.CharField(blank=True, max_length=400, null=True, verbose_name='detailed address')),
                ('additionalInformation', models.CharField(blank=True, max_length=400, null=True, verbose_name='additional information')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('shipping_cost', models.IntegerField(verbose_name='shipping cost')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(choices=[('NEW', 'NEW'), ('PROCESSING', 'PROCESSING'), ('SHIPPED', 'SHIPPED'), ('COMPLETED', 'COMPLETED'), ('REFUNDED', 'REFUNDED')], max_length=255, verbose_name='title')),
                ('is_default', models.BooleanField(verbose_name='is default')),
            ],
            options={
                'verbose_name': 'order status',
                'verbose_name_plural': 'order statuses',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('imageOne', models.ImageField(blank=True, upload_to='')),
                ('imageTwo', models.ImageField(blank=True, upload_to='')),
                ('imageThree', models.ImageField(blank=True, upload_to='')),
                ('imageFour', models.ImageField(blank=True, upload_to='')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='short description')),
                ('long_description', models.TextField(blank=True, null=True, verbose_name='long description')),
                ('countInStock', models.IntegerField(default=0, verbose_name='count in stock')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='ecommerce.category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(verbose_name='item quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product', verbose_name='product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=0, max_digits=1000, verbose_name='total')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.address', verbose_name='address')),
                ('items', models.ManyToManyField(related_name='order', to='ecommerce.orderitem', verbose_name='order items')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce.orderstatus', verbose_name='status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='ecommerce.city'),
        ),
    ]