import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Remplace "your_project" par le nom de ton projet
django.setup()

import random
from django.utils import timezone
from api.models import Sale, ProductPerformance, MarketTrend  # Remplace "your_app" par le nom de ton application

# Liste de noms de produits fictifs
PRODUCT_NAMES = ["Produit A", "Produit B", "Produit C", "Produit D", "Produit E"]

# Fonction pour générer des données aléatoires
def generate_random_data():
    # Générer des données pour les ventes
    for _ in range(20):  # Générer 20 enregistrements de ventes
        Sale.objects.create(
            product_name=random.choice(PRODUCT_NAMES),
            amount=round(random.uniform(10, 1000), 2),  # Montant entre 10 et 1000
            date=timezone.now() - timezone.timedelta(days=random.randint(0, 30))  # Date aléatoire dans les 30 derniers jours
        )

    # Générer des données pour les performances des produits
    for _ in range(10):  # Générer 10 enregistrements de performances
        ProductPerformance.objects.create(
            product_name=random.choice(PRODUCT_NAMES),
            sales_volume=random.randint(100, 1000),  # Volume de ventes entre 100 et 1000
            customer_rating=round(random.uniform(1, 5), 1),  # Note client entre 1 et 5
            date=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
        )

    # Générer des données pour les tendances du marché
    TREND_NAMES = ["Tendance A", "Tendance B", "Tendance C"]
    for _ in range(5):  # Générer 5 enregistrements de tendances
        MarketTrend.objects.create(
            trend_name=random.choice(TREND_NAMES),
            value=round(random.uniform(0, 100), 2),  # Valeur entre 0 et 100
            date=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
        )

    print("Données aléatoires générées avec succès !")

# Exécuter la fonction
generate_random_data()