from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from mainapp.models import(
    School,
    Galeria,
    Teacher,
    Rewiew,
    New,
)

from mainapp.serializers import(
    SchoolSerializer,
    TeacherSerializer,
    GaleriaSerializer,
    RewiewSerializer,
    NewSerializer,
)
class SchoolView(ModelViewSet):
    queryset= School.objects.all()
    serializer_class= SchoolSerializer

    def list(self, request, *args, **kwargs):
        return Response(SchoolSerializer(School.objects.first()).data)

class TeacherView(ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class= TeacherSerializer

class GaleriaView(ModelViewSet):
    queryset=Galeria.objects.all()
    serializer_class=GaleriaSerializer

class RewiewView(ModelViewSet):
    queryset=Rewiew.objects.all()
    serializer_class=RewiewSerializer

class NewView(ModelViewSet):
    queryset=New.objects.all()
    serializer_class=NewSerializer

