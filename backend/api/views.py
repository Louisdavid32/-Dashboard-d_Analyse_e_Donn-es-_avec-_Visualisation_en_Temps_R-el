from rest_framework import viewsets
from .models import Sale, ProductPerformance, MarketTrend
from .serializers import SaleSerializer, ProductPerformanceSerializer, MarketTrendSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class ProductPerformanceViewSet(viewsets.ModelViewSet):
    queryset = ProductPerformance.objects.all()
    serializer_class = ProductPerformanceSerializer

class MarketTrendViewSet(viewsets.ModelViewSet):
    queryset = MarketTrend.objects.all()
    serializer_class = MarketTrendSerializer



@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()

        # Logique du chatbot
        if "montre-moi les ventes du produit" in user_message:
            product_name = user_message.replace("montre-moi les ventes du produit", "").strip()
            sales = Sale.objects.filter(product_name__iexact=product_name)
            if sales.exists():
                sales_data = [sale.amount for sale in sales]
                labels = [sale.date.strftime('%Y-%m-%d') for sale in sales]

                # Renvoyer un graphique
                response = {
                    'reply': f"Voici les ventes du {product_name} :",
                    'chart': {
                        'type': 'bar',
                        'data': {
                            'labels': labels,
                            'datasets': [{
                                'label': f'Ventes du {product_name}',
                                'data': sales_data,
                                'backgroundColor': 'rgba(75, 192, 192, 0.6)',
                            }]
                        },
                        'options': {
                            'responsive': true,
                            'maintainAspectRatio': false,
                            'scales': {
                                'y': {
                                    'beginAtZero': true
                                }
                            }
                        }
                    }
                }
            else:
                response = {'reply': f"Aucune vente trouvée pour le produit {product_name}."}

        elif "quel est le produit le plus vendu" in user_message:
            # Trouver le produit le plus vendu
            from django.db.models import Sum
            most_sold_product = Sale.objects.values('product_name').annotate(total_sales=Sum('amount')).order_by('-total_sales').first()

            if most_sold_product:
                response = {'reply': f"Le produit le plus vendu est {most_sold_product['product_name']} avec {most_sold_product['total_sales']} unités vendues."}
            else:
                response = {'reply': "Aucune donnée de vente disponible."}

        else:
            response = {'reply': "Je ne comprends pas votre demande. Pouvez-vous reformuler ?"}

        return JsonResponse(response)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)