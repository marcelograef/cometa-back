from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializer, OrderSerializer
from .services import get_stock_data, get_order_data

class StockView(APIView):
    def get(self, request):
        stock_data = get_stock_data()  # Fetch data from the service
        serializer = StockSerializer(stock_data)  # Serialize the data
        return Response(serializer.data)

class OrderView(APIView):
    def get(self, request):
        order_data = get_order_data()  # Fetch data from the service
        serializer = OrderSerializer(order_data)  # Serialize the data
        return Response(serializer.data)
