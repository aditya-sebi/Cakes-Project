from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework .views import APIView

from rest_framework .response import Response

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

from authentication.permissions import IsAdmin,ISUser

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

from .models import Cakes,Shape,Weight,Category

from .serializers import CakeSerializer,ShapeSerializer,WeightSerializer,CategorySerializer

class CakeCreateListCreateView(APIView):

    serializer_class = CakeSerializer

    # authentication_classes = [BasicAuthentication]
    
    # authentication_classes = [TokenAuthentication]

    authentication_classes =[JWTAuthentication]

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdmin]

        return [permission() for permission in permissions]

    def get(self, request, *args, **kwargs):

        cakes = Cakes.objects.all()

        serializer = self.serializer_class(cakes, many=True)

        return Response(serializer.data, status=200)


    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'cake created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status = 400) 

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    # authentication_classes = [BasicAuthentication]

    # authentication_classes = [TokenAuthentication]

    authentication_classes = [JWTAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method in ['PATCH','DELETE']:

            permissions = [IsAdmin]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')
       
        cake = Cakes.objects.get(id=id)

        serializer = self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cakes.objects.get(id=id)

        serializer = self.serializer_class(data=request.data,instance=cake,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        cake = Cakes.objects.get(id=id)

        cake.delete()

        return Response({'msg':'cake deleted successfully'},status=204)

#shape

class ShapeCreateListCreateView(APIView):

    serializer_class = ShapeSerializer
    
    authentication_classes = [BasicAuthentication]
    
    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self, request, *args, **kwargs):

        shapes = Shape.objects.all()

        serializer = self.serializer_class(shapes, many=True)

        return Response(serializer.data, status=200)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'shape created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status = 400) 

class ShapeRetrieveUpdateDestroyView(APIView):

    serializer_class = ShapeSerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method in ['PATCH','DELETE']:

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        shape = Shape.objects.get(id=id)

        serializer = self.serializer_class(shape)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        shape = Shape.objects.get(id=id)

        serializer = self.serializer_class(data=request.data,instance=shape,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        shape = Shape.objects.get(id=id)

        shape.delete()

        return Response({'msg':'shape deleted successfully'},status=204)

#Category

class CategoryCreateListCreateView(APIView):

    serializer_class = CategorySerializer
    
    authentication_classes = [BasicAuthentication]
    
    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self, request, *args, **kwargs):

        category = category.objects.all()

        serializer = self.serializer_class(category, many=True)

        return Response(serializer.data, status=200)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'category created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status = 400) 

class CategoryRetrieveUpdateDestroyView(APIView):

    serializer_class = CategorySerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method in ['PATCH','DELETE']:

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        category = Category.objects.get(id=id)

        serializer = self.serializer_class(category)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        category = Category.objects.get(id=id)

        serializer = self.serializer_class(data=request.data,instance=category,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        category = Category.objects.get(id=id)

        category.delete()

        return Response({'msg':'category deleted successfully'},status=204)


# Weight

class WeightCreateListCreateView(APIView):

    serializer_class = WeightSerializer
    
    authentication_classes = [BasicAuthentication]
    
    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self, request, *args, **kwargs):

        weight = Weight.objects.all()

        serializer = self.serializer_class(weight, many=True)

        return Response(serializer.data, status=200)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'weight created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status = 400) 

class WeightRetrieveUpdateDestroyView(APIView):

    serializer_class = WeightSerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method in ['PATCH','DELETE']:

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        weight = Weight.objects.get(id=id)

        serializer = self.serializer_class(weight)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        weight = Weight.objects.get(id=id)

        serializer = self.serializer_class(data=request.data,instance=weight,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        weight = Weight.objects.get(id=id)

        weight.delete()

        return Response({'msg':'weight deleted successfully'},status=204)
