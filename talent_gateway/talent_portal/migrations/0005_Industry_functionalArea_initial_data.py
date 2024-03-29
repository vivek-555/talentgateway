# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:48
from __future__ import unicode_literals

from django.db import migrations
from django.apps import apps

Industry = apps.get_model("talent_portal", "industry")
FunctionalArea = apps.get_model("talent_portal", "functionalarea")
SUPERADMIN_EMAIL_ADDRESS = "admin@abc.com"  # FIXME: change to real email address later

def forward_func(*args, **kwargs):
    print("Inserting Industry and Functional Area in database...")

    try:
        Industry.objects.create(name="Accounting/Tax/Audit", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="HR/Recruitment/Staffing", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Retail/SuperMarkets", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Consumer Goods/CPG/FMCG", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Home Appliances", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Heavy Electricals/Machinery", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Food & Beverages", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Apparel/Fashion", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Luxury Goods/Jewelery", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Textile", alias=None, created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Banking/Mortgage", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Capital Markets/Hedge Fund", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Financial Services/NBFC", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Private Equity/VC", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="ITES/Computer Software", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Computer Hardware", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Insurance", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Telecom", alias=None, created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Architecture/Planning", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Arts/Crafts", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Automotive", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Aviation/Aerospace", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Biotechnology/Greentech", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Cosmetics", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Dairy", alias=None, created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Furniture", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Graphic Design/Web Design", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Internet", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Sporting Goods", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Entertainment/Movie/Media Production", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Events Services", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Publishing Industry", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Corporate Communication/IR/PR", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Health/Fitness", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Education/Training", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Hospital/Health Care", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Hospitality/Restaurants", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Management Consulting", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Market Research", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Non-Profit/Volunteering", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Oil/Energy/Solar/Greentech", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Outsourcing/Offshoring/COE", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="KPO/Analytics", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Construction/Civil/Infrastructure", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Pharma/Bio-Tech", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Chemical/Plastic/Rubber", alias=None,
                                created_by=SUPERADMIN_EMAIL_ADDRESS)
        Industry.objects.create(name="Paint", alias=None, created_by=SUPERADMIN_EMAIL_ADDRESS)

        FunctionalArea.objects.create(name="WebSite Development", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Software Engineer", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Sales/BD", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="QA/Testing", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Networking", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Security", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Trade Marketing", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Project Management", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Operations", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Client/Account Management", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Product Development", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Facility", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="HR/Recruitment/Payroll", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Data Entry", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Voice Process", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Non Voice Customer Service", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="BPO", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Analytics", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Actuary", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="CFA", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Accountant", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Tax", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Auditor", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Reporting", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Engineer", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Marketing/Media Planning/PR/Advertising", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Vertical/Category Management", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)
        FunctionalArea.objects.create(name="Store Manager", alias=None,
                                      created_by=SUPERADMIN_EMAIL_ADDRESS)

    except Exception as e:
        print("There was some error: " + str(e))

    print ("Insertion complete!")


def reverse_func(*args, **kwargs):
    print("Removing all data from Industry and Functional Area")
    try:
        Industry.objects.all().delete()
        FunctionalArea.objects.all().delete()
    except Exception as e:
        print("There was some error: " + str(e))

    print("Removed all data from Industry and Functional Area")


class Migration(migrations.Migration):
    dependencies = [
        ('talent_portal', '0004_degree_initial_data'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_code=reverse_func),
    ]