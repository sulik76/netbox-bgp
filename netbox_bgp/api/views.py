from rest_framework.viewsets import ModelViewSet

from .serializers import (
    ASNSerializer, BGPSessionSerializer, RoutingPolicySerializer, BGPPeerGroupSerializer,
    CommunitySerializer, PrefixListSerializer
)
from netbox_bgp.models import ASN, BGPSession, RoutingPolicy, BGPPeerGroup, Community, PrefixList
from netbox_bgp.filters import (
    ASNFilterSet, BGPSessionFilterSet, RoutingPolicyFilterSet, BGPPeerGroupFilterSet,
    CommunityFilterSet, PrefixListFilterSet
)


class ASNViewSet(ModelViewSet):
    queryset = ASN.objects.all()
    serializer_class = ASNSerializer
    filterset_class = ASNFilterSet


class BGPSessionViewSet(ModelViewSet):
    queryset = BGPSession.objects.all()
    serializer_class = BGPSessionSerializer
    filterset_class = BGPSessionFilterSet


class RoutingPolicyViewSet(ModelViewSet):
    queryset = RoutingPolicy.objects.all()
    serializer_class = RoutingPolicySerializer
    filterset_class = RoutingPolicyFilterSet


class BGPPeerGroupViewSet(ModelViewSet):
    queryset = BGPPeerGroup.objects.all()
    serializer_class = BGPPeerGroupSerializer
    filterset_class = BGPPeerGroupFilterSet


class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    filterset_class = CommunityFilterSet


class PrefixListViewSet(ModelViewSet):
    queryset = PrefixList.objects.all()
    serializer_class = PrefixListSerializer
    filterset_class = PrefixListFilterSet
