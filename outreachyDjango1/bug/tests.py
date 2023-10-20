from django.test import TestCase
from django.urls import reverse

from outreachyDjango1.bug.models import Bug


# Create your tests here.
class BugModelTests(TestCase):

    def test_create_valid_bug(self):
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="Bug Type",
            report_date="2023-10-05",
            status="todo"
        )
        self.assertEqual(bug.description, "Test Bug")
        self.assertEqual(bug.bug_type, "Bug Type")
        self.assertEqual(bug.status, "todo")

    def test_create_invalid_bug(self):
        # Attempt to create a bug with missing required fields
        with self.assertRaises(Exception):
            bug = Bug.objects.create(description="Incomplete Bug")

    def test_bug_model_method(self, expected_result=None):
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="Bug Type",
            report_date="2023-10-05",
            status="todo"
        )
        # Test a custom method (if applicable)
        result = bug.custom_method()
        self.assertEqual(result, expected_result)

    def test_bug_model_data_integrity(self):
        # Create and save a bug to the database
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="Bug Type",
            report_date="2023-10-05",
            status="todo"
        )

        # Retrieve the bug from the database
        retrieved_bug = Bug.objects.get(pk=bug.pk)

        # Compare attributes to ensure data integrity
        self.assertEqual(bug.description, retrieved_bug.description)
        self.assertEqual(bug.bug_type, retrieved_bug.bug_type)
        self.assertEqual(bug.status, retrieved_bug.status)


class BugViewTests(TestCase):

    def test_bug_registration_view(self):
        # Simulate a POST request to register a bug
        response = self.client.post(reverse('bug-registration'), {
            'description': 'Test Bug',
            'bug_type': 'Bug Type',
            'report_date': '2023-10-05',
            'status': 'todo',
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect on success
        self.assertEqual(Bug.objects.count(), 1)  # Ensure the bug is saved

    def test_bug_listing_view(self):
        # Create multiple bug instances in the test database
        Bug.objects.create(description='Bug 1', bug_type='Type 1', report_date='2023-10-01', status='todo')
        Bug.objects.create(description='Bug 2', bug_type='Type 2', report_date='2023-10-02', status='in_progress')

        response = self.client.get(reverse('bug-list'))
        self.assertEqual(response.status_code, 200)  # Expect a successful response
        self.assertContains(response, 'Bug 1')  # Verify that bug data is displayed

    def test_bug_detail_view(self):
        # Create a bug instance in the test database
        bug = Bug.objects.create(description='Test Bug', bug_type='Bug Type', report_date='2023-10-05', status='todo')

        response = self.client.get(reverse('bug-detail', args=(bug.id,)))
        self.assertEqual(response.status_code, 200)  # Expect a successful response
        self.assertContains(response, 'Test Bug')  # Verify that bug details are displayed







