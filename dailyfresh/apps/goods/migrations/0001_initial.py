# Generated by Django 2.1.7 on 2019-05-08 10:01

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodSKUImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_image', models.ImageField(upload_to='goods', verbose_name='商品图片')),
            ],
            options={
                'db_table': 'df_good_sku_image',
                'verbose_name_plural': '商品图片',
                'verbose_name': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodSPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('spu_title', models.CharField(max_length=64, verbose_name='商品SPU名称')),
                ('spu_detail', tinymce.models.HTMLField(blank=True, verbose_name='商品SPU详情')),
            ],
            options={
                'db_table': 'df_good_spu',
                'verbose_name_plural': '商品spu',
                'verbose_name': '商品spu',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=20, verbose_name='商品名称')),
                ('detail', models.CharField(max_length=256, verbose_name='商品简介')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('unite', models.CharField(max_length=20, verbose_name='单位')),
                ('status', models.SmallIntegerField(choices=[(1, '上架'), (0, '下架')], default=1, verbose_name='商品状态')),
                ('image', models.ImageField(upload_to='goods', verbose_name='商品图片')),
                ('stock', models.IntegerField(default=1, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodSPU', verbose_name='所属SPU')),
            ],
            options={
                'db_table': 'df_good_sku',
                'verbose_name_plural': '商品sku',
                'verbose_name': '商品sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(upload_to='goods', verbose_name='种类图片')),
                ('title', models.CharField(max_length=64, verbose_name='种类名称')),
                ('logo', models.CharField(max_length=20, verbose_name='标识')),
            ],
            options={
                'db_table': 'df_goods_class',
                'verbose_name_plural': '商品种类',
                'verbose_name': '商品种类',
            },
        ),
        migrations.CreateModel(
            name='IndexByTurns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('turns_image', models.ImageField(upload_to='goods', verbose_name='首页轮播商品图片')),
                ('turns_index', models.SmallIntegerField(default=0, verbose_name='商品展示顺序')),
                ('turns_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name='所属商品SKU')),
            ],
            options={
                'db_table': 'df_index_by_turns',
                'verbose_name_plural': '首页轮播商品',
                'verbose_name': '首页轮播商品',
            },
        ),
        migrations.CreateModel(
            name='IndexClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('index_display_type', models.SmallIntegerField(choices=[(0, '标题'), (1, '图片')], default=1, verbose_name='展示类型')),
                ('index_index', models.IntegerField(verbose_name='展示顺序')),
                ('index_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='商品所属分类')),
                ('index_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name='所属分类商品')),
            ],
            options={
                'db_table': 'df_index_class',
                'verbose_name_plural': '首页分类商品展示',
                'verbose_name': '首页分类商品展示',
            },
        ),
        migrations.CreateModel(
            name='IndexSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('sales_title', models.CharField(max_length=20, verbose_name='活动名称')),
                ('sales_image', models.ImageField(upload_to='goods', verbose_name='首页促销商品图片')),
                ('sales_urls', models.URLField(verbose_name='活动链接')),
                ('sales_index', models.SmallIntegerField(verbose_name='展示顺序')),
            ],
            options={
                'db_table': 'df_index_sales',
                'verbose_name_plural': '首页促销商品',
                'verbose_name': '首页促销商品',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='所属种类'),
        ),
        migrations.AddField(
            model_name='goodskuimage',
            name='goods_sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name='所属商品'),
        ),
    ]
