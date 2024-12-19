"""
teamwork URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    CAN OPTIONALLY INCLUDE A CONVERTER TYPE. I.e: <int: index>. Otherwise all <index> will be passed as string. -kp
"""
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from teamwork.apps.core import helpers as core_helpers
# Core Imports
from teamwork.apps.core.views import (AboutView, ContactView, LandingView,
                                      LoginView)
# Course Imports
from teamwork.apps.courses.views import BaseView as CourseBaseView
from teamwork.apps.courses.views import (CourseView, EditCourseView,
                                         EmailCourseView, InterestView,
                                         MatchesView, MyCoursesView, StatsView)
# Profile Imports
from teamwork.apps.profiles.views import AlertView
from teamwork.apps.profiles.views import BaseView as ProfileBaseView
from teamwork.apps.profiles.views import (EditProfileView, EditScheduleView,
                                          ProfileView)
# Project Imports
from teamwork.apps.projects.views import BaseView as ProjectBaseView
from teamwork.apps.projects.views import (EditProjectView, EditTsrView,
                                          MeetingsView, MyProjectsView,
                                          ProjectView, TsrView)

urlpatterns = [
        # CORE AND SIGNUP
        path('', LandingView.index, name='index'),
        # Button to Disable course
        path('<str:slug>/disable/',LandingView.disable , name='landing_disable'),
        # /about/
        path('about/', AboutView.about, name='about'),
        # /signup/
        path('signup/', ProfileBaseView.signup, name='signup'),
        # /contact/
        path('contact/', ContactView.contact, name='contact'),
        path('profSignup/', ProfileBaseView.profSignup, name='profSignup'),
        path('search/', core_helpers.search, name='search'),
        path('password_reset/', auth_views.password_reset, name='password_reset'),
        path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
        re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
        path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

        # PROJECT
        # /create_project/
        path('project/create/', ProjectBaseView.create_project, name='create_project'),
        # /view_projects/
        re_path(r'^project/all/', MyProjectsView.view_projects, name='view_projects'),
        # View individual project
        path('project/<str:slug>/', ProjectView.view_one_project, name='view_one_project'),
        # Edit individual project (based on slug)
        path('project/<str:slug>/edit/', EditProjectView.edit_project, name='edit_project'),
        # Post update for individual project (based on slug)
        path('project/<str:slug>/update/', ProjectView.post_update, name='post_update'),
        # Edit existing update to project (based on slug and update id)
        path('project/<str:slug>/update/<str:id>/', ProjectView.update_project_update, name='update_project_update'),
        # Delete existing update to project (based on slug and update id)
        path('project/<str:slug>/update/<str:id>/delete',ProjectView.delete_project_update, name='delete_project_update'),
        # Add new resource (based on slug)
        path('project/<str:slug>/resource/', ProjectView.resource_update, name='resource_update'),
        # Edit existing resource to project (based on slug and resource id)
        path('project/<str:slug>/resource/<str:id>/', ProjectView.update_resource_update, name='update_resource_update'),
        # Delete existing resource to project (based on slug and resource id)
        path('project/<str:slug>/resource/<str:id>/delete',ProjectView.delete_resource_update, name='delete_resource_update'),
        # Create Scrum Master TSR
        path('project/<str:slug>/tsr/<str:asg_slug>/smaster/', TsrView.create_scrum_master_tsr, name='create_scrum_master_tsr'),
        # Update TSR information
        path('project/<str:slug>/tsr/<str:asg_slug>/member/', TsrView.create_member_tsr, name='create_member_tsr'),
        # Edit TSR information
        path('project/<str:slug>/tsr/<str:asg_slug>/edit/', EditTsrView.tsr_edit, name='tsr_edit'),
        # View TSRs
        path('project/<str:slug>/view_tsr/', TsrView.view_tsr, name='view_tsr'),
        # View meeting times
        path('project/<str:slug>/meetings/', MeetingsView.view_meetings, name='view_meetings'),
        # Request to join Project
        path('project/<str:slug>/join/', ProjectView.request_join_project, name='request_to_join'),
        # Request to leave Project
        path('project/<str:slug>/leave/', EditProjectView.leave_project, name='leave_project'),
        # Add member to project
        path('project/<str:slug>/add/<str:uname>', EditProjectView.add_member, name='add_member'),
        # Try add member to project
        path('project/<str:slug>/tryadd/<str:uname>', EditProjectView.try_add_member, name='try_add_member'),
        # Add member to project
        path('project/<str:slug>/reject/<str:uname>', ProjectView.reject_member, name='reject_member'),
        # Email Members of Project
        path('project/<str:slug>/email_members/', ProjectBaseView.email_project, name='email_project'),
        # select members (select2)
        path('project/create/ajax/select_members/', core_helpers.select_members, name='select_members'),
        path('project/<str:slug>/edit/ajax/edit_select_members/', core_helpers.edit_select_members, name='edit_select_members'),
        path('project/<str:slug>/edit/ajax/add_desired_skills/', EditProjectView.add_desired_skills, name='add_desired_skills'),
        path('project/create/ajax/add_desired_skills/', EditProjectView.create_desired_skills, name='create_desired_skills'),

        # COURSE
        # Delete individual assignment (based on slug)
        path('assignment/<str:slug>/delete/', CourseView.delete_assignment, name='delete_assignment'),
        # Edit individual assignment (based on slug)
        path('assignment/<str:slug>/edit/', CourseView.edit_assignment, name='edit_assignment'),

        # View all courses
        path('course/', CourseBaseView.view_courses, name='view_course'),
        # Join a course (valid for all courses)
        path('course/join/', CourseBaseView.join_course, name='join_course'),
        # Create new course
        path('course/new/', CourseBaseView.create_course, name='create_course'),
        # View individual course (based on slug)
        path('course/<str:slug>/', CourseView.view_one_course, name='view_one_course'),
        # Delete individual course (based on slug)
        path('course/<str:slug>/delete_course/', EditCourseView.delete_course, name='delete_course'),
        # Drop from a course based on a slug
        #url(r'^course/(?P<slug>[^/]+)/drop/$', course_views.drop_course, name='drop_course'),
        # Edit individual course (based on slug)
        path('course/<str:slug>/edit/', EditCourseView.edit_course, name='edit_course'),
        # Stats page link
        path('course/<str:slug>/stats/', StatsView.view_stats, name='view_statistics'),
        # Email Roster link
        path('course/<str:slug>/email_roster/', EmailCourseView.email_roster, name='email_roster'),
        # Email w/ CSV
        path('course/<str:slug>/email_csv/', EmailCourseView.email_csv, name='email_csv'),
        # upload csv
        path('course/<str:slug>/upload_csv/', CourseBaseView.upload_csv, name='upload_csv'),
        # Auto Generation page link
        path('course/<str:slug>/auto_gen/', MatchesView.auto_gen, name='auto_gen'),
        # Setup link to assign students
        path('course/<str:slug>/auto_gen/assign/',MatchesView.assign_auto, name='assign_auto'),
        # Post update to course (based on slug)
        path('course/<str:slug>/update/', CourseView.update_course, name='update_course'),
        # Edit existing update to course (based on slug and update id)
        path('course/<str:slug>/update/<str:course_update_id>/', CourseView.update_course_update, name='update_course_update'),
        # Edit existing update to course (based on slug and update id)
        path('course/<str:slug>/update/<str:course_update_id>/delete', CourseView.delete_course_update, name='delete_course_update'),
        # Button to lock interest
        path('course/<str:slug>/lock/', EditCourseView.lock_interest, name='lock_interest'),
        # Button to Disable course
        path('course/<str:slug>/disable/', EditCourseView.disable, name='disable'),
        # link to show interest page
        path('course/<str:slug>/show_interest/',InterestView.show_interest, name='show_interest'),
        # select2 for course
        path('course/<str:slug>/edit/ajax/edit_select_members/', core_helpers.edit_select_members, name='edit_select_members'),
        # select2 for course
        # url(r'^course/(?P<slug>[^/]+)/claim/ajax/select_projects/$', course_views.select_projects, name='select_projects'),
        # Export Spreadsheet
        path('course/<str:slug>/export/', CourseBaseView.export_xls, name='export_xls'),
        # Export Interest
        path('course/<str:slug>/export_interest/', InterestView.export_interest, name='export_interest'),
        # Claim Projects (TA)
        path('course/<str:slug>/claim/', CourseView.claim_projects, name='claim_projects'),

        # ADMIN AND AUTH
        re_path(r'^admin/', admin.site.urls),
        re_path(r'^login', LoginView.login, name='login'),
        re_path(r'^logout', auth_views.logout, {'next_page': 'login'}, name='logout'),

        # PROFILE
        path('user/<str:username>/', ProfileView.view_profile, name='profile'),
        path('user/<str:username>/edit/', EditProfileView.edit_profile, name='edit_profile'),
        path('user/<str:username>/edit_schedule/', EditScheduleView.edit_schedule, name='edit_schedule'),
        path('user/<str:username>/edit_schedule/ajax/save_event/', EditScheduleView.save_event, name='save_event'),
        path('user/<str:username>/edit/ajax/edit_skills/', EditProfileView.edit_skills, name='edit_skills'),

        # MATCHES AND MATCHSTATS
        path('matches/', MatchesView.view_matches, name='view_matches'),
        # see why this user matches
        path('matchstats/<str:slug>/', MatchesView.matchstats, name='matchstats'),

        # favicon
        re_path(r'^favicon.ico$', RedirectView.as_view(url='/static/images/favicon.ico',permanent=True),name="favicon"),

        # alerts
        path('alerts/', AlertView.view_alerts, name="view_alerts"),
        path('alerts/<str:ident>/read/', AlertView.read_alert, name="read_alert"),
        path('alerts/<str:ident>/unread/', AlertView.unread_alert, name="unread_alert"),
        path('alerts/<str:ident>/delete/', AlertView.delete_alert, name="delete_alert"),
        path('alerts/readall/', AlertView.archive_alerts, name="archive_alerts"),

        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Django Toolbar Uncomment to turn on
#
# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ]
