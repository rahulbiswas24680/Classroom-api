from django.urls import path
from rest_framework import routers
from .views import ClassroomViewSet, CreatedAssignmentViewSet, CompletedAssignmentViewSet, NoticeViewSet


router = routers.SimpleRouter()

router.register(r'classroom', ClassroomViewSet)
router.register(r'created-assignment', CreatedAssignmentViewSet)
router.register(r'completed-assignment', CompletedAssignmentViewSet)
router.register(r'notice', NoticeViewSet)


urlpatterns = router.urls

