import io
import csv
from rest_framework.response import Response
from .models import Member
from rest_framework import generics, status
from .serializers import FileUploadSerializer, MemberSerializerTop


class FileUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        if csv_file.name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=','):
                if Member.objects.filter(customer=column[0]).exists():
                    m = Member.objects.get(customer=column[0])
                    m.item.append(column[1])
                    m.total += int(column[2])
                    m.save()
                else:
                    Member.objects.create(
                        customer=column[0],
                        item=[column[1]],
                        total=column[2]
                    )
            m = Member.objects.order_by('-total')[:5]
            for first in m:
                a = []
                for second in m:
                    if first is second:
                        continue
                    b = list(set(first.item).intersection(set(second.item)))
                    if b is not None and b not in a and b != list():
                        a.append(b)
                a = [item for sublist in a for item in sublist]
                first.item_top_five = a
                first.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MemberListAPIView(generics.ListAPIView):
    queryset = Member.objects.order_by('-total')[:5]
    serializer_class = MemberSerializerTop
