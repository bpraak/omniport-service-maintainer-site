import swapper
from rest_framework import viewsets
from maintainer_site.serializers.maintainer_info import MaintainerInfoSerializer
from maintainer_site.models.maintainer_info import MaintainerInformation
from kernel.enums.active_status import ActiveStatus

Maintainer = swapper.load_model('kernel', 'Maintainer')

class MaintainerInfoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing all the Maintainer's Information
    """
    
    serializer_class = MaintainerInfoSerializer
    queryset = MaintainerInformation.objects.all()
    
class ActiveMaintainerInfoViewSet(MaintainerInfoViewSet):
    """
    A viewset for viewing and editing all the active Maintainer's Information
    """

    pagination_class = None

    def get_queryset(self):
        queryset = Maintainer.objects_filter(ActiveStatus.IS_ACTIVE).all()
        queryset_map = []
        for obj in queryset:
            if hasattr(obj, 'maintainerinformation'):
                queryset_map.append(obj.maintainerinformation)
        return queryset_map

class InactiveMaintainerInfoViewSet(MaintainerInfoViewSet):
    """
    A viewset for viewing and editing all the inactive Maintainer's Information
    """

    def get_queryset(self):
        queryset = Maintainer.objects_filter(ActiveStatus.IS_INACTIVE).all()
        queryset_map = []
        for obj in queryset:
            if hasattr(obj, 'maintainerinformation'):
                queryset_map.append(obj.maintainerinformation)
        return queryset_map
