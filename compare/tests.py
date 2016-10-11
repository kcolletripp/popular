from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_pushlied_recently() should return False for questions whose pub_date is in the future
        """
        tomorrow = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=tomorrow)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return true for questions whose pub_date is within 1 day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

def create_question(q_text, d):
    """
    Creates a question with the question_text: 'q_text' and published the given
    number of 'd' days offset to now (neg for questions published in past, pos for future)
    """
    time = timezone.now() + datetime.timedelta(days=d)
    return Question.objects.create(question_text=q_text, pub_date=time)

class QuestionViewTests(TestCase):

    def test_index_view_with_no_questions(self):
        """
        If not questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('compare:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the index page
        """
        create_question("Past question.", -30)
        response = self.client.get(reverse('compare:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Question with a pub_date in the future should not be displayed on the index page.
        """
        create_question("Future question.", 30)
        response = self.client.get(reverse('compare:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        If both kind exist, only past questions should be displayed
        """
        create_question("Past question.", -30)
        create_question("Future question.", 30)
        response = self.client.get(reverse('compare:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        Can display multiple questions
        """
        create_question("Past question 1.", -30)
        create_question("Past question 2.", -5)
        response = self.client.get(reverse('compare:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with pub_date in the future should return 404
        """
        future_question = create_question('Future queston.', 5)
        url = reverse('compare:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should display the question's text
        """
        past_question = create_question('Past Question.', -5)
        url = reverse('compare:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        
